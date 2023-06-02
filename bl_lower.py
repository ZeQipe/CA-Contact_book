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
Здесь функция выбора книги
"""


def input_com_book():
    while True:
        var = input(f'{blu.ti_and_you()} > ')
        if var == 'stop':
            return False
        elif var == 'open':
            pass
        elif var == 'now':
            print(f'{blu.ti_and_inf()} Введите имя адресной книги:')
            name = input(f'{blu.ti_and_you()} > ')
            if name == 'stop':
                return False
            else:
                create_book(name)
        elif var == 'del':
            pass
        elif var == 'list':
            list_books()
        elif var == 'help':
            blu.book_com_info()
        else:
            print(f'{blu.ti_and_war()} Такой команды не обнаружено')


def directions(name):
    return os.path.join('books', name)


def list_books():
    if os.path.exists('books'):
        books = os.listdir(r'books')
        if not books:
            print(f'{blu.ti_and_war()} Адресные книги отсутсвуют\n'
                  f'                    Выберите следующее действие (help - Вывести команды):')
        else:
            lst = "\n                    - ".join(books)
            print(f'{blu.ti_and_inf()} Список доступных книг:\n'
                  f'                    - {lst}\n'
                  f'                    Выберите следующее действие (help - Вывести команды):')
    else:
        os.mkdir('books')
        list_books()

def create_book(name):  # Готов
    book_dir = directions(name)
    if not os.path.exists(book_dir):
        file = open(directions(name), 'a')
        file.write('')
        file.close()
        print(blu.ti_and_inf(), ' Адресная книга создана! Что дальше?')  # уведомим об успехе
    else:
        print(blu.ti_and_war(),' Такая адресная книга уже есть! Следующее действие?')
