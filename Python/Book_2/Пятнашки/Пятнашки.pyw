# импорт библиотек
# ============== И М П О Р Т ================

# Tkinter
from tkinter import *
# radiobutton
from tkinter import ttk
# всплывающие окна
from tkinter import messagebox
# рандом
from random import randint
# пищалка
from winsound import Beep
# пауза
from time import sleep

# функции и методы
# ======== Ф У Н К Ц И И  И  М Е Т О Д Ы ==========

# срабатывает после нажатия на кнопку Старт
def start_new_round():
    global play_game, steps

    # игра начата
    play_game = True
    steps[diff_combobox.current()] = 0
    # деактивируем все ненужные виджеты
    start_button['state'] = DISABLED
    radio01['state'] = DISABLED
    radio02['state'] = DISABLED
    diff_combobox['state'] = DISABLED

    # проигрываем мелодию
    Beep(294, 125)

    refresh_text()

# задача - оформить данный цикл без break (while)
# задача - избавиться от циклов поиска пустой клетки
    # метод поиска пустого поля
    x = 0
    y = 0
    for i in range(n):
        for j in range(m):
            if data_image[i][j] == black_img:
                x = i
                y = j
                break

    # запускаем метод перемешивания поля
    shuffle_pictures(x, y)

# перемешивает спрайты (x,y - координаты пустого спрайта)

# задача - избавиться от проблемы выхода за границы поля
# при генерации выбора направления движения
# например при позиции [3][3] нельзя двигаться вниз и вправо
# и цикл for с вероятностью 50% будет работать бесполезно
def shuffle_pictures(x, y):
    if diff_combobox.current() < 5:
        # количество перемешиваний в зависимости от уровня сложности
        count = (2 + diff_combobox.current()) ** 4
        # переменная для запрета одного направления
        no_direction = 0

        # повторение перемешиваний
        for i in range(count):
            # перемешиваем, пока не сгенерируется доступное направление
            direction = no_direction

            while direction == no_direction:
                # если переменная direction равна переменной no_direction
                # она генерируется снова, т.к. передвигать спрайт в этом
                # направлении запрещено
                direction = randint(0, 3)

            # перемещаем спрайты
            # вниз
            if direction == 0 and x + 1 < n:
                # обмениваем спрайты
                exchange_image(x, y, x + 1, y)
                # увеличиваем x, т.к. пустое поле переместилось ниже
                x += 1
                # запрещаем направление наверх, т.к. там был пустой спрайт
                no_direction = 1
            # вверх
            elif direction == 1 and x - 1 >= 0:
                exchange_image(x, y, x - 1, y)
                x -= 1
                no_direction = 0
            # вправо
            elif direction == 2 and y + 1 < m:
                exchange_image(x, y, x, y + 1)
                y += 1
                no_direction = 3
            # влево
            elif direction == 3 and y - 1 >= 0:
                exchange_image(x, y, x, y - 1)
                y -= 1
                no_direction = 2

    else:
        exchange_image(n - 1, m - 3, n - 1, m - 2)

    reset_button['state'] = NORMAL

    Beep(1750, 50)

# меняет местами спрайты с координатами x1,y2 и x2,y2
# задача - прописать код анимации смены спрайтов
def exchange_image(x1, y1, x2, y2):
    global data_image, label_image

    # меняем местами номера изображений в data_image
    data_image[x1][y1], data_image[x2][y2] = \
            data_image[x2][y2], data_image[x1][y1]
    # меняем местами спрайты в label_image
    label_image[x1][y1]['image'] = image_background[data_image[x1][y1]]
    label_image[x2][y2]['image'] = image_background[data_image[x2][y2]]
    # обновляем картинку на экране
    root.update()

    sleep(0.001)

# сбрасывает ижображение на собранное (кнопка Сброс)
def reset_pictures():
    global data_image, play_game, steps

    # игра окончена
    play_game = False
    steps[diff_combobox.current()] = 0

    # восстанавливаем состояние виджетов
    start_button['state'] = NORMAL
    reset_button['state'] = DISABLED
    radio01['state'] = NORMAL
    radio02['state'] = NORMAL
    diff_combobox['state'] = 'readonly'

    # вносим в data_image данные нормального положения спрайтов
    for i in range(n):
        for j in range(m):
            data_image[i][j] = i * n + j

    # задаем пустое поле
    data_image[n - 1][m - 1] = black_img

    # звуки
    Beep(800, 50)
    Beep(810, 35)

    # обновляем экран
    update_pictures()
    refresh_text()

# обновляет изображения
def update_pictures():
    # проходим по всем ячейкам label_image для обновления спрайтов на экране
    for i in range(n):
        for j in range(m):
            label_image[i][j]['image'] = image_background[data_image[i][j]]

    root.update()

