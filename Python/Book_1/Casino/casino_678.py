'''Казино 678
28.09.2020'''
#первые 10-20 запусков программа обращается на Вы, а потом на Ты
#при победе - на Вы, при поражении - на Ты, при проигрыше всех денег - по гоповски

import random   #рандомные числа
import time
import os       #команды системы
from ctypes import *   #форматирование текста в консоли

#windll.Kernel32.GetStdHandle.restype = c_ulong  #этот код нужен, что бы в командной строке Win можно было менять цвет текста
#h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

#используемые переменные в коде
valuta = 'руб.'         #валюта
money = 0               #остаток денег в кошельке
startMoney = 0          #сумма, с которой игрок начал играть в этот раз
defaultMoney = 10000    #стандартное количество стартовых денег
playGame = True         #играем или нет

result = 0              #выйгранные или проигранные деньги
stavka = 0              #ставка

#вывод приветственной шапки
def colorLine(c, s):
    os.system('clear')                #очистка экрана командной строки
    color(c)
    print('*' * (len(s) + 2))         #len() возвращает длину строки в символах
    print(' ' + s)
    print('*' * (len(s) + 2))

#функция выбора игры
def getInput(digit, message):
    color(7)
    ret = ''
    while(ret == '' or not ret in digit):
        ret = input(message)
    return ret

#функия ввода ставки и приветствие в конкретной игре
def getIntInput(minimum, maximum, message):
    color(7)
    ret = -1
    while(ret < minimum or ret > maximum):
        st = input(message)
        if(st.isdigit()):
            ret = int(st)
        else:
            print('    Введите целое число!')
    return ret

#победа
def vin(result):
    color(14)
    print(f'\n    Хорошо, Вы победили. Ваш выйгрыш: {result} {valuta}')
    print(f'    У Вас на счету {money} {valuta}')

#поражение
def defeat(result):
    color(12)
    print(f'\n    Хммм, ты проиграл. Твой проигрыш: {result} {valuta}')
    print(f'    У тебя на счету {money} {valuta}')
    print('    Отыграешься? Если конечно не ссылко.')

#загрузка денег из файла
def loadMoney():
    try:
        f = open('money.dat', 'r')
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f'Наша казино впервые открывает свои двери для игроков! В качестве приветственного бонуса вручаем каждому игроку {defaultMoney} {valuta}')
        m = defaultMoney
    return m

#сохранение денег в файле
def saveMoney(moneyToSave):
    try:
        f = open('money.dat', 'w')
        f.write(str(moneyToSave))
        f.close()
    except:
        print('Книга учета потеряна! Казино временно закрывается! Прощайте.')
        quit(0)

#изменение цвета текста
def color(c):
#    windll.Kernel32.SetConsoleTextAttribute(h, c)
    pass
#анимация рулетки
def getRoulette(visible):
    tickTime = random.randint (100, 200) / 10000    #время на которое увеличится пауза
    mainTime = 0    #время паузы
    number = random.randint(0, 38)  #число, выпавшее на рулетке
    increaseTickTime = random.randint(100, 110) / 100   #время, на которое увеличивается TickTime
    col = 1 #цвет сообщения

    while(mainTime < 0.7):
        col += 1    #выбор цвета сообщения
        if(col > 15):
            col = 1

        mainTime += tickTime    #увеличение времени
        tickTime *= increaseTickTime

        color(col)
        number += 1
        if(number > 38):
            number = 0
            print()

        printNumber = number    #дабл/трипл зеро
        if(number == 37):
            printNumber = '00'
        elif(number == 38):
            printNumber = '000'

        print(' Число >',
              printNumber,
              '*' * number,
              ' ' * (79 - number * 2),
              '*' * number)

        if(visible):        #пауза
            time.sleep(mainTime)

    return number

