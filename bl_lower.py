import bl_upper as blu
import datetime as dt
import os


"""
Здесь функция для возрата времени.
"""


def t_now():
    now = dt.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


"""
Реализация работы с адресными книгами
"""


# Вывод директории для контактных книг
def directions(name):
    return os.path.join('books', name)


# проверка на наличие файла
def exists_file(name=''):
    if os.path.exists('books'):
        if os.path.exists(directions(name)):
            return True
        else:
            return False
    else:
        os.mkdir('books')
        return True if exists_file(name) else False


# Вывод списка существующих книг
def list_books():
    exists_file()
    books = os.listdir(r'books')
    if not books:
        print(f'{blu.ti_and_war()} Адресные книги отсутсвуют')
    else:
        lst = "\n                    - ".join(books)
        print(f'{blu.ti_and_inf()} Список доступных книг:\n'
              f'                    - {lst}')
    blu.reminder()


# создание контактной книги
def create_book(name):  # Готов
    if not exists_file(name):
        file = open(directions(name), 'a')
        file.close()
        print(f'{blu.ti_and_inf()} Файл успешно создан!') # уведомим об успехе
    else:
        print(f'{blu.ti_and_war()} Такая адресная книга уже существует!')
    blu.reminder()


# Удаление контактной книги
def del_book(name):
    if exists_file(name):
        os.remove(directions(name))
        print(f'{blu.ti_and_inf()} Файл успешно удалён!') # уведомим об успехе
    else:
        print(f'{blu.ti_and_war()} Такой адресной книги не существует!')
        blu.reminder()


# Открытие контактной книги
def open_books(name):
    if exists_file(name):
        print(f'{blu.ti_and_inf()} Адресная книга успешно выбрана!')
        return True
    else:
        print(f'{blu.ti_and_war()} Такой адресной книги не существует!\n'
              f'                    Создать с таким именем? (y/n):')
        while True:
            var = input(f'{blu.ti_and_you()} >')
            if var == 'stop':
                return var
            elif var == 'y':
                create_book(name)
                return True
            elif var == 'n':
                blu.reminder()
                return False
            else:
                print(f'{blu.ti_and_war()} Такая команда не обнаружена в этом меню\n'
                      f'                    Выберите "y" что бы создать или "n" что бы вернуться к прошлому меню:')


"""
Реализация работы с контактами
"""


# Рализация добавления контакта в адресную книгу
def add_contact(name):
    contact = []
    print(f'{blu.ti_and_inf()} Введите ИМЯ')
    names = input_contact_info()
    if names == 'stop' or names == 'back':
        return names
    contact.append(names)
    print(f'{blu.ti_and_inf()} Введите ФАМИЛИЮ')
    surnames = input_contact_info()
    if surnames == 'stop' or surnames == 'back':
        return surnames
    contact.append(surnames)
    print(f'{blu.ti_and_inf()} Введите НОМЕР')
    number = input_contact_info()
    if number == 'stop' or number == 'back':
        return number
    contact.append(number)
    print(f'{blu.ti_and_inf()} Введите ПОЧТОВЫЙ АДРЕС')
    email = input_contact_info()
    if email == 'stop' or email == 'back':
        return email
    contact.append(email + ' \n')
    file = open(directions(name), 'a+')
    file.write(' '.join(contact))
    file.close()
    print(f'{blu.ti_and_inf()} Контакт успешно записан')


def input_contact_info():
    while True:
        buff = input(f'{blu.ti_and_you()} > ')
        if ' ' in buff:
            print(f'{blu.ti_and_war()} Введите без пробелов:')
        else:
            return buff


# Реализация удаления контакта
def input_target():
    print(f'{blu.ti_and_inf()} Введите ИМЯ и/или ФАМИЛИЮ')
    target = input(f'{blu.ti_and_you()} > ')
    return target


def check_target_in_lst(name, target):
    lst = list(filter(lambda x: target in x, read_cont(name)))
    return True if not lst else False


def option_del(name, target):
    check = list(filter(lambda x: target in x, read_cont(name)))
    print(f'{blu.ti_and_inf()} Вот что удалось обнаружить:')
    for i in range(len(check)):
        print(f'                    {i+1}) {" ".join(check[i])}', end='')
    print(f'\n{blu.ti_and_inf()} Удалить все вхождения контакта (all) или конкретный (one)? '
          f'back - Отменить удаление')
    while True:
        opt = input(f'{blu.ti_and_you()} > ')
        if opt == 'stop' or opt == 'back':
            return opt
        elif opt == 'all':
            del_all_target(name, target)
            return
        elif opt == 'one':
            buff = search_del_cont(name, target, check)
            if buff == 'stop' or buff == 'back':
                return buff
            return
        else:
            print(f'{blu.ti_and_war()} Такая команда не обнаружена в этом меню\n'
                  f'                    Введите "all" или "one", "back" - отменить удаление:')


def search_del_cont(name, target, check):
    print(f'{blu.ti_and_inf()} Введите номер контакта, который надо удалить:')
    while True:
        index_target = input(f'{blu.ti_and_you()} > ')
        if index_target == 'stop' or index_target == 'back':
            return index_target
        elif index_target.isdigit():
            index_target = int(index_target)
            if 0 < index_target < (len(check) + 1):
                del check[index_target - 1]
                break
            else:
                print(f'{blu.ti_and_war()} Не правильный порядковый номер, попробуйте еще раз')
        else:
            print(f'{blu.ti_and_war()} Введите число, пожалуйста.')
    write_after_del(name, del_index_target(name, check, target))
    print(f'{blu.ti_and_inf()} Контакт успешно удалён.')
    blu.reminder()


