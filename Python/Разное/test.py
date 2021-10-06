from tkinter import *   #импорт библиотеки tkinter
from tkinter import messagebox
from tkinter import ttk
import random
import time

def showInTerminal(*args):
    lbl['text'] = cmbSelect.get()

WIDTH = 250    #размеры окна
HEIGHT = 150

root = Tk()     #переменная, управляющая библиотекой tkinter

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2  #позиция координаты окна для размещения по центру экрана
POS_Y = root.winfo_screenheight() //2 - HEIGHT // 2

root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')  #установка окна
root.title('Тестик')                              #заголовок окна
root.resizable(False, False)                        #запрет изменение размеров окна

#выпадающие списки со ставками
cmb = ttk.Combobox(root)
cmb['state'] = 'readonly' #только чтение
cmb.place(x = 60, y = 50)   

cmbSelect = StringVar()
cmb['textvariable'] = cmbSelect
cmb['values'] = ['Привет!', 'bonjorno!', 'oh, hi!']
#cmb.current(0)

cmb.bind('<<ComboboxSelected>>', showInTerminal)

lbl = Label(root, font='Arial 15')
lbl['text'] = 'Здесь выбор'
lbl.place(x=10, y=10)

root.mainloop() #запуск программы

#игра в орла и решку
'''
import random

n = 1000000 #количество бросков
for i in range(5):
    orel = 0
    reshka = 0

    for j in range(n):
        if(random.randint(0, 1) == 0):
            orel += 1
        else:
            reshka +=1
    print(f'Из {n} бросков {orel} - орел, {reshka} - решка. Отношение {orel/reshka}')
'''
#задания из главы 4.2
'''
import random

a = 0
b = 0
c = 0
d = 0
e = 0

def maxi(a, b):
    if(a > b):
        return(a)
    elif(a < b):
        return(b)
    elif(a == b):
        print('Числа равны.')

def step(a, b):
    if(b == 1):
        return(a)
    elif(b == 0):
        return(1)
    for i in range b
        if(i > 1):
            a *= a
        return a

def rand5():
    c = random.randint(0, 20)
    c = c * 5
    return(c)

def arif(a,b,c,d,e):
    summa = a + b + c + d + e
    ariff = summa / 5
    return(ariff)

print('1 - максимальное из двух чисел \n
2 - a ^ b \n
3 - случайное число кратное 5 \n
4 - среднее арифметическое из 5 чисел')

var = int(input('Что собрались делать? '))

if(var == 1):
    a = int(input('Введите a '))
    b = int(input('Введите b '))
    print(maxi(a, b))

elif(var == 2):
    a = int(input('Введите a '))
    b = int(input('Введите b '))
    print(step(a, b))

elif(var == 3):
    print(f'Случайное число, кратное 5 = {rand5()}')

elif(var == 4):
    a = int(input('Введите a '))
    b = int(input('Введите b '))
    c = int(input('Введите c '))
    d = int(input('Введите d '))
    e = int(input('Введите e '))
    print(arif(a,b,c,d,e))
'''  
#создание, запись и чтение файла
'''
name = '' #имя файла
a = '' #a, b, c - переменные
b = ''
c = ''

nameWrite = input('Введите имя файла ')

f = open(f'{nameWrite}.txt', 'w', encoding = 'utf-8') 
a = input(f'Что хотите записать в первую строку? \n')
while(not b.isdigit()):
    b = input(f'Введите первое число для вычисления суммы. \n')
while(not c.isdigit()):
    c = input(f'Введите второе число для вычисления суммы. \n')

f.write(a + '\n')
f.write(b + '\n')
f.write(c + '\n')
f.write(str(int(b) + int(c)))
f.close()

nameOpen = input('Введите имя файла для открытия ')

try:
    f = open(f'{nameOpen}.txt', 'r', encoding = 'utf-8')
    print('В файле хранится следующая информация: ')
    x = f.readline().replace("\n", "")
    y = f.readline().replace("\n", "")
    z = f.readline().replace("\n", "")
    q = f.readline().replace("\n", "")
    f.close()
    print(f'{x}{y}{z}{q}')
except:
    print('Ошибка имени файла')
'''
#обработка ошибки
'''
try:
    f = open('???.txt', 'r', encoding = 'utf-8') #открытие файла для чтения, параметр R
    x = f.readline()
    f.close()
except IOError:
    print('Ошибка открытия файла')
    x = 0
print(x)
'''
#типы ошибок
'''
ZeroDivisionError - деление на 0
TypeError - несоответствие типов
NameError - отсутствие переменной
EOFError - нет строки для чтения
Warning - предупреждение
'''
#обработка ошибок
'''
a = 5
try:
    print(10 / a)
except ZeroDivisionError:
    print('Ошибка! Деление на 0.')

print('Все норм, работаем дальше!')
'''
#работа с файлами
'''
s = 'Приветики пистолетики!'
a = 100

f = open('testfile.txt', 'w', encoding = 'utf-8') #создание файла и запись в него, параметр W

f.write(s + '\n') #\n для того, что бы запись велась построчно
f.write(str(a))
f.close()       #закрыли файл

f = open('testfile.txt', 'r', encoding = 'utf-8') #открытие файла для чтения, параметр R

x = f.readline() #чтение строк файла в переменные
y = f.readline()
f.close()

x = x.replace('\n', '') #удаляем ВСЕ символы \n в строке и заменяем на пустоту ''

print(x)
print(y)
'''
#тест остановки работы цикла
'''
a = True

while(a == True):
    print(1)
    print(2)
    a = input()
    if(a == 'False'):
        a = False
        break
    print(a)
    print(3)
print(4)
'''
#Генерирует числа кратные N в диапазоне от Х до Y
'''
import random

x = ''
y = ''
z = 0
n = 5 #кратность числа

while(not x.isdigit()):
    x = input('Введите число x ')
    if(not x.isdigit()):
        print('Это не число. Введите число!')
x = int(x)

while (not y.isdigit() or int(y) < x):
    y = input('Введите число y ')
    if(not y.isdigit()):
        print('Это не число. Введите число!')
    elif(int(y) < x):
        print('y не может быть меньше x')
y = int(y)

if(y - x >= n or x % n == 0 or y % n == 0 or (x // n + 1) * n <= y):
    z = random.randint(x, y) // n * n
    if(z < x):
        z = z + n
else:
    z = 0

print(z)      
'''
#проверка ввода строки
'''
qua = input('Введите Нет или нет   ')

if (qua == 'Нет' or qua == 'нет'):
    print('Молодец!')
else:
    print ('Ну и лошара...')

'''
#Вывод последовательности чисел 8 4 9 3 10 2 11 1 12 0 13, END нужен для того, что бы вывод был в строку, а не каждый раз с новой строки
'''
x = int(8)
print (x, end = ' ')
for i in range(4, 14, 1):
    if(i%2 == 0):
        x = x - i
        print (x, end=' ')
    else:
        x = x + i
        print (x, end=' ') 
'''
#_________________________________________________________________
'''money = int(input('Enter the amount of money: '))

for i in range (10):
    print()
    buy = int(input('Enter the product cost: '))

    money = money - buy

    print ('You have', money, 'money left.')
    if (money <= 0):
        print ('Stop shopping! Money run out!')
'''
#Вычисление факториала
'''
summa = 1

o = int(input('What number factorial do you want to calculate? ')) 

for i in range (2, o+1):
    summa *= i

print ('Factorial', str(o) + '!', '=', summa)

#_________________________________________________________________

'''
