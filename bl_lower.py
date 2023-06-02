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
        if var == 'open':
            pass
        if var == 'now':
            pass
        if var == 'del':
            pass
        if var == 'list':
            list_books()
        else:
            print(f'{blu.ti_and_war()} Такой команды не обнаружено')


def list_books():
    books = os.listdir(r'D:\Обучение\Проекты\contact_book\book')
    if not books:
        print(f'{blu.ti_and_war()} Адресные книги отсутсвуют\n'
              f'                    Выберите следующее действие (help - Вывести команды):')
    else:
        lst = "\n                    - ".join(books)
        print(f'{blu.ti_and_inf()} Список доступных книг:\n'
              f'                    - {lst}\n'
              f'                    Выберите следующее действие (help - Вывести команды):')



def create_book(name):  # Готов
    file = open(name, 'a')
    file.write('')
    file.close()
    print(t_now(), '    INFO:    ', 'Адресная книга создана и выбрана')  # уведомим об успехе
