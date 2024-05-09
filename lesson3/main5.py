"""
На вход подаётся число N. Вывести все числа от 1 до N,
которые являются палиндромами, одной строкой через пробел.

Палиндромом считается то число, которое слева направо
и справа налево читается одинаково (числа от 1 до 9 не являются палиндромами).

Тест:

Входные данные:

101

Выходные данные:

11 22 33 44 55 66 77 88 99 101
"""


def is_palindrome(array):
    size = len(array)
    if size == 1:
        return False
    for index in range(size // 2):
        if array[index] != array[-1 - index]:
            return False
    return True


number = int(input())
for i in range(number + 1):
    analytic_array = str(i)
    if is_palindrome(analytic_array):
        print(analytic_array, end=" ")
