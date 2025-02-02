"""
Напишите фукнцию-таймер, которая получает время в секундах и выводит сообщение по истечении этого времени. Используйте модуль time

Вывод результата в виде строки (без кавычек):

"Время истекло! 5 секунд прошло."

Файл с решением должен иметь название task5_3.py, название функции - def timer(). Вызывать в скрипте функцию не нужно.

Тестовый пример:

timer(5)

Вывод:

Время истекло! 5 секунд прошло.
"""
import time


def timer(stdin):
    time.sleep(int(stdin))
    return f"Время истекло! {stdin} секунд прошло."
