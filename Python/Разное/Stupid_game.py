from tkinter import *
from random import randint

# когда курсор наводится на кнопку
def motion_mouse(event):
    btn.place(x=randint(0, w - btn.winfo_reqwidth()), y=randint(0, h))

# нажатие на кнопку
def press_mouse(event):
    quit(0)

# создаем окно и разворачиваем на полный экран
root = Tk()
root.attributes('-fullscreen', True)
root.resizable(True, True)

# черный цвет фона
root.configure(bg='#000000')

# получаем размеры экрана
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

# создаем кнопку
btn = Button(text='Что бы продолжить работу, нажмите на кнопку.', font='Arial 20')
btn.place(x=w // 2 - btn.winfo_reqwidth() // 2, y=h // 2)

# что произойдет, когда курсор окажется над кнопкой
btn.bind('<Enter>', motion_mouse)

btn.bind('<Button-1>', press_mouse)

root.mainloop()
