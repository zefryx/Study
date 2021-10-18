from tkinter import *

def goCode():
    tOutput.delete(1.0, END)
    tIn = tInput.get(1.0, END)
    tIn = tIn[0:len(tIn) - 1]
    Len = len(tIn)
    tOut = ''

    if (rBtn.get() == 0):
        for i in range(Len - 1, -1, -1):
            tOut += tIn[i]
    if (rBtn.get() == 1):
        for i in range(0, Len - 1, 2):
            tOut += tIn[i + 1] + tIn[i]
        if (Len % 2 != 0):
            tOut += tIn[Len - 1]
    if (rBtn.get() == 2):
        for i in range(Len):
            tOut += chr(ord(tIn[i]) + 1)
    if (rBtn.get() == 3):
        p = 0
        for i in range(Len):
            tOut += chr(ord(tIn[i]) + p)
            p = (p + 1) % 33

    tOutput.insert(1.0, tOut)

def goDecode():
    if (rBtn.get() == 0 or rBtn.get() == 1):
        goCode()
    else:
        tOutput.delete(1.0, END)
        tIn = tInput.get(1.0, END)
        tIn = tIn[0:len(tIn) - 1]
        Len = len(tIn)
        tOut = ''

        if (rBtn.get() == 2):
            for i in range(Len):
                tOut += chr(ord(tIn[i]) - 1)
        if (rBtn.get() == 3):
            p = 0
            for i in range(Len):
                tOut += chr(ord(tIn[i]) - p)
                p = (p + 1) % 33

        tOutput.insert(1.0, tOut)

def copyToClipboard():
    root.clipboard_clear();
    root.clipboard_append(tOutput.get(1.0, END))

def pasteFromClipboard():
    try:
        tInput.insert(END, root.clipboard_get())
    except:
        tInput.insert(END, '\nОШИБКА: буфер пуст')

def resToDef():
    tInput.delete(1.0, END)
    txt = tOutput.get(1.0, END)
    txt = txt[0:len(txt) - 1]
    tInput.insert(1.0, txt)

def clearText():
    tInput.delete(1.0, END)
    tOutput.delete(1.0, END)

def setMenuPos(event):
    menuInput.post(event.x_root, event.y_root)

#инициализация окна
root = Tk()
root.resizable(False, False)
root.title('Шифровщик')

WIDTH = 800
HEIGHT = 320
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

#текстовые поля
textInput = Label(text='Введите исходный текст:')
textInput.place(x=2, y=1)
textOutput = Label(text='Результат:')
textOutput.place(x=2, y=157)

tInput = Text(width=70, height=8, wrap=WORD)
tInput.place(x=5, y=20)

#скролл бары для текстовых полей
scrollInput = Scrollbar(command = tInput.yview, width=20)
scrollInput.place(x=570, y=20, height = 132)
tInput['yscrollcommand'] = scrollInput.set

tOutput = Text(width=70, height=8, wrap=WORD)
tOutput.place(x=5, y=180)

scrollOutput = Scrollbar(command = tOutput.yview, width=20)
scrollOutput.place(x=570, y=180, height = 132)
tOutput['yscrollcommand'] = scrollOutput.set

#меню на правую кнопку
menuInput = Menu(tearoff=False)
menuInput.add_command(label='Копировать реультат', command=copyToClipboard)
menuInput.add_command(label='Вставить в исходный текст', command=pasteFromClipboard)
menuInput.add_command(label='Результат -> Исходный', command=resToDef)
menuInput.add_command(label='Очистить  текст', command=clearText)
tInput.bind('<Button-3>', setMenuPos)

#кнопки шифровать / дешифровать
btnCode = Button(text='Шифровать', width=25, command=goCode)
btnCode.place(x=600, y=20)

btnDecode = Button(text='Дешифровать', width=25, command=goDecode)
btnDecode.place(x=600, y=50)

#радиокнопки
textAlgo = Label(text='Алгоритм:')
textAlgo.place(x=600, y=100)
rBtn = IntVar()
rBtn.set(0)
algo01 = Radiobutton(text='Инвентировать', variable=rBtn, value=0)
algo02 = Radiobutton(text='Замена с соседней', variable=rBtn, value=1)
algo03 = Radiobutton(text='+1', variable=rBtn, value=2)
algo04 = Radiobutton(text='+позиция (до 33)', variable=rBtn, value=3)
algo01.place(x=600, y=120)
algo02.place(x=600, y=140)
algo03.place(x=600, y=160)
algo04.place(x=600, y=180)

root.mainloop()
