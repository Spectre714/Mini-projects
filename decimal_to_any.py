# ПЕРЕВОД ДЕСЯТИЧНОГО ЧИСЛА В ЛЮБУЮ ДРУГУЮ СС

numbers = [10, 11, 12, 13, 14, 15]
chars = 'ABCDEF'

def osn(n, base):
    r = ''
    while n >= base:
        x = n % base
        if x in numbers:
            r += chars[x - 10]
        else:
            r += str(x)
        n = n // base
    if n in numbers:
        r += chars[n - 10]
    else:
        r += str(n)
    print(r[::-1])

d = int(input('Ваше число в десятичной системе счисления: '))
b = int(input('Укажите, в какую систему счисления хотите перевести число: '))
osn(d, b)