# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

proposal = 'Буквы а_б_в абв являются самозабвенным началом забвения зимбабвийского русского алфавита!'
word = proposal.split(' ') # делим предложение на слова
words = ' '.join(word)
print(f'Изначальное предложение:\n{words}\n')


combination = 'абв' # сочетание букв для удаление слов, в которых они содержатся
new_words = []
for i in word:
    if combination not in i:
        new_words.append(i)
new_proposal = ' '.join(new_words)
print(f'Предложение после удаления слов, соржащих сочетание букв абв:\n{new_proposal}')
print()


# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# 1. Игра человека против человека:

from random import randint

player1 = input('Как вас зовут? --> ')
player2 = input('Как вас зовут? --> ')
candys = int(input('Сколько всего у вас конфет для игры? --> '))
priority = randint(0, 2) # разыгрывается кто первый будет ходить

if priority:
    print(f'Первый ходит {player1}')
else:
    print(f'Первый ходит {player2}')

def take_how(quantity):  # функция описывает сколько кто возьмёт конфет
    x = int(input(f'{quantity}, сколько возьмёшь конфет (max можно взять 28)? --> '))
    while x < 1 or x > 28:
        x = int(input(f'{quantity}, такое количество брать нельзя! '))
    return x

def start_game(name, k, candys):
    print(f'{name} взял {k}, всего осталось {candys} конфет!')

while candys > 28:
    if priority:
        k = take_how(player1)
        candys -= k
        priority = False
        start_game(player1, k, candys)
    else:
        k = take_how(player2)
        candys -= k
        priority = True
        start_game(player2, k, candys)

if priority:
    print(f'Выиграл {player1}')
else:
    print(f'Выиграл {player2}')

print()

# Игра человека против Бота:

from random import randint

player1 = input('Как вас зовут? --> ')
player2 = 'Bot'
candys = int(input('Сколько всего у вас конфет для игры? --> '))
priority = randint(0, 2) # разыгрывается кто первый будет ходить

if priority:
    print(f'Первый ходит {player1}')
else:
    print(f'Первый ходит {player2}')

def take_how(quantity):  # функция описывает сколько кто возьмёт конфет
    x = int(input(f'{quantity}, сколько возьмёшь конфет (max можно взять 28)? --> '))
    while x < 1 or x > 28:
        x = int(input(f'{quantity}, такое количество брать нельзя! '))
    return x

def start_game(name, k, candys):
    print(f'{name} взял {k}, всего осталось {candys} конфет!')

while candys > 28:
    if priority:
        k = take_how(player1)
        candys -= k
        priority = False
        start_game(player1, k, candys)
    else:
        k = randint(1, 29)
        candys -= k
        priority = True
        start_game(player2, k, candys)

if priority:
    print(f'Выиграл {player1}')
else:
    print(f'Выиграл {player2}')

print()

# Создайте программу для игры в ""Крестики-нолики"".

n = list(range(1,10))

def draw_board(n):
    print ("-" * 13)
    for i in range(3):
        print ("|", n[0+i*3], "|", n[1+i*3], "|", n[2+i*3], "|")
        print ("-" * 13)

def enter_data(player_token):
    meaning = False
    while not meaning:
        answer_player = input(f'Куда поставишь {player_token}? --> ')
        try:
            answer_player = int(answer_player)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if answer_player >= 1 and answer_player <= 9:
            if (str(n[answer_player-1]) not in "XO"):
                n[answer_player-1] = player_token
                meaning = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректное значение. Введите число от 1 до 9 чтобы походить.")

def win_player(n):
    win_combination = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_combination:
        if n[i[0]] == n[i[1]] == n[i[2]]:
            return n[i[0]]
    return False

def result_main(n):
    counter = 0
    win = False
    while not win:
        draw_board(n)
        if counter % 2 == 0:
            enter_data('X')
        else:
            enter_data('O')
        counter += 1
        if counter > 4:
            full_win = win_player(n)
            if full_win:
                print (full_win, "ВЫИГРАЛ! УРА!")
                win = True
                break
        if counter == 9:
            print ("НИЧЬЯ!")
            break
    draw_board(n)
result_main(n)
print()

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('input_data.txt', 'w') as data:
    data.writelines('AAASSSSDDFFFFFGGGGGG')

with open('input_data.txt', 'r') as data:
    my_text1 = data.read()

def input_line(n):  # функция реализует модуль сжатия данных
    input_data = ''
    i = 0
    while i < len(n):  
        count = 1
        while i + 1 < len(n) and n[i] == n[i + 1]: 
            count += 1
            i += 1
        input_data += str(count) + n[i]
        i += 1
    return input_data

input_data = input_line(my_text1)
print(input_data)

with open('output_data.txt', 'w') as data:
    data.writelines('5A6S1D8F5G')

with open('output_data.txt', 'r') as data:
    my_text2 = data.read()

def output_line(x:str):     # функция реализует модуль восстановления данных
    k = ''
    output_data = ''
    for i in x:
        if i.isdigit():
            k += i
        else:
            output_data += i * int(k)
            k = ''
    return output_data

output_data = output_line(my_text2)
print(output_data)