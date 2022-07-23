# Вычислить число pi c заданной точностью d Пример:
# - при d = 0.001, π = 3.141.$    10^{-1} ≤ d ≤10^{-10}

# формула Бэйли-Боруэйна-Плаффа

n = 100
my_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))
print(my_pi)

a = round(my_pi, 3)
print(a)
print()

# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Введите натуральное число --> '))
def simple_multiplier(n):
    i = 2
    simple = []
    while i*i <= n:
        while n%i == 0:
            simple.append(i)
            n /= i
        i += 1
    if n > 1:
        simple.append(n)
    return simple
print(simple_multiplier(n))
print()

# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

my_list = [1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9]

def nonrepeating_element(my_list):
    new_my_list = []
    unique_element = set(my_list)
    for my_list in unique_element:
        new_my_list.append(my_list)
    return new_my_list
print(my_list)
print(nonrepeating_element(my_list))
print()

# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import itertools
from random import randint

k = randint(2, 7) # задаём рандомно натуральную степень k 
def look_ratio(k):
    ratio = [randint(0, 101) for i in range(k + 1)] # формируем случайным образом список коэффициентов
    while ratio[0] == 0:
        ratio[0] = randint(1, 101)
    print(f'{ratio} - список коэффициентов, сформированный случайным образом')
    print()
    return ratio
    
def look_polynomial(k, ratio):
    exi = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratio, exi, range(k, 1, -1), fillvalue= '') if a != 0]
# с помощью этого метода объединяем несколько списков в список кортежей    
    # print(f'{polynomial} - заготовочка')
    # print()
    for x in polynomial:
        x.append(' + ') # добавляем + между кортежами
    polynomial = list(itertools.chain(*polynomial)) # объединяем в один список
    polynomial[-1] = ' = 0' # заменяем последний '+' на '= 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x ')

ratio = look_ratio(k)
poly_one = look_polynomial(k, ratio)
print(f'первый искомый многочлен --> {poly_one}')
print()

with open('Polynomial_one.txt', 'w') as data:
    data.write(poly_one)

k = randint(2, 5)

ratio = look_ratio(k)
poly_two = look_polynomial(k, ratio)
print(f'второй искомый многочлен --> {poly_two}')
print()

with open('Polynomial_two.txt', 'w') as data:
    data.write(poly_two)