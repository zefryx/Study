from tkinter import *

root = Tk()
root.resizable(False, False)
root.title('x-o')

WIDTH = 210
HEIGHT = 210

n = 10
m = 10
side = 19

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

label_image = []
data_image = []

for i in range(n):
    label_image.append([])
    data_image.append([])

    for j in range(m):
        data_image[i].append(i * n + j)

        label_image[i].append(Label(root, width = 2, height = 1, bg = 'green'))
        label_image[i][j]['bd'] = 0
        label_image[i][j].place(x = 10 + j * side, y = 10 + i * side)
        label_image[i][j].bind('<Button-1>')

root.mainloop()
