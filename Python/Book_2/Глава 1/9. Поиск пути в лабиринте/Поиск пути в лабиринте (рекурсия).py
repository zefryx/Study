import os
import time

# печать массива значений лабиринта
def printList2D(list):
    for i in range(len(list)):
        print(end='  ')
        for j in range(len(list[i])):
            if (list[i][j] != -1):
                if (list[i][j] != 'F'):
                    if (list[i][j] // 10 >= 1):
                        print(f'  {list[i][j]} ', end='')
                    else:
                        print(f'   {list[i][j]} ', end='')
                else:
                    print(f'   {list[i][j]} ', end='')
            else:
                print(f'  {list[i][j]} ', end='')
        print()

# вывод на экран лабиринта
def printLab():
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (map[i][j] == 1):        # 1 старт
                print(' o ', end='')
            elif (map[i][j] == 'F'):    # F финиш
                print(' X ', end='')
            elif (map[i][j] == -1):     # -1 стена
                print(wall, end='')
            elif (map[i][j] > 1):
                #print(f' . ', end='') # остальное убрать
                if (map[i][j] < 10):
                    print(f' {map[i][j]} ', end='')
                else:
                    print(f' {map[i][j]}', end='')
            else:                       # все остальное - проход
                print(path, end='')
        print()

# поиск индекса позиции
def searchCoordIndex(a):
    Coord = []
    xInd = 0
    yInd = 0

    while(not xInd):
        try:
            xInd = map[yInd].index(a)
        except:
            yInd += 1

    Coord.append(yInd)
    Coord.append(xInd)

    return Coord

# поиск координат пути
def searchCoord(a):
    c = finish.copy()

    ret = []
    ret.append(c)

    i = 0
    while(ret[i] != start):

        if (map[ret[i][0] + 1][ret[i][1]] == a - 1):
            ret.append([ret[i][0] + 1, ret[i][1]])
        elif (map[ret[i][0]][ret[i][1] + 1] == a - 1):
            ret.append([ret[i][0], ret[i][1] + 1])
        elif (map[ret[i][0] - 1][ret[i][1]] == a - 1):
            ret.append([ret[i][0] - 1, ret[i][1]])
        elif (map[ret[i][0]][ret[i][1] - 1] == a - 1):
            ret.append([ret[i][0], ret[i][1] - 1])
        i += 1
        a -= 1

    return ret

# движение по лабиринту
def move():
# переменная для копирования значений координат
    c = start.copy()
# текущая позиция на карте, или откуда еще доступен путь
    actPos = []
    actPos.append(c)
# найден ли выход
    exit = False
# основной цикл поиска пути
    i = 0
    while (not exit):
# если тупик - True
        lock = False
# проход по одной ветке, i++ по следующей ветви
        while (not lock and not exit):
# очистка экрана от лишнего
            os.system('cls')
# счетчик, сколько вариантов пути есть с клетки
            count = 0
            if (map[actPos[i][0] + 1][actPos[i][1]] == 0):
                count += 1
            if (map[actPos[i][0]][actPos[i][1] + 1] == 0):
                count += 1
            if (map[actPos[i][0] - 1][actPos[i][1]] == 0):
                count += 1
            if (map[actPos[i][0]][actPos[i][1] - 1] == 0):
                count += 1
# если путей нет - тупик, переход к следующей ветви пути
            if (count == 0):
                lock = True
            else:
# запись координат, если есть дополнительные ветви пути
                for j in range(1, count):
                    c = actPos[i].copy()
                    actPos.append(c)
# условия прохождения лабиринта
                if (map[actPos[i][0] + 1][actPos[i][1]] == 0):    # движение вниз
                    map[actPos[i][0] + 1][actPos[i][1]] += 1 + map[actPos[i][0]][actPos[i][1]]
                    actPos[i][0] += 1
                elif (map[actPos[i][0] - 1][actPos[i][1]] == 0):    # движение вверх
                    map[actPos[i][0] - 1][actPos[i][1]] += 1 + map[actPos[i][0]][actPos[i][1]]
                    actPos[i][0] -= 1
                elif (map[actPos[i][0]][actPos[i][1] + 1] == 0):    # движение вправо
                    map[actPos[i][0]][actPos[i][1] + 1] += 1 + map[actPos[i][0]][actPos[i][1]]
                    actPos[i][1] += 1
                elif (map[actPos[i][0]][actPos[i][1] - 1] == 0):    # движение влево
                    map[actPos[i][0]][actPos[i][1] - 1] += 1 + map[actPos[i][0]][actPos[i][1]]
                    actPos[i][1] -= 1
# печать пути лабиринта
            printLab()
#            print('\n\n')
#            printList2D(map)
# найден ли финиш
            if ((map[actPos[i][0] + 1][actPos[i][1]] or\
                 map[actPos[i][0]][actPos[i][1] + 1] or\
                 map[actPos[i][0] - 1][actPos[i][1]] or\
                 map[actPos[i][0]][actPos[i][1] - 1]) == 'F'):
                exit = True
                stepLab = map[actPos[i][0]][actPos[i][1]] + 1
                print('Выход найден!')
                print(f'Минимальное количество ходов, для достижения выхода = {stepLab}')
                wayCoord = searchCoord(stepLab)
                wayCoord.reverse()
                print('Координаты пути:')
                printList2D(wayCoord)
# пауза,для плавности печати
#            time.sleep(0.00005)
        i += 1

map = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       [-1,  1, -1,  0,  0,  0, -1,  0,  0,  0, -1],
       [-1,  0,  0,  0, -1,  0, -1,  0, -1,  0, -1],
       [-1,  0, -1,  0, -1,  0,  0,  0, -1,  0, -1],
       [-1,  0, -1,  0, -1, -1, -1, -1, -1,  0, -1],
       [-1,  0, -1,  0,  0,  0,  0,  0, -1,  0, -1],
       [-1,  0, -1, -1, -1, -1, -1, -1, -1,  0, -1],
       [-1,  0,  0,  0,  0,  0,  0,  0, -1,'F', -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

start = searchCoordIndex(1)     # 1 - старт
finish = searchCoordIndex('F')  # F - финиш

wall = '|||'
path = '   '

#printLab()
#printList2D(map)
move()
