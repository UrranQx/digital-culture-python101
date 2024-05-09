"""
Напишите функцию random_character() для вывода случайного символа из заданной строки

Файл с решением должен иметь название task5_1.py, название функции - def random_character().
Вызывать в скрипте функцию не нужно

Пример ввода:
world

Вывод:

r
"""
import random


def random_character(stdin):
    return random.choice(stdin)

