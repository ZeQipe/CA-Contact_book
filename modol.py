from bl_upper import *
from bl_lower import *


def main():
    welcome()
    start()
    goodbye()


def start():
    while True:
        name_book = book()
        if not name_book:
            return
