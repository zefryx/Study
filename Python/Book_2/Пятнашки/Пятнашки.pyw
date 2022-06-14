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
    print('Нажата кнопка СТАРТ')

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
    return 0

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
    return 0

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
radio01 = Radiobutton(root, text='Скин 1', variable=image, value=True, activebackground=back, bg=back, fg=fore)
radio01.place(x=150, y=416)

# используемые переменные
# =========== П Е Р Е М Е Н Н Ы Е =============

# номер пустого поля
black_img = 0

# список, содержащий расположение текущих спрайтов на поле
image_background = []

# списки для хранения разных скинов
image_background01 = []
image_background02 = []

#набор виджетов, в которых выводятся спрайты в окне
label_image = []

# математическая модель игрового поля, хранится расположений тайтлов сейчас
data_image = []

# копия data_image, когда зажата кнопка Посмотреть
copy_data = []

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
