from tkinter import *

global b1Count
b1Count = 0

def green_b1():
    b1['bg'] = 'green'
    global b1Count
    b1Count = 1

def red_b1():
    b1['bg'] = 'red'
    global b1Count
    b1Count = 2

def yellow_b1():
    b1['bg'] = 'yellow'
    global b1Count
    b1Count = 3

def white_b1():
    b1['bg'] = 'white'
    global b1Count
    b1Count = 0

def change():
    if b1Count == 0:
        green_b1()
    elif b1Count == 1:
        red_b1()
    elif b1Count == 2:
        yellow_b1()
    elif b1Count == 3:
        white_b1()

root = Tk()

b1 = Button(text='Нажми меня', width=15, height=3, bg='white')
b1['command']=change
b1.pack()

root.title('Тест3')
root.mainloop()