def del_index_target(name, check, target):
    lst = read_cont(name)
    count = 0
    for i in range(len(lst)):
        for j in lst[count]:
            if target == j:
                del lst[count:count + 1:]
                count -= 1
                break
        count += 1
    return lst + check


def del_all_target(name, target):
    lst = read_cont(name)
    count = 0
    for i in range(len(lst)):
        for j in lst[count]:
            if target == j:
                del lst[count:count + 1:]
                count -= 1
                break
        count += 1
    write_after_del(name, lst)
    print(f'{blu.ti_and_inf()} Успешно удалены все вхождения контакта')
    blu.reminder()


def write_after_del(name, lst):
    file = open(directions(name), 'w')
    lst1 = []
    for i in lst:
        lst1.append(' '.join(i))
    for i in lst1:
        file.write(i)
    file.close()


# Реализация поиска контакта
def ser_contact(name):
    while True:
        print(f'{blu.ti_and_inf()} Введите ИМЯ или ФАМИЛИЮ для поиска контакта')
        target = input(f'{blu.ti_and_you()} >')
        if target == 'stop' or target == 'back':
            return target
        check = list(filter(lambda x: target in x, read_cont(name)))
        if check:
            print(f'{blu.ti_and_inf()} Есть совпадения, вот результаты поиска:')
            result(check)
            blu.reminder()
            return
        else:
            print(f'{blu.ti_and_war()} Совпадений не найдено, повторить с другим именем? (y/n)')
            while True:
                var = input(f'{blu.ti_and_you()} >')
                if var == 'y':
                    break
                elif var == 'n':
                    return
                elif var == 'stop' or var == 'back':
                    return var
                else:
                    print(f'{blu.ti_and_war()} Введите "y" или "n"')


def read_cont(name):
    file = open(directions(name), 'r')
    lst = []
    for buff in file.readlines():
        cont = buff.split(' ')
        lst.append(cont)
    file.close()
    return lst


def result(filtering):
    for i in filtering:
        print('                      ', ' '.join(i), end='')
    print('')


# Реализация редактирования контакта
def red_contact(name, target):
    check = list(filter(lambda x: target in x, read_cont(name)))
    print(f'{blu.ti_and_inf()} Вот что удалось обнаружить:')
    for i in range(len(check)):
        print(f'                    {i + 1}) {" ".join(check[i])}', end='')
    print(f'{blu.ti_and_inf()} Введите поряковый номер контакта, который необходимо изменить:')
    while True:
        index_target = input(f'{blu.ti_and_you()} > ')
        if index_target == 'stop' or index_target == 'back':
            return index_target
        elif index_target.isdigit():
            index_target = int(index_target)
            if 0 < index_target < (len(check) + 1):
                lst = read_cont(name)
                index = lst.index(check[index_target - 1])
                buff = redact_cont(check[index_target - 1])
                if buff == 'stop' or buff == 'back':
                    return buff
                lst[index] = buff
                file = open(directions(name), 'w')
                for i in lst:
                    file.write(' '.join(i))
                file.close()
                print(f'{blu.ti_and_inf()} Контакт успешно отредактирован!')
                blu.reminder()
                break
            else:
                print(f'{blu.ti_and_war()} Не правильный порядковый номер, попробуйте еще раз')
        else:
            print(f'{blu.ti_and_war()} Введите число, пожалуйста.')


#
def redact_cont(contact):
    print(f'{blu.ti_and_inf()} Вот выбранный вами контакт:\n'
          f'                    {" ".join(contact)}'
          f'                    Что необходимо изменить в контакте?\n'
          f'                    Имя (name), Фамилию (sur), Номер (num), Почтовый адрес (mail):')
    while True:
        var = input(f'{blu.ti_and_you()} > ')
        if var == 'stop' or var == 'back':
            return var
        elif var == 'name':
            return opt_red(contact, 0)
        elif var == 'sur':
            return opt_red(contact, 1)
        elif var == 'num':
            return opt_red(contact, 2)
        elif var == 'mail':
            return opt_red(contact, 3)
        else:
            print(f'{blu.ti_and_war()} Выберите какой параметр изменить или back что бы отменить редактирование')


def opt_red(contact, val):
    print(f'{blu.ti_and_inf()} Введите новое значение:')
    buff = input(f'{blu.ti_and_you()} > ')
    if buff == 'stop' or buff == 'back':
        return buff
    contact[val] = buff
    return contact


def convert_opt(name):
    print(f'{blu.ti_and_inf()} В какой формат конвертировать файл? (vcf / csv)')
    while True:
        var = input(f'{blu.ti_and_you()} > ')
        if var == 'stop' or var == 'back':
            return var
        elif var == 'vcf':
            convert_vcf(name)
        elif var == 'csv':
            convert_csv(name)
        else:
            print(f'{blu.ti_and_war()} Выберите формат vcf или csv, back - отменить конвертацию')


def convert_vcf(name):
    pass


def convert_csv(name):
    pass
