# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

a = float(input('Введите число --> '))
str_a = str(a)
str_a = str_a.replace('.', '')
line_str = list(str_a)
line_num = map(int, line_str)
s = sum(line_num)
print(s)

print()

# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число --> '))
def set_composition(n):
    proiz = 1
    pro = []
    for i in range(1, n+1):
        proiz *= i
        pro.append(proiz)
    return pro
print(set_composition(n))
print()

# Задайте список из n чисел последовательности
# (1+1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число --> '))

def pop_fun(n):
    return [round((1 + 1 / n)**n, 2)
    for n in range (1, n + 1)]

summ = pop_fun(n)
print(summ)
print(round(sum(summ), 2))
print()

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = int(input('Введите число --> '))
def composition_element(n):
    for i in range(-n, n):
        x = randint(-n, n)
        y = randint(-n, n)
        result = x*y
    print(f'[{-n} , {n}]')
    print(f'одно число из промежутка = {x}, второе число из промежутка = {y}')
    return result
print(f'произведение равно {composition_element(n)}')
print()

# Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)
new_list = random.sample(list, k=len(list))
print(new_list)
