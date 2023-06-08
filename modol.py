from bl_upper import *


def main():
    welcome()
    start()
    goodbye()
    input(f'                    Нажмите ENTER чтобы закрыть консоль.')


def start():
    while True:
        name_book = book()
        if not name_book:
            return
        contact_result = contact(name_book)
        if not contact_result:
            return
        elif contact_result == 'change':
            continue
