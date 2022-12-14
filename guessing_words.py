"""УГАДАЙКА СЛОВ"""

import random as rnd
word_list = ['Машина', 'Телефон', 'Конструктор', 'Программирование', 'Бизнес', 'Сок', 'Птица',
'Молоко', 'Теннис', 'Галактика', 'Шифр', 'Государство', 'Ножницы', 'Муляж',
'Погода', 'Велосипед', 'Инструмент', 'Пещера', 'Убежище',
'Собака', 'Факториал', 'Зонд', 'Муравей', 'Планшет', 'Лента', 'Нравственность', 'Одеяло', 'Огород', 'Усадьба', 'Редактор', 'Самолет', 'Проводник',
'Частица', 'Пружина', 'Тигр', 'Скалка', 'Баскетбол', 'Новелла', 'Астрология', 'Ночник']

# функция получения рандомного слова
def get_word():
    return rnd.choice(word_list).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


# сама игра
def play(word):
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = ['_'] * len(word)
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('Я хочу сыграть с тобой в игру...\n')
    print(display_hangman(tries))
    print(*word_completion)

    while tries > 0:
        char = input('Назови букву или слово целиком: ').upper()
        if not char.isalpha():
            print('Введите ИМЕННО букву или слово')
            continue
        if char in guessed_letters:
            print(f'Буква {char} уже была')
            continue
        if char in guessed_words:
            print(f'Слово {char} уже было')
            continue        
        if char in word:
            if len(char) == 1:
                guessed_letters.append(char)
                print('Да, такая буква в слове имеется')
                for i in range(len(word)):
                    if word[i] == char:
                        word_completion[i] = char
                print(*word_completion)
                if ''.join(word_completion) == word:
                    guessed = True
                    break
                else:
                    continue
            else:
                guessed = True
                break
        if char not in word:
            if len(char) == 1:
                guessed_letters.append(char)
                print('Такой буквы в слове нет')
                tries -= 1
                print(display_hangman(tries))
                print(*word_completion)
                continue
            else:
                guessed_words.append(char)
                print('Неверный ответ')
                tries -= 1
                print(display_hangman(tries))
                print(*word_completion)
                continue                

    if guessed is False:
        print('Ты истратил все имеющиеся попытки, игра окончена!\n')
        print(display_hangman(tries))
        print(f'Правильное слово - {word}')
    else:
        print('Поздравляю, ты угадал слово! Игра окончена.')

while True:
    print('Ну здравствуй ^^\n')
    k = get_word()
    play(k)
    answer = input('\nЖелаешь сыграть еще??? (y/n)\n')
    if answer.lower() == 'y':
        continue
    else:
        print('Ну как знаешь. See ya around, kid!')
        break