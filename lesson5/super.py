import random
import math
import time
import datetime


def random_character(stdin):
    """
    Задание 1

    Напишите функцию random_char(), которая принимает строку и возвращает случайный
    символ из этой строки.
    """
    return random.choice(stdin)


def area_and_length(stdin):
    """

    Задание 2

    Напишите функцию area_and_length(), которая принимает одно целое число
    – радиус окружности. Функция должна возвращать площадь круга и длину окружности.

    Результат округлите до сотых.

    Для выполнения этого задания воспользуйтесь модулем math
    input:
    23
    output:
    Area = 1661.9; Length = 144.51
    """

    return (f"Area = {round(math.pi * float(stdin) * float(stdin), 2)};"
            f" Length = {round(2 * math.pi * float(stdin), 2)}")


def timer(stdin):
    """
    Задание 3

    Напишите функцию timer(), которая получает время в секундах и выводит сообщение по истечении этого времени.

    Для выполнения этого задания воспользуйтесь модулем time
    input:
    5
    output:
    Время вышло! Прошло 5 секунд.
    """
    time.sleep(int(stdin))
    return f"Время вышло! Прошло {stdin} секунд."


def time_to_seconds(text_input):
    """
    Задание 4

    Напишите функцию time_to_seconds(), которая принимает время в формате ЧЧ:ММ:СС
    и форматирует его в секунды.

    Используйте модуль datetime, а именно метод datetime.datetime.strptime()
    для создания объекта времени, после чего воспользуйтесь методами .second, .minute и т.д.
    для подсчета общего количества секунд

    input:
    05:05:05
    output:
    18305
    """
    frame = datetime.datetime.strptime(text_input, '%H:%M:%S')
    return frame.hour * 3600 + frame.minute * 60 + frame.second


def discriminant_root(stdin):
    """
    Задание 5

    Напишите discriminant_root() функцию для вычисления корня дискриминанта в уравнении,
    с заданными целыми коэффициентами a, b, c (подаются в виде строки через пробел).
    Если дискриминант меньше нуля, верните строку “Дискриминант меньше нуля”
    input:
    2 -7 3
    output:
    5
    """
    a, b, c = stdin.split()
    D = math.pow(b, 2) - 4 * a * c
    if D < 0:
        return "Дискриминант меньше нуля"
    return math.sqrt(D)
