from tkinter import *
from random import randint

# обрабатывает нажатия на кнопки
def pressLatter(x):
    print(f'Нажата буква {chr(st + x)}.')

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
wordLabel = Label(text='TEST', font='consolas 15', bg='red')
wordLabel.place(x = 290,y = 100)
# отображение очков
scoreLabel = Label(text='TEST', font=', 12')
scoreLabel.place(x = 10, y = 165)
# топ очков
topScoreLabel = Label(text='TEST', font=', 12')
topScoreLabel.place(x = 10, y = 190)
# оставшиеся ПОПЫТки
userTryLabel = Label(text='TEST', font=', 12')
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
    btn[i]['command'] = lambda x = i: pressLatter(x)


root.mainloop()
