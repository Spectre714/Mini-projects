# ШИФР ЦЕЗАРЯ

upper_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lower_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
upper_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_en = 'abcdefghijklmnopqrstuvwxyz'

def caesar():
    r = ''
    if lan == 'ru':
        if method == 'encr':
            for i in range(len(text)):
                if text[i].isalpha() and text[i] in lower_ru:
                    r += lower_ru[(lower_ru.find(text[i]) + k) % 32]
                elif text[i].isalpha() and text[i] in upper_ru:
                    r += upper_ru[(upper_ru.find(text[i]) + k) % 32]
                else:
                    r += text[i]
            return r
        elif method == 'decr':
            for i in range(len(text)):
                if text[i].isalpha() and text[i] in lower_ru:
                    r += lower_ru[(lower_ru.find(text[i]) - k) % 32]
                elif text[i].isalpha() and text[i] in upper_ru:
                    r += upper_ru[(upper_ru.find(text[i]) - k) % 32]
                else:
                    r += text[i]
            return r
    elif lan == 'en':
        if method == 'encr':
            for i in range(len(text)):
                if text[i].isalpha() and text[i] in lower_en:
                    r += lower_en[(lower_en.find(text[i]) + k) % 26]
                elif text[i].isalpha() and text[i] in upper_en:
                    r += upper_en[(upper_en.find(text[i]) + k) % 26]
                else:
                    r += text[i]
            return r
        elif method == 'decr':
            for i in range(len(text)):
                if text[i].isalpha() and text[i] in lower_en:
                    r += lower_en[(lower_en.find(text[i]) - k) % 26]
                elif text[i].isalpha() and text[i] in upper_en:
                    r += upper_en[(upper_en.find(text[i]) - k) % 26]
                else:
                    r += text[i]
            return r
    
method = input(
    'Выберите, какую операцию вы хотите совершить с текстом? (''encr'' - шифрование, ''decr'' - дешифрование) ')
lan = input('Выберите язык (''ru'' - русский, ''en'' - английский) ')
k = int(input('Введите шаг сдвига: '))
text = input('Введите ваш текст: ')
print(caesar())