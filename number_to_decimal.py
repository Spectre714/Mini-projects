# ПЕРЕВОД ЧИСЛА В 10-УЮ СИСТЕМУ СЧИСЛЕНИЯ

d = input('Введите ваше число: ')
p = int(input('Введите основание системы счисления: '))
l = 'ABCDEF'
answer = 0
for i in range(len(d)):
    if d[i] in l:
        answer += (l.find(d[i]) + 10) * (p ** (len(d) - 1 - i))
    else:
        answer += int(d[i]) * (p ** (len(d) - 1 - i))
print(f'Ваше число в {p}-ой системе счисления: {answer}')