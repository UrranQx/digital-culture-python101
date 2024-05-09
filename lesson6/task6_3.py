"""
Объявите функцию read_file,
которая на вход получает имя txt файла в виде строки и записывает каждую строку в список,
который в конце выводит.

Допустим, есть файл test.txt:

test string
new string

Тогда функция должна вернуть список вида ['test string', 'new string']

Файл с решением должен иметь название task6_3.py, название функции - def read_file().
Вызывать в скрипте функцию не нужно.

Важно: создавать файл не нужно, нужно его прочитать.

Подсказка: обращайтесь с объектом файла, как со списком (чтобы пройтись по всем строкам файла).
"""


def read_file(stdin):
    with open(stdin) as file:
        return [line.strip() for line in file]
