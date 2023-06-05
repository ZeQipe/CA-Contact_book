from bl_upper import *
from bl_lower import *


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
        if not contact(name_book):
            return
