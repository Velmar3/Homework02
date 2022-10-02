# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# number = input('Введите вещественное число: ')
# suma = 0
# for digit in number:
#     if digit.isdigit():
#         suma += int(digit)

# print("Сумма:", suma)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# 	пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')

# Задайте список из n чисел последовательности 〖(1+1/n)〗^n  и выведите на экран их сумму.

# n = int(input('Введите число: '))
# def sequence(n):

#     return [round((1 + 1 / n)**n, 2) for x in range(1, n + 1)]

# print(sequence(n))
# print(round(sum(sequence(n))))

# Реализуйте алгоритм перемешивания списка.

# list = ['Перемешивание списка', 9, 9.99, 'работает!']
# print(list)
# import random
# random.shuffle(list)
# print('->', list)