from tkinter import *

WIDTH = 380
HEIGHT = 420

root = Tk()

# Расчет координат центра
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')      # установка окна на экране
root.title('Калькулятор')
root.resizable(False, False)

# создаем текстовое поле
text_field = Text(width=50, height=10, wrap=WORD)
text_field.place(x=10, y=10)

# создаем кнопок
button_1 = Button(text='1', font='arial 20', width=3)
button_1.place(x=10, y=360)

button_2 = Button(text='2', font='arial 20', width=3)
button_2.place(x=90, y=360)

button_3 = Button(text='3', font='arial 20', width=3)
button_3.place(x=170, y=360)

button_4 = Button(text='4', font='arial 20', width=3)
button_4.place(x=10, y=310)

button_5 = Button(text='5', font='arial 20', width=3)
button_5.place(x=90, y=310)

button_6 = Button(text='6', font='arial 20', width=3)
button_6.place(x=170, y=310)

button_7 = Button(text='7', font='arial 20', width=3)
button_7.place(x=10, y=260)

button_8 = Button(text='8', font='arial 20', width=3)
button_8.place(x=90, y=260)

button_9 = Button(text='9', font='arial 20', width=3)
button_9.place(x=170, y=260)

button_equal = Button(text='=', font='arial 20', width=2, height=2)
button_equal.place(x=310, y=330)

root.mainloop()
