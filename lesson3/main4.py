"""
На вход подаётся число от 1 до 9. Вам нужно вывести таблицу умножения на это число.

Тест:

Входные данные:

5

Выходные данные:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
"""
init_number = int(input())
ans = [print(f"{init_number} x {x} = {x * init_number}") for x in range(1, 10 + 1)]
