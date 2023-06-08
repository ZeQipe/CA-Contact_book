from bl_lower import *

"""
Здесь функция вывода времени и типа сообщения
"""


def ti_and_inf():
    text = '\033[32m Info\033[0m'
    return f'\033[33m{t_now()}\033[0m   ' + text + ':  '


def ti_and_war():
    text = '\033[31m Error\033[0m'
    return f'\033[33m{t_now()}\033[0m  ' + text + ':  '


def ti_and_you():
    text = '\033[34m Your\033[0m'
    return f'\033[33m{t_now()}\033[0m   ' + text + ':  '


"""
Функции вывода сообщений
"""


def welcome():
    print(f'{ti_and_inf()} Программа запущена и готова к работе!')


def reminder():
    print(f'                    Выберите следующее действие (help - Вывести команды):')


def goodbye():
    print(f'{ti_and_inf()} Работа программы завершена!')


"""
Функции вывода информации о командах
"""


def book_com_info():
    print(f'{ti_and_inf()} open - Открыть адресную книгу\n'
          f'                    list - Вывести список достпуных книг\n'          
          f'                    now  - Создать адресную книгу\n'
          f'                    rem  - Удалить адресную книгу\n'
          f'                    book - Открыть папку с конвертированными файлами\n'               
          f'                    stop - Завершение работы')


def contact_com_info():
    print(f'{ti_and_inf()} add - Добавить контакт\n'
          f'                    del - Удалить контакт\n'
          f'                    read - Вывести весь список контактов\n'
          f'                    search - Поиск контакта в книге\n'
          f'                    edit - Редактировать контакт в книге\n'
          f'                    change - Cменить адресную книгу\n'
          f'                    convert - Конвертировать адресную книгу\n'
          f'                    book - Открыть папку с конвертированными файлами\n'  
          f'                    stop - Завершение работы')


"""
Работа с адресными книгами.
"""


def book():
    print(f'{ti_and_inf()} Необходимо выбрать адресную книгу:')
    book_com_info()
    while True:
        com = input(f'{blu.ti_and_you()} > ')
        result_b = input_com_book(com)
        if result_b == 'stop':
            return False
        elif not result_b:
            continue
        else:
            return result_b


# проверка команды и исполнение
def input_com_book(var):
    if var == 'stop':
        return var

    elif var == 'open':
        print(f'{ti_and_inf()} Введите имя адресной книги:')
        name = input(f'{ti_and_you()} > ')
        if name == 'stop':
            return name
        elif name == 'break':
            return
        buff = open_books(name)
        if buff == 'stop':
            return buff
        elif buff:
            return name

    elif var == 'now':
        print(f'{ti_and_inf()} Введите имя адресной книги:\n'
              f'                    break - отменить создание адресной книги')
        name = input(f'{ti_and_you()} > ')
        if name == 'stop':
            return name
        elif name == 'break':
            print(f'{ti_and_inf()} Вы отменили добавление адресной книги!')
            reminder()
            return
        else:
            create_book(name)

    elif var == 'rem':
        if list_books():
            print(f'{ti_and_inf()} Введите имя адресной книги, которую надо удалить:\n'
                  f'                    break - Отменить удаление!')
            name = input(f'{ti_and_you()} > ')
            if name + '.data' in os.listdir(r'books'):
                del_book(name)
                reminder()
            elif name == 'stop':
                return name
            elif name == 'break':
                print(f'{ti_and_inf()} Вы отменили удаление адресной книги!')
                reminder()
                return
            elif name == '':
                print(f"{ti_and_war()} Вы не ввели имя адресной книги, попробуйте еще раз!")
                reminder()
                return
            else:
                del_book(name)
                reminder()
        else:
            reminder()

    elif var == 'list':
        list_books()
        reminder()

    elif var == 'help':
        book_com_info()

    elif var == 'book':
        exists_file_convert()
        os.system(r"explorer.exe Convert Books")
        reminder()

    else:
        print(f'{ti_and_war()} Такой команды не обнаружено')
        reminder()


"""
Работа с контактами.
"""


def contact(name_book):
    print(f'{ti_and_inf()} Для работы со списком контактов, выберите действие:')
    contact_com_info()
    while True:
        com = input(f'{ti_and_you()} > ')
        result_c = input_com_contact(name_book, com)
        if result_c == 'stop':
            return False
        elif result_c == 'rep':
            return True
        elif result_c == 'change':
            return result_c


def input_com_contact(name_book, var):
    if var == 'stop':
        return var

    elif var == 'add':
        buff = add_contact(name_book)
        if buff == 'stop':
            return buff
        elif buff == 'break':
            print(f'{ti_and_inf()} Вы отменили добавление контакта')
            blu.reminder()
            return
        blu.reminder()

    elif var == 'del':
        if not read_cont(name_book):
            print(f'{ti_and_war()} Список контактов пуст!')
            reminder()
            return
        target = input_target()
        if target == 'stop':
            return target
        elif target == 'break':
            print(f'{ti_and_inf()} Вы отменили удаление контакта')
            blu.reminder()
            return
        if check_target_in_lst(name_book, target):
            print(f'{ti_and_war()} Таких контактов не обнаружено.')
            reminder()
            return
        optional = option_del(name_book, target)
        if optional == 'stop':
            return optional
        elif optional == 'break':
            print(f'{ti_and_inf()} Вы отменили удаление контакта')
            blu.reminder()
            return

    elif var == 'read':
        lst = read_cont(name_book)
        if lst:
            print(f'{ti_and_inf()} Список всех контактов в этой адресной книге:')
            for i in range(len(lst)):
                print(f'                    {i + 1}) {" ".join(lst[i])}', end='')
        else:
            print(f'{ti_and_war()} Список контактов пуст!')
        reminder()

    elif var == 'edit':
        if not read_cont(name_book):
            print(f'{ti_and_war()} Список контактов пуст!')
            reminder()
            return
        target = input_target()
        if target == 'stop':
            return target
        elif target == 'break':
            print(f'{ti_and_inf()} Вы отменили редактирование контакта')
            blu.reminder()
            return
        if check_target_in_lst(name_book, target):
            print(f'{ti_and_war()} Таких контактов не обнаружено.')
            reminder()
            return
        buff = red_contact(name_book, target)
        if buff == 'stop':
            return buff
        elif buff == 'break':
            print(f'{ti_and_inf()} Вы отменили редактирование контакта')
            blu.reminder()
            return

    elif var == 'search':
        if not read_cont(name_book):
            print(f'{ti_and_war()} Список контактов пуст!')
            reminder()
            return
        buff = ser_contact(name_book)
        if buff == 'stop':
            return buff
        elif buff == 'break':
            print(f'{ti_and_inf()} Вы отменили поиск контакта')
            blu.reminder()
            return

    elif var == 'change':
        return var

    elif var == 'help':
        contact_com_info()

    elif var == 'convert':
        if not read_cont(name_book):
            print(f'{ti_and_war()} Список контактов пуст!')
            reminder()
            return
        buff = convert_opt(name_book)
        if buff == 'stop':
            return buff
        elif buff == 'break':
            print(f'{ti_and_inf()} Вы отменили конвертацию адресной книги')
            blu.reminder()
            return
        reminder()

    elif var == 'book':
        exists_file_convert()
        os.system(r"explorer.exe Convert Books")
        reminder()

    else:
        print(f'{blu.ti_and_war()} Такой команды не обнаружено')
        reminder()
