"""
Задание 1

Запросите у пользователя его имя и выведите приветственное сообщение с его именем.



Задание 2

Запросите у пользователя цену товара и выведите цену на этот же товар с учётом НДС в 10%.



Задание 3

Запросите у пользователя количество товара, который он хочет приобрести и его количество. Выведите общую стоимость всей покупки.



Задание 4

Запросите у пользователя размер его ежемесячного дохода. Разделите его бюджет на траты и сбережения в соотношении 3 к 1. Выведите сумму его сбережений, которую он может накопить за год.



Задание 5

Напишите программу, которая принимает строку чисел через пробел и выводит наибольшее число.
"""


def task1():
    print(f"Oh I see, {input("Hello, what's your name?\n")}! Nice to meet you")


def task2():
    print(f'Total price will be: {float(input("Please, enter the product initial price: ")) * 110 / 100}')


def task3():
    price = float(input("Enter price of one product: "))
    quantity = int(input("Enter amount of products: "))
    print(f"Total price = {price * quantity}")


def task4():
    """
    Запросите у пользователя размер его ежемесячного дохода.
    Разделите его бюджет на траты и сбережения в соотношении 3 к 1.
    Выведите сумму его сбережений, которую он может накопить за год.
    """
    monthly_income = float(input("enter your monthly income"))
    buys, savings = monthly_income * 0.75, monthly_income * 0.25
    print(f"Your savings for year = {savings * 12}")


def task5():
    numbers = input().split(" ")
    print(max(numbers))