# сохраняет рекорды в файл для каждого уровня сложности
# если файла нет - создает его
def save_records():
    global record

    try:
        # открываем файл и записываем
        f = open('steps.dat', 'w', encoding='utf-8')
        for i in range(len(steps)):
            # условие для проверки, есть ли новый рекорд
            if steps[i] > 0 and steps[i] < record[i]:
                record[i] = steps[i]

            f.write(str(record[i]) + '\n')

        f.close()
    # в случае ошибки
    except:
        messagebox.showinfo('Ошибка', 'Возникла проблема с файлом при сохранении очков')

# загружает рекорды из файла
# если файла нет - ставит значения по умолчанию
# задача - сделать метод чуть более оптимизированным
def get_record_step():

    try:
        m = []
        # открываем файл только для чтения
        f = open('steps.dat', 'r', encoding='utf-8')

        for line in f.readlines():
            m.append(int(line))
        f.close()
    except:
        m = []
    # если в файле не 6 строк с рекордами, то -
    if len(m) != 6:
        m = []
        for i in range(6):
            m.append(1000 + 1000 * i)

    return m

# обновляет поля Label
def refresh_text():
    text_steps['text'] = f'Сделано ходов: {steps[diff_combobox.current()]}'
    text_record['text'] = f'Рекорд ходов: {record[diff_combobox.current()]}'

# передвигает спрайт на свободное место
# увелиивает количество сделанных ходов
# проверяет собран ли паззл
def go(x, y):
    global steps, play_game

    # проверям снизу ли пустая клетка
    if (x + 1 < n and data_image[x + 1][y] == black_img):
        # если да - меняем местами
        exchange_image(x, y, x + 1, y)
    elif (x - 1 >= 0 and data_image[x - 1][y] == black_img):
        exchange_image(x, y, x - 1, y)
    elif (y + 1 < m and data_image[x][y + 1] == black_img):
        exchange_image(x, y, x, y + 1)
    elif (y - 1 >= 0 and data_image[x][y - 1] == black_img):
        exchange_image(x, y, x, y - 1)
    else:
        Beep(500, 100)
        return 0

    Beep(1400, 5)

    # пюс ход к уровню сложности
    if play_game:
        steps[diff_combobox.current()] += 1
        refresh_text()

        # переменная, для проверки выйграл ли игрок
        win = True

        # задача - избавиться от for и бессмысленной прокрутки циклов
        # когда win = False
        for i in range(n):
            for j in range(m):

                if i == n - 1 and j == m - 1:
                    win = win and data_image[i][j] == black_img
                else:
                    win = win and data_image[i][j] == i * n + j
        if win:
            data_image[n - 1][m - 1] = black_img - 1
            update_pictures()

            messagebox.showinfo('Браво!', 'Вы молодец!')

            music()
            save_records()

            play_game = False

            refresh_text()

# показыавет, как должен выглядеть собранный паззл
# зажата кнопка Посмотреть
def see_start(event):
    global copy_data, data_image
    Beep(1632, 25)
    # копируем data_image в copy_data
    for i in range(n):
        for j in range(m):
            copy_data[i][j] = data_image[i][j]
            data_image[i][j] = i * n + j

    update_pictures()

# возвращает все, как было
# кнопка посмотреть отпущена
def see_end(event):
    global data_image
    Beep(1082, 25)
    # копируем copy_data в data_image
    for i in range(n):
        for j in range(m):
            data_image[i][j] = copy_data[i][j]

    update_pictures()

# выбор рисунка для игры
def is_check_image():
    global image_background
    # если в радиокнопке истина - первый скин
    if image.get():
        image_background = image_background01
        Beep(1000, 25)
    # ложь - второй
    else:
        image_background = image_background02
        Beep(1000,25)
    # обновляем картинку
    update_pictures()

# победоносная музычка
def music():
    Beep(100, 100)
    Beep(200, 200)
    Beep(300, 250)

# главное окно программы
# ======== О К Н О  П Р О Г Р А М М Ы ==========

# цвета для виджетов
back = '#373737'
fore = '#AFAFAF'

# список с уровнями сложности
item_diff = ['Простой',
             'Обычный',
             'Редкий',
             'Мифический',
             'Легендарный',
             'НЕВОЗМОЖНО!']

# создание окна
root = Tk()
root.resizable(False, False)
root.title("Пятнашки-шестнадцатяшки")

# замена иконки приложения
root.iconbitmap('icon/icon.ico')

# настройка размеров окна
WIDTH = 422
HEIGHT = 598 # 730 - 132
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

# фоновый цвет окна
root['bg'] = back

