"""
Требуется написать программу, которая проверяет,
делится ли введенное с клавиатуры число на 2 без остатка.
Если число делится нацело, программа должна вывести "Число делится на 2 без остатка",
иначе программа должна вывести "Число не делится на 2 без остатка".

Тест:

Входные данные:

10

Выходные данные:

Число делится на 2 без остатка.
"""
print("Число" + ' не' * (int(input()) % 2) + ' делится на 2 без остатка')
