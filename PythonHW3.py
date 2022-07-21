# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

sum_list = [2, 3, 5, 9, 3]
sum = 0
for i in range(len(sum_list)):
    if i%2 != 0:
        sum += sum_list[i]
        i += 2
print(sum)
print()

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]

def composition(numbers):
    result = []
    while len(numbers) > 1:
        result.append(numbers[0]*numbers[-1])
        del numbers[0]
        del numbers[-1]
    if len(numbers) == 1:
        result.append(numbers[0]**2)
    return result
print(composition(my_list))
print()

# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

diff_list = [1.1, 1.2, 3.1, 5, 10.01]

def find_diff(list):
    need_diff = [round(i - int(i), 2) for i in list]
    need_diff = [i for i in need_diff if type(i) == float]
    return max(need_diff) - min(need_diff)
print(find_diff(diff_list))
print()

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число --> '))

def convert_number(n):
    drob = ''
    while n > 0:
        drob += str(n%2)
        n = n//2
    return drob
print(convert_number(n))
print()

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число --> '))
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(n))

def fibonacci2(n):
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a, b = b, a + b*-1
newdata = list(fibonacci2(n))
new_data = list(reversed(newdata))
combo_list = new_data + data
print(combo_list)