#функция Рулетки
def roulette():
    global money
    playGame = True

    while (playGame and money > 0):             #главный цикл рулетки
        colorLine(3, 'ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!')
        color(14)
        print(f'\n У Вас на счету {money} {valuta} \n')
        color(11)
        print('\n  Ставка на:')
        print('    1. Чётное (выйгрыш 1:1)')
        print('    2. Нечётное (выйгрыш 1:1)')
        print('    3. Дюжина (выйгрыш 3:1)')
        print('    4. Число (выйгрыш 36:1)')
        print('    0. Возврат в предыдущее меню\n')

        x = getInput('01234', '    Твой выбор?')    #выбор пункта из меню игры

        playRoulette = True         #условие игры в рулетку (играем или нет)

        if(x == '3'):             #выбор дюжины
            color(2)
            print()
            print(' Выбери числа:')
            print('    1. От 1 до 12')
            print('    2. От 13до 24')
            print('    3. От 25 до 36')
            print('    0. Назад')

            duzhina = getInput('0123', '    Твой выбор?')   #выбор конкретной дюжины

            if(duzhina == '1'):
                textDuzhina = 'от 1 до 12'
            elif(duzhina == '2'):
                textDuzhina = 'от 13 до 24'
            elif(duzhina == '3'):
                textDuzhina = 'от 25 до 36'
            elif(duzhina == '0'):
                playRoulette = False        #если захотел выйти из дюжины, возврат к меню рулетки
        elif(x == '4'):
            chislo = getIntInput(0, 36, '    На какое число будете ставить? (0...36):')     #ставка на число

        color(7)
        if(x == '0'):   #если выбрал выход вместо конкретной игры (возвращается к главному меню)
            return 0

        if(playRoulette):   #еси выбрал игру, пора делать ставки
            stavka = getIntInput(0, money, f'    Делайте ваши ставки, господа! (не больше {money})')

            if(stavka == 0):    #если ставка 0 - выход из игры в главное меню
                return 0

            number = getRoulette(True) #анимация рулетки плюс рандом числа

            print()
            color(11)
            if(number < 37):
                print(f'    Выпало число {number}!' + '*' * number)
            else:
                if(number == 37):
                    printNumber = '00'
                elif(number == 38):
                    printNumber = '000'
                print(f'Выпало число {printNumber}!')

            #результаты игры
            if(x == '1'):
                print('    Ваша ставка на ЧЕТНОЕ!')
                if(number < 37 and number % 2 == 0):
                    money += stavka
                    vin(stavka)
                else:
                    money -= stavka
                    defeat(stavka)
            elif(x == '2'):
                print('    Ваша ставка на НЕЧЕТНОЕ!')
                if(number < 37 and number % 2 != 0):
                    money += stavka
                    vin(stavka)
                else:
                    money -= stavka
                    defeat(stavka)
            elif(x == '3'):
                print(f'    Ваша ставка на дюжину {textDuzhina}')
                winDuzhina = ''

                if(0 < number < 13):
                    winDuzhina = '1'
                elif(12 < number < 25):
                    winDuzhina = '2'
                elif(24 < number < 37):
                    winDuzhina = '3'

                if(duzhina == winDuzhina):
                    money += stavka * 2
                    vin(stavka * 3)
                else:
                    money -= stavka
                    defeat(stavka)
            elif(x == '4'):
                print(f'    Ваша ставка на число {chislo}!')
                if(number == chislo):
                    money += stavka * 35
                    vin(stavka*36)
                else:
                    money -= stavka
                    defeat(stavka)

            input('\nНажмите Enter для продолжения...')

#после ставки, анимация
def getDice():
    count = random.randint(3, 8)    #сколько раз будут перекатываться кубики
    sleep = 0       #пауза

    while(count > 0):
        color(count + 7)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(' ' * 10,'----- -----')
        print(' ' * 10, f'| {x} | | {y} |')
        print(' ' * 10,'----- -----')
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1

    return x + y