# кнопка ПОСМОТРЕТЬ СОБРАННОЕ
see_button = Button(root, text = 'Посмотреть, как должно быть', width=56)
see_button.place(x=10, y=488)
# зажатие кнопки
see_button.bind('<Button-1>', see_start)
see_button.bind('<ButtonRelease>', see_end)

# кнопка СТАРТ
start_button = Button(root, text = 'СТАРТ', width=56)
start_button.place(x=10, y=518)
start_button['command'] = start_new_round

# кнопка СБРОС
reset_button = Button(root, text = 'СБРОС', width=56)
reset_button.place(x=10, y=548)
reset_button['command'] = reset_pictures

# метка для вывода текста с количеством
# сделанных ходов и рекордом текущего уровня
text_steps = Label(root, text='steps', bg=back, fg=fore)
text_steps.place(x=10, y=418)
text_record = Label(root, text='record', bg=back, fg=fore)
text_record.place(x=10, y=438)

# выбор уровня сложности
Label(root, bg=back, fg=fore, text='Сложность:').place(x=267, y=418)
diff_combobox = ttk.Combobox(root, width=20, values=item_diff, state='readonly')
diff_combobox.place(x=267, y=438)
diff_combobox.bind('<<ComboboxSelected>>',lambda e: refresh_text())
# выбранная сложность в момент запуска
# задача - сложность ставится такая же, какая была на момент закрытия игры
diff_combobox.current(0)

# радиопереключатели
# создаем переменную
image = BooleanVar()
# устанавливаем значение
image.set(True)

# создаем переключатель и привязываем переменную image
radio01 = Radiobutton(root, text='Зеленый', variable=image, value=True, activebackground=back, bg=back, fg=fore)
radio02 = Radiobutton(root, text='Голубой', variable=image, value=False, activebackground=back, bg=back, fg=fore)
radio01['command'] = is_check_image
radio02['command'] = is_check_image
radio01.place(x=150, y=416)
radio02.place(x=150, y=436)

# параметры изображения
# ========== И З О Б Р А Ж Е Н И Е ============

# размер поля
n = 4
m = 4

# размер полного изображения
picture_width = 400
picture_height = 400

# размер одного спрайта
width_pic = picture_width / n
height_pic = picture_height / m

# список названий файлов спрайтов
file_name = ['img01.png',
             'img02.png',
             'img03.png',
             'img04.png',
             'img05.png',
             'img06.png',
             'img07.png',
             'img08.png',
             'img09.png',
             'img10.png',
             'img11.png',
             'img12.png',
             'img13.png',
             'img14.png',
             'img15.png',
             'img16.png',
             'black.png']

# используемые переменные
# =========== П Е Р Е М Е Н Н Ы Е =============

# список, содержащий расположение текущих спрайтов на поле
image_background = []

# списки для хранения разных скинов
image_background01 = []
image_background02 = []

for name in file_name:
    image_background01.append(PhotoImage(file='image01/' + name))
    image_background02.append(PhotoImage(file='image02/' + name))

# номер пустого поля
black_img = 16

# устанавливаем первый набор спрайтов по умолчанию
# задача - при запуске программы устанавливается скин, который был при закрытии
image_background = image_background01

#набор виджетов, в которых выводятся спрайты в окне
label_image = []

# математическая модель игрового поля, хранится расположений тайтлов сейчас
data_image = []

# копия data_image, когда зажата кнопка Посмотреть
copy_data = []

# наполняем скиски выше
for i in range(n):
    label_image.append([])
    data_image.append([])
    copy_data.append([])

    for j in range(m):
        # создаем ряд числе от 1 до 16
        # это номера собранного паззла
        data_image[i].append(i * n + j)
        copy_data[i].append(i * n + j)

        # создаем и настраиваем label, в который будем
        # выводить спрайты PhotoImag из image_background
        label_image[i].append(Label(root, bg=back))
        label_image[i][j]['bd'] = 1
        label_image[i][j].place(x = 10 + j * width_pic, y = 10 + i * height_pic)

        # что произойдет при нажатии на label
        label_image[i][j].bind('<Button-1>', lambda e, x=i, y=j: go(x, y))

        # устанавливаем изображение
        label_image[i][j]['image'] = image_background[data_image[i][j]]

# количество сделанных ходов до полной сборки для разных уровней сложности
# индекс 0 - сложность 1, индекс 1 - сложность 2 и т.д.
steps = [0, 0, 0, 0, 0, 0]

# рекорды (минимальное количество ходов) для разных уровней сложности
# индекс 0 - сложность 1, индекс 1 - сложность 2 и т.д.
record = get_record_step()

# логическая переменная - начата ли игра?
play_game = False

# обновляем поле
reset_pictures()
refresh_text()

root.mainloop()
