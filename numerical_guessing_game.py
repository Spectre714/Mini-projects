# ЧИСЛОВАЯ УГАДАЙКА

from random import *

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= right

def input_num():
    while True:
        n = input(f'Введите число от 1 до {right}: ')
        if is_valid(n):
            return int(n)
        else:
            print(f'А может быть все - таки введем целое число от 1 до {right}?')

def compare_num():
    s = randint(1, right)
    counter = 0
    while True:
        n = input_num()
        counter += 1
        if n < s:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > s:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n == s:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', counter)
            break

def new_game():
    answer = input('Хотите начать новую игру? (Да/Нет) ')
    if answer.lower() == 'да':
        game()
    elif answer.lower() == 'нет':
        print('Спасибо, что играли в числовую угадайку! Еще увидимся...')

def game():
    print('Добро пожаловать в числовую угадайку!')
    global right
    right = int(input('Укажите правую границу для случайного выбора числа, большую 1: '))
    compare_num()
    new_game()

game()