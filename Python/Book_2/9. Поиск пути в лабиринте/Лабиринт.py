import os
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

# движение вниз
def down():
    map[actPosition[0] + 1][actPosition[1]] += 1 + map[actPosition[0]][actPosition[1]]
    actPosition[0] += 1

# движение вправо
def right():
    map[actPosition[0]][actPosition[1] + 1] += 1 + map[actPosition[0]][actPosition[1]]
    actPosition[1] += 1

# движение вверх
def up():
    map[actPosition[0] - 1][actPosition[1]] += 1 + map[actPosition[0]][actPosition[1]]
    actPosition[0] -= 1

# движение влево
def left():
    map[actPosition[0]][actPosition[1] - 1] += 1 + map[actPosition[0]][actPosition[1]]
    actPosition[1] -= 1

# движение по лабиринту
def move(a, x, y, number):
    return


os.system('cls')                # очистка экрана командной строки

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
actPosition = start

wall = '|||'
path = '   '

printLab()
#move()
printList2D(map)
