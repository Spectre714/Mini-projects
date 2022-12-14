# ГЕНЕРАТОР БЕЗОПАСНЫХ ПАРОЛЕЙ

import random as rnd
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

amount = int(input('Укажите количество паролей для генерации: '))
length = int(input('Укажите длину одного пароля: '))
dig_in = input('Включать ли цифры от 0 до 9? (y/n) ')
ABC_in = input('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? (y/n) ')
abc_in = input('Включать ли строчные буквы "abcdefghijklmnopqrstuvwxyz"? (y/n) ')
symb_in = input('Включать ли символы "!#$%&*+-=?@^_?" (y/n) ')
symb_out = input('Исключать ли неоднозначные символы "il1Lo0O"? (y/n) ')

if dig_in.lower() == 'y':
    chars += digits
if ABC_in.lower() == 'y':
    chars += uppercase_letters
if abc_in.lower() == 'y':
    chars += lowercase_letters
if symb_in.lower() == 'y':
    chars += punctuation
if symb_out.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    for i in range(amount):
        print(*(rnd.sample(chars, length)), sep='')

print(f'\nСгенерированы следующие {amount} паролей:\n')
generate_password(length, chars)