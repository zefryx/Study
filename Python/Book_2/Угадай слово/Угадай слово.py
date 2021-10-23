from tkinter import *
from tkinter import messagebox
from random import randint

# обработчик нажатий на клавиши
def pressKey(event):
    # переменную можно изменять
    global cheat
    # воод чита
    if (event.keycode in (50, 49, 53)):
        cheat += str(event.keycode)
    else:
        # если нажаты не символы чита, переменная обнуляется
        cheat = ''

    # если чит введен правильно - открывает слово
    if (cheat == '50494953'):
        wordLabel['text'] = wordComp
    # если чит введен правильно - скрывает слово
    elif (cheat == '53494950'):
        wordLabel['text'] = wordStar

    # получаем нажатый символ
    ch = event.char.upper()
    # отсеиваем нажатые клавиши типа Ctrl, Shift, Alt
    if (len(ch) == 0):
        return 0
    # получаем порядковый номер нажатой клавиши в алфавите
    codeBtn = ord(ch) - st
    # если номер буквы лежит в пределах - вызываем метода
    if (0 <= codeBtn <= 32):
        pressLetter(codeBtn)

# обновление информации на экране
def updateInfo():
    scoreLabel['text'] = f'Ваши очки: {score}'
    topScoreLabel['text'] = f'Рекорд: {topScore}'
    userTryLabel['text'] = f'Осталось попыток: {userTry}'

# сохраняем рекорд в файл
def saveTopScore():
    # глобал для того, что бы изменить значение в лейбле
    global topScore
    # присваиваем топу значение набранных очков
    topScore = score
    # блок обработки ошибок при работе с файлами
    try:
        # открывает файл, если его нет - создает
        f = open('record.dat', 'w', encoding='utf-8')
        f.write(str(topScore))
        f.close()
    # если возникла проблема при записи
    except:
        messagebox.showinfo('Ошибка!',
                            'Возникла проблема при сохранении файла.')

# загружает рекорд из файла
def getTopScore():
    # блок проверки на наличие файла
    try:
        f = open('record.dat', 'r', encoding='utf-8')
        m = int(f.readline())
        f.close()
    # если файла нет - рекорд обнуляется
    except:
        m = 0
    return m

# получение слов из словаря
def getWordsFromFile():
    # переменная для возвращаемого результата
    ret = []

    # блок проверки ошибок, если словарь удален
    try:
        # получаем данные из файла
        f = open('words.txt', 'r', encoding='utf-8')
        # читаем построчно
        for l in f.readlines():
            # удаляем символ переноса строки
            l = l.replace('\n', '')
            # добавляем в переменную слово, upper делает все символы в слове большими буквами, для удобства
            ret.append(l.upper())
        # закрываем файл
        f.close()
    # если словаря нет
    except:
        messagebox.showinfo('Ошибка!','Файл словаря не найден. \nРабота программы закончена.')
        # прекращение работы программы
        quit(0)
    # возвращаем выбранное слово
    return ret

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
    global wordStar, score, userTry
    # проверка, нажата ли одна и та же клавиша несколько раз, если да, то выполнение прерывается
    if (btn[n]['text'] == '.'):
        return 0
    # после нажатия на кнопку она блокируется
    btn[n]['text'] = '.'
    btn[n]['state'] = 'disabled'
    # временная переменная
    oldWordStar = wordStar
    # получаем строку с открытыми символами
    wordStar = getWordStar(chr(st + n))
    # находим различие между старым и новым словом oldWordStar и wordStar (сколько букв в слове угадал)
    count = compareWord(wordStar, oldWordStar)
    # обновляем виджет с загаданным словом
    wordLabel['text'] = wordStar
    # считаем очки
    if (count > 0):
        # если угадал - увеличиваем
        score += count * 11 - count ** 2
    else:
        # не угадал - уменьшаем
        score -= 10
        # если меньше нуля - ноль
        if (score < 0):
            score = 0
        # уменьшаем количество попыток
        userTry -= 1
    # обновляем информацию на экране
    updateInfo()

    # сравниваем загаданное слово с getWordStar
    if (wordStar == wordComp):
        # увеличиваем полученные очки на 50%
        score += score // 2
        # обновляем окно
        updateInfo()
        # сохраняем очки в файл (обновляем рекорд)
        if (score > topScore):
            # если рекорд обновлен
            messagebox.showinfo('Поздравляю!',
                               f'Вы установили новый рекорд! Угадано слово - {wordComp}. \
Набрано очков - {score}. Нажмите OK для продолжения игры.')
            saveTopScore()
        else:
            # если рекорд не обновлен
            messagebox.showinfo('Отлично!',
                               f'Вы молодец! Угадано слово - {wordComp}. \
Набрано очков - {score}. Нажмите OK для продолжения игры.')
        # запускаем новый раунд
        startNewRound()
    # если закончилось количество попыток
    elif (userTry <= 0):
        messagebox.showinfo('Проигрыш', 'У Вас не осталось попыток. Игра окончена.')
        quit(0)

# старт нового раунда
def startNewRound():
    global wordStar, wordComp, userTry
    # проверка, остались ли еще слова в словаре. Если нет - выход из программы
    if (len(dictionary) == 0):
        messagebox.showinfo('Ого!', 'Кажется вы разгадали все слова!\
Ждем Вас снова после обновления программы.')
        quit(0)
    # устанавливаем количество попыток
    userTry = 10
    # компьютер выбирает случайное слово из словаря
    wordComp = dictionary[randint(0, len(dictionary) - 1)]
    # удаление загаданного слова из словаря
    dictionary.remove(wordComp)
    # Формируем строку из *
    wordStar = '*' * len(wordComp)
    # Устанавливаем текст в метку wordLabel
    wordLabel['text'] = wordStar
    # размещаем метку wordLabel по центру экрана
    wordLabel.place(x = WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y = 50)
    # обновляем информацию на экране
    updateInfo()

    # возвращаем кнопки к нормальному виду
    for i in range(32):
        btn[i]['text'] = f'{chr(st+i)}'
        btn[i]['state'] = 'normal'

# создание окна
root = Tk()
root.resizable(False, False)
root.title('Угадай слово')
root.bind('<Key>', pressKey)

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
topScore = getTopScore()
# количество попыток
userTry = 0 # добавить 3 редима игры, от которых зависит количество попыток и очки, при кгадывании буквы
# стартовый символ
st = ord('А')
# список с кнопками
btn = []
# заполнение списка кнопками
for i in range(32): # 32 потому что без Ё
    btn.append(Button(text=chr(st+i), width=2, font='consolas 15'))
    btn[i].place(x = 215 + i % 11 * 35, y = 150 + i // 11 * 50)
    btn[i]['command'] = lambda x = i: pressLetter(x)

# чит, для отображения загаданного словар
cheat = ''
# загаданное слово
wordComp = ''
# вместо слова звездочки
wordStar = ''
# словарь
dictionary = getWordsFromFile()
# старт нового раунда
startNewRound()

root.mainloop()