#функция Костей
def dice():
    global money
    playGame = True

    while(playGame):

        print()
        colorLine(13, 'ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!')
        color(14)
        print(f'\n У Вас на счету {money} {valuta} \n')

        color(7)
        stavka = getIntInput(0, money, f'    Делайте ваши ставки, господа! (не больше {money})')
        if(stavka == 0):    #выход в главное меню
            return 0

        playRound = True        #играем в кости?
        control = stavka        #начальная ставка (константа)
        oldResult = getDice()   #предыдущий результат
        firstPlay = True        #первая игра?

        while (playRound and stavka > 0 and money > 0):     #цикл раунда
            if(stavka > money):
                stavka = money

            color(11)
            print(f'\n    В Вашем распоряжении {stavka} {valuta}')
            color(12)
            print(f'\n    Текущая сумма чисел на костях: {oldResult}.')
            color(11)
            print(f'\n    Сумма чисел на гранях при следующем броске будет больше, меньше или равной предыдущей?')
            color(7)
            x = getInput('0123', '    Как вы считаете? 1 - больше, 2 - меньше, 3 - равна, 0 - выход: ')

            if(x != '0'):     #сделана ставка, играем
                firstPlay = False   #дальше уже не первый раунд
                if(stavka > money):     #если вдруг кончились деньги
                    stavka = money

                money -= stavka     #списываем с кошелька ставку

                diceResult = getDice()  #бросаем кости

                win = (oldResult < diceResult and x == '1') or (oldResult > diceResult and x == '2')    #смотрим, победил ли игрок

                if(not x == '3'):   #определяем результат игры
                    if(win):
                        money += stavka + stavka // 5
                        vin(stavka // 5)
                        stavka += stavka // 5
                    else:
                        stavka = control
                        defeat(stavka)
                elif(x == '3'):     #победа/поражение для равенства
                    if(oldResult == diceResult):
                        money += stavka * 3
                        vin(stavka * 2)
                        stavka *= stavka * 3
                    else:
                        stavka = control
                        defeat(stavka)

                oldResult = diceResult #перезаписываем предыдущий результат

            else: #выход на первой ставке
                if(firstPlay):
                    money -= stavka
                playRound = False

#однорукий Бандит
def bandit():
    global money
    playBandit = True

    while(playBandit):
        colorLine (13, 'ДОБРО ПОЖАЛОВАТЬ В АВТОМАТЫ!')
        color(14)
        print(f'У Вас на счету {money} {valuta}')
        color(5)
        print('\nПравила игры:\
    \n1. При совпадении 2-х чисел выйгрыш 1:1. \
    \n2. При совпадении 3-х чисел выйгрыш 2:1.\
    \n3. При совпадении 4-х чисел выйгрыш 5:1.\
    \n4. При совпадении 5-ти чисел выйгрыш 10:1.\
    \n0. Ставка 0 для завершении игры.')

        stavka = getIntInput(0, money, f'Введите ставку (не больше {money}): ') #ставка

        if(stavka == 0):    #если ставка 0 - выход в главное меню игры
            return 0

        money -= stavka #списали ставку

        money += getBandit(stavka) #прибавили выйгрыш

        if(money <= 0):
            playBandit = False

#анимация
def getBandit(stavka):
    res = stavka

    d1 = 0    #цифры в слотах
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    getD1 = True    #пока истина меняем цифры
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True

    col = 10

    while(getD1 or getD2 or getD3 or getD4 or getD5): #вращение слотов
        if(getD1):
            d1 += 1
        if(getD2):
            d2 -= 1
        if(getD3):
            d3 += 1
        if(getD4):
            d4 -= 1
        if(getD5):
            d5 += 1

        if(d1 > 9):         #проверка, что числа не двухзначные
            d1 = 0
        if(d2 < 0):
            d2 = 9
        if(d3 > 9):
            d3 = 0
        if(d4 < 0):
            d4 = 9
        if(d5 > 9):
            d5 = 0

        if(random.randint(0, 20) == 1):
            getD1 = False
        if(random.randint(0, 20) == 1):
            getD2 = False
        if(random.randint(0, 20) == 1):
            getD3 = False
        if(random.randint(0, 20) == 1):
            getD4 = False
        if(random.randint(0, 20) == 1):
            getD5 = False

        time.sleep(0.1) #пауза между сменой кадров
        color(col)
        col += 1
        if(col > 15):
            col = 10

        os.system('cls')                #очистка экрана командной строки

        print('><' * 9)
        print(f'    {d1} {d2} {d3} {d4} {d5}')
        print('><' * 9)

    maxCount = getMaxCount(d1, d1, d2, d3, d4, d5)  #поиск количества совпадений

    if(maxCount < getMaxCount(d2, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if(maxCount < getMaxCount(d3, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if(maxCount < getMaxCount(d4, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if(maxCount < getMaxCount(d5, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    color(14)
    if(maxCount == 2):
        print(f' Совпадение двух чисел. Ваш выйгрыш {res} {valuta}')
    elif(maxCount == 3):
        res *= 2
        print(f' Совпадение трех чисел. Ваш выйгрыш {res} {valuta}')
    elif(maxCount == 4):
        res *= 5
        print(f' Совпадение ЧЕТЫРЕХ чисел! Ваш выйгрыш {res} {valuta}')
    elif(maxCount == 5):
        res *= 10
        print(f'СОВПАДЕНИЕ ВСЕХ ЧИСЕЛ!!! ВЫШ ВЫЙГРЫШ {res} {valuta}')
    else:
        defeat(res)
        res = 0

    color(11)
    input('\n Нажмите Enter для продолжения...')

    return res

#считает количество совпадений
def getMaxCount(digit, v1, v2, v3, v4, v5):
    sovp = 0

    if(digit == v1):
        sovp += 1
    if(digit == v2):
        sovp += 1
    if(digit == v3):
        sovp += 1
    if(digit == v4):
        sovp += 1
    if(digit == v5):
        sovp += 1

    return sovp

#главный цикл игры
def main():
    global money, playGame  #определяем глобальные переменные
    money = loadMoney()     #загружаем деньги из файла
    startMoney = money

    while(money > 0 and playGame):  #главный цикл игры
        colorLine(10, 'Приветствую тебя в казино, дружище!')
        color(14)
        print(f'\nУ Вас на счету {money} {valuta}\n')

        color(6)
        print('\n  Вы можете сыграть в:')
        print('    1. Рулетку')
        print('    2. Кости')
        print('    3. Однорукого бандита')
        print('    0. Выход. Ставка 0 в играх - Выход\n')
        color(7)

        x = getInput('0123', '    Ваш выбор?')

        if (x == '0'):
            playGame = False
        elif(x == '1'):
            roulette()
        elif(x == '2'):
            dice()
        elif(x == '3'):
            bandit()

    colorLine(12, '\nЖаль, что вы так скоро уходите. Мы будем ждать Вас вновь!\n')
    color(13)

    if(money <= 0):
        print('\nВаша казна опустела, милорд! Придется взять кретит, что бы вернуться.')

    color(11)
    if(money == startMoney):
        print('\nДаже не знаем везение это или нет, но Вы остались при своих средствах ничего при этом не проиграв.')
        print('Надеемся, что вы получили удовольствие, посетив наше заведение.')
        print('Ждем вас снова!')
    elif(money > startMoney):
        print(f'\nЧто же, поздравляем, Вы выйграли у казино.')
        print(f'Ваша прибыль составила {money - startMoney} {valuta}')
        print('Приходите снова и выигрывайте еще больше!')
    elif(money < startMoney):
        print(f'\nК сожалению Вы проиграли.')
        print(f'Ваш убыток составил {startMoney - money} {valuta}')
        print('Приходите снова и у Вас наверняка все получится!')

    saveMoney(money)        #сохраняем количество денег в файле

    color(7)
    quit(0)

#отсюда и начинается выполнение программы
main()
