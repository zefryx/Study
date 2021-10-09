#печатает список по строкам
def printList2D(list):
    for i in range(len(list)):
        print(end='  ')
        for j in range(len(list[i])):
            print(f'{list[i][j]} ', end='')
        print()
