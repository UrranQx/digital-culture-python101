"""
Напишите функцию area_and_length(), определяющую площадь круга и длину окружности,
по заданному радиусу R. Используйте модуль math

! Результат округлите до сотых

Вывод результата в виде строки (без кавычек):
"Circle area = circle_area, circle length = circle_length"

Файл с решением должен иметь название task5_2.py, название функции - def area_and_length().
Вызывать в скрипте функцию не нужно.

Тестовый пример:

area_and_length(23)

Вывод:
Circle area = 1661.9, circle length = 144.51
"""
import math


def area_and_length(stdin):
    return (f"Circle area = {round(math.pi * float(stdin) * float(stdin), 2)},"
            f" circle length = {round(2 * math.pi * float(stdin), 2)}")
