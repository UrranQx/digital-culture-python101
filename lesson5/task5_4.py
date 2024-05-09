"""
Напишите функцию, которая принимает время в формате ЧЧ:ММ:СС и возвращает количество секунд.

Вывод результата в виде строки (без кавычек):

"Всего секунд: total_seconds"

Файл с решением должен иметь название task5_4.py, название функции - def seconds_total().
Вызывать в скрипте функцию не нужно.

Подсказка: используйте модуль datetime, а именно метод datetime.datetime.strptime()
для создания объекта времени, после чего воспользуйтесь методами .second, .minute и т.д.
для подсчета общего количества секунд

Тестовый пример:

seconds_total('05:05:05')

Вывод:

Всего секунд: 18305
"""
import datetime


def seconds_total(text_input):
    frame = datetime.datetime.strptime(text_input, '%H:%M:%S')
    return f"Всего секунд: {frame.hour * 3600 + frame.minute * 60 + frame.second}"
