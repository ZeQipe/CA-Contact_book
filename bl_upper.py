from bl_lower import *

"""
Здесь функция вывода времени и типа сообщения
"""


def ti_and_inf():
    return f'{t_now()}    INFO:  '


def ti_and_war():
    return f'{t_now()}   Error:  '


def ti_and_you():
    return f'{t_now()}    YOUR:  '


"""
Функции вывода сообщений
"""


def welcome():
    print(f'{ti_and_inf()} Программа запущена и готова к работе!')


def goodbye():
    print(f'{ti_and_inf()} Работа программы завершена!')


"""
Функции вывода информации о командах
"""


def book_com_info():
    print(f'{ti_and_inf()} open - Открыть адресную книгу\n'
          f'                    list - Вывести список достпуных книг\n'          
          f'                    now  - Создать адресную книгу\n'
          f'                    del  - Удалить адресную книгу\n'
          f'                    stop - Завершение работы')


"""
Работа с адресной книгой.
"""


def book():
    print(f'{ti_and_inf()} Выберите адресную книгу или введите другое действие')
    while True:
        book_com_info()
        com = input_com_book()
        if not com:
            return False
        return com
