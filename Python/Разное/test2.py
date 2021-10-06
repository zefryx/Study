from tkinter import *
root = Tk()

#label1 = Label(text='Label').grid(row=1, column=0)

POS_X = root.winfo_screenwidth() // 100  # позиция координаты окна для размещения по центру экрана
POS_Y = root.winfo_screenheight() // 100

letters = [i for i in range(100)]
labels = {}
xPos = 0
yPos = 0
for letter in letters:
    if(yPos == 10):
        xPos = xPos + 1
        yPos = 0
#    if(xPos == 10):
#        yPos = 7
    labels[letter] = Label(width=POS_X, height=POS_Y, text='A')
    labels[letter].grid(row=xPos, column =yPos)
    yPos = yPos + 1

root.mainloop()
