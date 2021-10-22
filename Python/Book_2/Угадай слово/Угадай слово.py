from tkinter import *
from random import randint

# ищет сколько букв совпало
def compareWord(s1, s2):
# возвращаемая переменная
    res = 0
# проверяет посимвольно старое и новые слова
    for i in range(len(s1)):
# если символы разные (есть совпадения), += 1
        if (s1[i] != s2[i]):
            res += 1
    return res

# заменяет найденные буквы в слове со звездочками
def getWordStar(ch):
    ret = ''
# сравниваем нажатую букву с буквой в слове
    for i in range(len(wordComp)):
# если совпала, записываем в ret символ
        if (ch == wordComp[i]):
            ret += ch
# если не совпала, записываем звездочку
        else:
            ret += wordStar[i]
# возвращаем новую строку
    return ret

# обрабатывает нажатия на кнопки
def pressLetter(n):
# global означает, что переменную можно изменять из метода
    global wordStar
# после нажатия на кнопку она блокируется
    btn[n]['text'] = '.'
    btn[n]['state'] = 'disabled'
# временная переменная
    oldWordStar = wordStar
# получаем строку с открытыми символами
    wordStar = getWordStar(chr(st + n))
# находим различие между старым и новым словом oldWordStar и wordStar
    count = compareWord(wordStar, oldWordStar)
# обновляем виджет с загаданным словом
    wordLabel['text'] = wordStar

# старт нового раунда
def startNewRound():
    global wordStar, wordComp

    # загадываем слово
    wordComp = 'ИНТЕРНЕТ'
    # Формируем строку из *
    wordStar = '*' * len(wordComp)
    # Устанавливаем текст в метку wordLabel
    wordLabel['text'] = wordStar
    # размещаем метку wordLabel по центру экрана
    wordLabel.place(x = WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y = 50)
    '''
    for i in range(32):
        btn[i]['text'] = f'{chr(st+i)}'
        btn[i]['state'] = 'normal'
    '''

# создание окна
root = Tk()
root.resizable(False, False)
root.title('Угадай слово')

# размещение окна по центу экрана и задание параметров размера окна
WIDTH = 810     # ширина
HEIGHT = 320    # высота

SCR_WIDTH = root.winfo_screenwidth()    # ширина экрана
SCR_HEIGHT = root.winfo_screenheight()  # высота экрана

POS_X = SCR_WIDTH // 2 - WIDTH // 2     # поправка относительно центра
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2   # поправка относительно центра

root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}') # ширина х высота + смещение по Х + смещение по У

# размещение виджетов
################################################################################

# загаданное слово
wordLabel = Label(font='consolas 15')
# отображение очков
scoreLabel = Label(font=', 12')
scoreLabel.place(x = 10, y = 165)
# топ очков
topScoreLabel = Label(font=', 12')
topScoreLabel.place(x = 10, y = 190)
# оставшиеся ПОПЫТки
userTryLabel = Label(font=', 12')
userTryLabel.place(x = 10, y = 215)

# очки
score = 0
# топ очков
topScore = 1000
# количество попыток
userTry = 10 # добавить 3 редима игры, от которых зависит количество попыток и очки, при кгадывании буквы
# стартовый символ
st = ord('А')
# список с кнопками
btn = []
# заполнение списка кнопками
for i in range(32): # 32 потому что без Ё
    btn.append(Button(text=chr(st+i), width=2, font='consolas 15'))
    btn[i].place(x = 215 + i % 11 * 35, y = 150 + i // 11 * 50)
    btn[i]['command'] = lambda x = i: pressLetter(x)

# загаданное слово
wordComp = ''
# вместо слова звездочки
wordStar = ''
# старт нового раунда
startNewRound()

root.mainloop()
