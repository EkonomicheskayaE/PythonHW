# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

def unique(my_list):
    list = [i for i in my_list if my_list.count(i) <= 1]
    return list
print(my_list)
print(unique(my_list))
print()

# Найти сумму чисел списка стоящих на нечетной позиции.
# from functools import reduce
from functools import reduce

data = list(map(int, input('Введите числа через пробел --> ').split()))
print(data)

res = list(filter(lambda i: i in range(len(data)) if i % 2 == 0 else i + 0, data))
result = reduce(lambda x, y: x + y, res)

print(res)
print(result)
print()

# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.

# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def get_dict(n):
    return {x: 3 * x + 1 for x in range(1, n + 1)}

n = int(input('Введите натуральное число n --> '))

print(n)
print(get_dict(n))