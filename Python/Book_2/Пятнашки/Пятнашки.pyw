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


# функции и методы
# ======== Ф У Н К Ц И И  И  М Е Т О Д Ы ==========

# срабатывает после нажатия на кнопку Старт
def start_new_round():
    # деактивируем все ненужные виджеты
    start_button['state'] = DISABLED
    radio01['state'] = DISABLED
    radio02['state'] = DISABLED
    diff_combobox['state'] = DISABLED

    # проигрываем мелодию
    Beep(294, 125)

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

    # print('Нажата кнопка СТАРТ')

# перемешивает спрайты (x,y - координаты пустого спрайта)
def shuffle_pictures(x, y):
    return 0

# меняет местами спрайты с координатами x1,y2 и x2,y2
def exchange_image(x1, y1, x2, y2):
    return 0

# сбрасывает ижображение на собранное (кнопка Сброс)
def reset_pictures():
    print('Нажата кнопка СБРОС')

# обновляет изображения
def update_pictures():
    return 0

# сохраняет рекорды в файл для каждого уровня сложности
# если файла нет - создает его
def save_records():
    return 0

# загружает рекорды из файла
# если файла нет - ставит значения по умолчанию
def get_record_step():
    return 0

# обновляет поля Label
def refresh_text():
    print(f'Выбран уровень сложности : {diff_combobox.get()}')

# передвигает спрайт на свободное место
# увелиивает количество сделанных ходов
# проверяет собран ли паззл
def go(x, y):
    print(f'Пришли координаты x - {x}, y - {y}')

# показыавет, как должен выглядеть собранный паззл
# зажата кнопка Посмотреть
def see_start(event):
    print('Нажата кнопка ПОСМОТРЕТЬ')

# возвращает все, как было
# кнопка посмотреть отпущена
def see_end(event):
    print('Отжата кнопка ПОСМОТРЕТЬ')


# выбор рисунка для игры
def is_check_image():
    if image.get():
        image_background = image_background01
        print('Выбран Зеленый скин')
    elif not image.get():
        image_background = image_background02
        print('Выбран Голубой скин')

# победоносная музычка
def music():
    return 0

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
steps = []

# рекорды (минимальное количество ходов) для разных уровней сложности
# индекс 0 - сложность 1, индекс 1 - сложность 2 и т.д.
record = []

# список с названиями уровней сложности
item_diff = []

# логическая переменная - начата ли игра?
play_game = False



root.mainloop()
