from tkinter import *  # импорт библиотеки tkinter
from tkinter import messagebox
from tkinter import ttk
from random import randint


# загрузка денег
def loadMoney():
    try:
        f = open('money.dat', 'r')
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        insertText(
            f'Добро пожаловать на ипподром! Вы у нас впервые? Тогда в качестве приветственного бонуса вручаем Вам {defaultMoney} {valuta}\n')
        m = defaultMoney
    return m

# сохранение денег
def saveMoney(moneyToSave):
    try:
        f = open('money.dat', 'w')
        f.write(str(moneyToSave))
        f.close()
    except:
        messagebox.showinfo('АЛЯРМА!', 'Книга учета потеряна! Ипподром временно закрывается! Прощайте...')
        quit(0)

# отрисовка лошадей на экране
def horsePlaceInWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)

# добавление строки S в информационный чат
def insertText(s):
    textDiary.insert(INSERT, s + '\n')
    textDiary.see(END)

# формирует список возможных ставок
def getValues(summa):
    value = []

    if (summa > 9):
        for i in range(11):
            value.append(i * (int(summa) // 10))
    else:
        value.append(0)
        if (summa > 0):
            value.append(summa)

    return value

# обновляет содеримое выпадающего списка, для выбора ставки
def refreshCombo(eventObject):
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    labelAllMoney['text'] = f'Осталось средств: {int(money - summ)} {valuta}'

    if (summ > 0):
        startButton['state'] = 'normal'
    else:
        startButton['state'] = 'disabled'

    # ставки загруженные в списки
    stavka01['values'] = getValues(int(money - summ02.get() - summ03.get() - summ04.get()))
    stavka02['values'] = getValues(int(money - summ01.get() - summ03.get() - summ04.get()))
    stavka03['values'] = getValues(int(money - summ01.get() - summ02.get() - summ04.get()))
    stavka04['values'] = getValues(int(money - summ01.get() - summ02.get() - summ03.get()))
    # активирует чекбоксы, если сделана ставка
    if (summ01.get() > 0):
        horse01Game.set(True)
    else:
        horse01Game.set(False)
    if (summ02.get() > 0):
        horse02Game.set(True)
    else:
        horse02Game.set(False)
    if (summ03.get() > 0):
        horse03Game.set(True)
    else:
        horse03Game.set(False)
    if (summ04.get() > 0):
        horse04Game.set(True)
    else:
        horse04Game.set(False)

# состояние конкретной лошади + коэфф.ставки на неё
def getHealth(name, state, win):
    s = f'Лошадь {name} '
    if (state == 5):
        s += 'плохо себя чувствует...'
    elif (state == 4):
        s += 'плохо спала, выглядит вялой.'
    elif (state == 3):
        s += 'выглядит не очень бодрой, но ведет себя хорошо.'
    elif (state == 2):
        s += 'в хорошем настроении, сытая и начесаная.'
    elif (state == 1):
        s += 'чувствует себя просто отлично!'

    s += f' ({win})'
    return s

# показывает информацию о погоде в чате
def viewWeather():
    s = 'Сейчас на ипподроме '
    if (weather == 1):
        s += 'ночь, '
    elif (weather == 2):
        s += 'утро, '
    elif (weather == 3):
        s += 'день, '
    elif (weather == 4):
        s += 'вечер, '

    if (timeDay == 1):
        s += 'льет сильный дожь, гремит гром и бьют молнии.'
    elif (timeDay == 2):
        s += 'идет дожь.'
    elif (timeDay == 3):
        s += 'облачно, порывистый ветер, на горизонте тучи.'
    elif (timeDay == 4):
        s += 'безоблачно, ветер.'
    elif (timeDay == 5):
        s += 'прекрасная погода.'

    insertText(s)

# внештатные ситуации с лошадьми
def problemHorse():
    global reverse01, reverse02, reverse03, reverse04, play01, play02, play03, play04, boost01, boost02, boost03, boost04

    horse = randint(1, 4)  # с какой лошадью произойдет проблема

    maxRand = 10000

    if (horse == 1 and play01 == True and x01 > 0):
        if (randint(0, maxRand) < state01 * 5):
            reverse01 = not reverse01  # если уж так произошло, что лошадь захотела бежать обратно
            messagebox.showinfo('АЛЯРМА',
                                f'Лошадка {nameHorse01} вспомнила, что не выключила утюг, и побежала обратно!')
        elif (randint(0, maxRand) < state01 * 5):
            play01 = False  # если уж так произошло, что лошадь захотела скинуть жокея
            messagebox.showinfo('Никогда такого не было, и вот опять!',
                                f'Наездник не справился с лошадью. {nameHorse01} скинул его с седла и остановился!')
        elif (randint(0, maxRand) < state01 * 5 and not boost01):  # ускорение лошади
            messagebox.showinfo('Воу воу!', f'Коняшку {nameHorse01} будто ужалила пчела! Он понесся быстрее ветра!')
            boost01 = True
    if (horse == 2 and play02 == True and x02 > 0):
        if (randint(0, maxRand) < state02 * 5):
            reverse02 = not reverse02
            messagebox.showinfo('АЛЯРМА',
                                f'Лошадка {nameHorse02} вспомнила, что не выключила утюг, и побежала обратно!')
        elif (randint(0, maxRand) < state02 * 5):
            play02 = False
            messagebox.showinfo('Никогда такого не было, и вот опять!',
                                f'Наездник не справился с лошадью. {nameHorse02} скинул его с седла и остановился!')
        elif (randint(0, maxRand) < state02 * 5 and not boost02):
            messagebox.showinfo('Воу воу!', f'Коняшку {nameHorse02} будто ужалила пчела! Он понесся быстрее ветра!')
            boost02 = True
    if (horse == 3 and play03 == True and x03 > 0):
        if (randint(0, maxRand) < state03 * 5):
            reverse03 = not reverse03
            messagebox.showinfo('АЛЯРМА',
                                f'Лошадка {nameHorse03} вспомнила, что не выключила утюг, и побежала обратно!')
        elif (randint(0, maxRand) < state03 * 5):
            play03 = False
            messagebox.showinfo('Никогда такого не было, и вот опять!',
                                f'Наездник не справился с лошадью. {nameHorse03} скинул его с седла и остановился!')
        elif (randint(0, maxRand) < state03 * 5 and not boost03):
            messagebox.showinfo('Воу воу!', f'Коняшку {nameHorse03} будто ужалила пчела! Он понесся быстрее ветра!')
            boost03 = True
    if (horse == 4 and play04 == True and x04 > 0):
        if (randint(0, maxRand) < state04 * 5):
            reverse04 = not reverse04
            messagebox.showinfo('АЛЯРМА',
                                f'Лошадка {nameHorse04} вспомнила, что не выключила утюг, и побежала обратно!')
        elif (randint(0, maxRand) < state04 * 5):
            play04 = False
            messagebox.showinfo('Никогда такого не было, и вот опять!',
                                f'Наездник не справился с лошадью. {nameHorse04} скинула его с седла и остановилась!')
        elif (randint(0, maxRand) < state04 * 5 and not boost04):
            messagebox.showinfo('Воу воу!', f'Коняшку {nameHorse04} будто ужалила пчела! Она понеслась быстрее ветра!')
            boost04 = True

# главный цикл игры
def moveHorse():
    global x01, x02, x03, x04

    if (randint(0, 100) < 20):  # вызов проблем лошадок
        problemHorse()

    speed01 = (randint(1, timeDay + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)  # расчет скорости
    speed02 = (randint(1, timeDay + weather) + randint(1, int((7 - state02)) * 3)) / randint(10, 175)
    speed03 = (randint(1, timeDay + weather) + randint(1, int((7 - state03)) * 3)) / randint(10, 175)
    speed04 = (randint(1, timeDay + weather) + randint(1, int((7 - state04)) * 3)) / randint(10, 175)

    multiple = 3  # величина ускорение
    speed01 *= int(randint(1, 2 + state01) * (1 + boost01 * multiple))
    speed02 *= int(randint(1, 2 + state02) * (1 + boost02 * multiple))
    speed03 *= int(randint(1, 2 + state03) * (1 + boost03 * multiple))
    speed04 *= int(randint(1, 2 + state04) * (1 + boost04 * multiple))

    if (play01):  # если лошади бегут
        if (not reverse01):  # вперед
            x01 += speed01
        else:  # назад
            x01 -= speed01
    if (play02):
        if (not reverse02):
            x02 += speed02
        else:
            x02 -= speed02
    if (play03):
        if (not reverse03):
            x03 += speed03
        else:
            x03 -= speed03
    if (play04):
        if (not reverse04):
            x04 += speed04
        else:
            x04 -= speed04

    horsePlaceInWindow()
    if (x01 < 952 and x02 < 952 and x03 < 952 and x04 < 952):
        root.after(5, moveHorse)
    else:
        if(x01 >= 952):
            winRound(1)
        elif(x02 >= 952):
            winRound(2)
        elif(x03 >= 952):
            winRound(3)
        elif(x04 >= 952):
            winRound(4)

    allPlay = play01 or play02 or play03 or play04
    allX = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0
    allReverse = reverse01 and reverse02 and reverse03 and reverse04

    if (not allPlay or allX or allReverse):
        winRound(0)
        return 0

# после нажатия на кнопку СТАРТ
def runHorse():
    global money

    startButton['state'] = 'disabled'
    stavka01['state'] = 'disabled'
    stavka02['state'] = 'disabled'
    stavka03['state'] = 'disabled'
    stavka04['state'] = 'disabled'
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()

    moveHorse()

# показывает состояние лошадей в чате
def healthHorse():
    insertText(getHealth(nameHorse01, state01, winCoeff01))
    insertText(getHealth(nameHorse02, state02, winCoeff02))
    insertText(getHealth(nameHorse03, state03, winCoeff03))
    insertText(getHealth(nameHorse04, state04, winCoeff04))

#победа одной из лошадей
def winRound(horse):
    global x01, x02, x03, x04, money

    res = 'К финишу пришла лошадь '
    if (horse == 1):
        res += nameHorse01
        win = summ01.get() * winCoeff01
    elif (horse == 2):
        res += nameHorse02
        win = summ02.get() * winCoeff02
    elif (horse == 3):
        res += nameHorse03
        win = summ03.get() * winCoeff03
    elif (horse == 4):
        res += nameHorse04
        win = summ04.get() * winCoeff04

    if (horse > 0):
        res += f'! Вы выйграли {int(win)} {valuta}. '
        if (win > 0):
            res += 'Поздравляем! Средства уже зачислены на ваш счет.'
            insertText(f'Этот забег принес Вам {int(win)} {valuta}.')
        else:
            res += 'К сожалению Ваша лошадь была неправильной. Попробуйте еще раз!'
            insertText('Делайте ставки! Увеличивайте прибыль!')
        messagebox.showinfo('Результат', res)
    else:
        messagebox.showinfo('Все плохо', 'До финиша не дошел никто. Забег признан несостоявшимся. Все ставки возвращены.')
        insertText('Забег признан несостоявшимся.')
        win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

    money += win
    saveMoney(int(money))

    setupHorse()

    # Сбрасываем виджетыы
    startButton['state'] = 'normal'
    stavka01['state'] = 'readonly'
    stavka02['state'] = 'readonly'
    stavka03['state'] = 'readonly'
    stavka04['state'] = 'readonly'
    stavka01.current(0)
    stavka02.current(0)
    stavka03.current(0)
    stavka04.current(0)

    # Сбрасываем лошадок
    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20
    horsePlaceInWindow()

    # Обновляем интерфейс
    refreshCombo(eventObject='')
    viewWeather()
    healthHorse()
    insertText(f'Ваши средства: {int(money)} {valuta}')

    if (money < 1):
        messagebox.showinfo('Стоп', 'На ипподром без денег заходить нельзя.')
        quit(0)

#установка состояния лошадей
def setupHorse():
    global state01, state02, state03, state04
    global weather, timeDay
    global winCoeff01, winCoeff02, winCoeff03, winCoeff04
    global play01, play02, play03, play04
    global reverse01, reverse02, reverse03, reverse04
    global boost01, boost02, boost03, boost04

    state01 = randint(1, 5)  # состояния лошадей, 1 - супер, 5 - очень плохо
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    weather = randint(1, 5)  # погода 1 - плохая, 5 - отличная
    timeDay = randint(1, 4)  # время суток 1 - вечер, 2- ночь и тд.

    winCoeff01 = int(100 + randint(state01 ** 3, 30 + state01 * 60)) / 100  # коэффициенты выйгрыша
    winCoeff02 = int(100 + randint(state02 ** 3, 30 + state02 * 60)) / 100
    winCoeff03 = int(100 + randint(state03 ** 3, 30 + state03 * 60)) / 100
    winCoeff04 = int(100 + randint(state04 ** 3, 30 + state04 * 60)) / 100

    reverse01 = False  # маркеры ситуаций
    reverse02 = False
    reverse03 = False
    reverse04 = False
    play01 = True
    play02 = True
    play03 = True
    play04 = True
    boost01 = False
    boost02 = False
    boost03 = False
    boost04 = False

###################
#                   тут будут переменные
###################

WIDTH = 1024  # размеры окна
HEIGHT = 600

x01 = 20  # стартовые позиции лошадей
x02 = 20
x03 = 20
x04 = 20

state01 = randint(1, 5)  # состояния лошадей, 1 - супер, 5 - очень плохо
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

winCoeff01 = int(100 + randint(state01 ** 3, 30 + state01 * 60)) / 100  # коэффициенты выйгрыша
winCoeff02 = int(100 + randint(state02 ** 3, 30 + state02 * 60)) / 100
winCoeff03 = int(100 + randint(state03 ** 3, 30 + state03 * 60)) / 100
winCoeff04 = int(100 + randint(state04 ** 3, 30 + state04 * 60)) / 100

reverse01 = False  # маркеры ситуаций
reverse02 = False
reverse03 = False
reverse04 = False
play01 = True
play02 = True
play03 = True
play04 = True
boost01 = False
boost02 = False
boost03 = False
boost04 = False

nameHorse01 = 'Фхтагнх'  # имена лошадок
nameHorse02 = 'Лейбниц'
nameHorse03 = 'Эдельвейс'
nameHorse04 = 'Звёздочка'

valuta = 'руб.'
money = 0
defaultMoney = 10000

weather = randint(1, 5)  # погода 1 - плохая, 5 - отличная
timeDay = randint(1, 4)  # время суток 1 - вечер, 2- ночь и тд.

###################
#                   тут будет все связанное с окном
###################

root = Tk()  # переменная, управляющая библиотекой tkinter

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2  # позиция координаты окна для размещения по центру экрана
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')  # установка окна
root.title('Ипподром')  # заголовок окна
root.resizable(False, False)  # запрет изменение размеров окна

# добавляем фон
road_image = PhotoImage(file='road.png')  # загружаем изображение
road = Label(root, image=road_image)  # помещаем его в переменную
road.place(x=0, y=17)  # задаем координаты

# добавляем лошадей поверх фона
horse01_image = PhotoImage(file='horse01.png')
horse01 = Label(root, image=horse01_image)

horse02_image = PhotoImage(file='horse02.png')
horse02 = Label(root, image=horse02_image)

horse03_image = PhotoImage(file='horse03.png')
horse03 = Label(root, image=horse03_image)

horse04_image = PhotoImage(file='horse04.png')
horse04 = Label(root, image=horse04_image)

horsePlaceInWindow()  # выводим лошадей на экран

# создаем кнопку
startButton = Button(text='СТАРТ', font='arial 20', width=64, background='#37AA37')
startButton.place(x=20, y=370)

startButton['state'] = 'disabled'
startButton['command'] = runHorse   #действие кнопки

# добавляем текстовое поле
textDiary = Text(width=77, height=10, wrap=WORD)
textDiary.place(x=450, y=450)

scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=451, height=133)
textDiary['yscrollcommand'] = scroll.set

# чекбоксы для лошадок
labelHorse01 = Label(text=f'Ставка на лошадь №1')  # текстовые поля
labelHorse01.place(x=20, y=450)

labelHorse02 = Label(text=f'Ставка на лошадь №2')
labelHorse02.place(x=20, y=480)

labelHorse03 = Label(text=f'Ставка на лошадь №3')
labelHorse03.place(x=20, y=510)

labelHorse04 = Label(text=f'Ставка на лошадь №4')
labelHorse04.place(x=20, y=540)

horse01Game = BooleanVar()  # чекбоксы с галочкой
horse01Game.set(0)
horse01Check = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horse01Check.place(x=150, y=448)
horse01Check['state'] = 'disabled'

horse02Game = BooleanVar()
horse02Game.set(0)
horse02Check = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horse02Check.place(x=150, y=478)
horse02Check['state'] = 'disabled'

horse03Game = BooleanVar()
horse03Game.set(0)
horse03Check = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horse03Check.place(x=150, y=508)
horse03Check['state'] = 'disabled'

horse04Game = BooleanVar()
horse04Game.set(0)
horse04Check = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horse04Check.place(x=150, y=538)
horse04Check['state'] = 'disabled'

# добавляем строку со счетом игрока
money = loadMoney()

if (money <= 0):
    messagebox.showinfo('АЛЯРМ!', 'Ваша казна опустела, милорд!')
    quit()

labelAllMoney = Label(text=f'Осталось средств: {money} {valuta}', font='Arial 12')
labelAllMoney.place(x=20, y=565)

# выпадающие списки со ставками
stavka01 = ttk.Combobox(root)
stavka01['state'] = 'readonly'  # только чтение
stavka01.place(x=280, y=450)

stavka02 = ttk.Combobox(root)
stavka02['state'] = 'readonly'
stavka02.place(x=280, y=480)

stavka03 = ttk.Combobox(root)
stavka03['state'] = 'readonly'
stavka03.place(x=280, y=510)

stavka04 = ttk.Combobox(root)
stavka04['state'] = 'readonly'
stavka04.place(x=280, y=540)

summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

stavka01['textvariable'] = summ01
stavka02['textvariable'] = summ02
stavka03['textvariable'] = summ03
stavka04['textvariable'] = summ04

stavka01.bind('<<ComboboxSelected>>', refreshCombo)
stavka02.bind('<<ComboboxSelected>>', refreshCombo)
stavka03.bind('<<ComboboxSelected>>', refreshCombo)
stavka04.bind('<<ComboboxSelected>>', refreshCombo)

refreshCombo('')

stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

viewWeather()  # информация о погоде
healthHorse()  # информация о состоянии лошадей

root.mainloop()  # запуск программы
