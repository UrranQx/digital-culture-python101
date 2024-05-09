"""
Объявите функцию analyze_prices, которая принимает список цен на товары,
находит максимальное, минимальное значения и сумму значений этого списка
и выводит результат в виде строки (без кавычек):

"Min = v_min, max = v_max, sum = v_sum"

где v_min, v_max, v_sum - вычисленные значения минимального,
максимального значений и суммы значений списка.

Файл с решением должен иметь название task4_5.py, название функции - def analyze_prices().
Вызывать в скрипте функцию не нужно.

Тест: Вход:

20 50 10 100

Выход:

Min = 10, max = 100, sum = 180
"""


def analyze_prices(input_text):
    prices_list = [int(x) for x in input_text.split()]
    return f"Min = {min(prices_list)}, max = {max(prices_list)}, sum = {sum(prices_list)}"
