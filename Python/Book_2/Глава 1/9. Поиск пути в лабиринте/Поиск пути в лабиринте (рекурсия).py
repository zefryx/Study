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
                print(f' . ', end='') # остальное убрать
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
def searchWay(a, x, y):
    res = []
    res.append([x, y])

    if (a[x + 1][y] == a[x][y] - 1):
        return res + searchWay(a, x + 1, y)
    if (a[x][y + 1] == a[x][y] - 1):
        return res + searchWay(a, x, y + 1)
    if (a[x - 1][y] == a[x][y] - 1):
        return res + searchWay(a, x - 1, y)
    if (a[x][y - 1] == a[x][y] - 1):
        return res + searchWay(a, x, y - 1)

    return res

# движение по лабиринту
def move(a, x, y, number):

    a[x][y] = number

    if (a[x + 1][y] == 0):
        move(a, x + 1, y, number + 1)
    if (a[x][y + 1] == 0):
        move(a, x, y + 1, number + 1)
    if (a[x - 1][y] == 0):
        move(a, x - 1, y, number + 1)
    if (a[x][y - 1] == 0):
        move(a, x, y - 1, number + 1)

map = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
       [-1,  1, -1,  0,  0,  0, -1,  0,  0,  0, -1],
       [-1,  0,  0,  0, -1,  0, -1,  0, -1,  0, -1],
       [-1,  0, -1,  0, -1,  0,  0,  0, -1,  0, -1],
       [-1,  0, -1,  0, -1, -1, -1, -1, -1,  0, -1],
       [-1,  0, -1,  0,  0,  0,  0,  0, -1,  0, -1],
       [-1,  0, -1, -1, -1, -1, -1, -1, -1,  0, -1],
       [-1,  0,  0,  0,  0,  0,  0,  0, -1,  0, -1],
       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

start = searchCoordIndex(1)     # 1 - старт
finish = [7, 9]  # F - финиш

wall = '|||'
path = '   '
print('Лабиринт до:')
printLab()

move(map, start[0], start[1], map[start[0]][start[1]])

print('Лабиринт после:')
printLab()
print(f'Выход найден\nМинимальное количество ходов, для достижения выхода = {map[7][9]}')

road = searchWay(map, finish[0], finish[1])
road.reverse()
print('Координаты пути:')
for i in road:
    print(i)
