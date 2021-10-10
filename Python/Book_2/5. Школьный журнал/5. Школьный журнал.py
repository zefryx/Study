#печатает список по строкам
def printList2D(list):
    for i in range(len(list)):
        print(end='  ')
        for j in range(len(list[i])):
            print(f'{list[i][j]} ', end='')
        print()

def getFileString(filename):
    ret = []

    try:
        f = open(filename, 'r', encoding='utf-8')

        for line in f.readlines():
            ret.append(line.replace('\n', ''))

        f.close()
    except:
        print('Ошибка открытия файла! Проверьте правильность имени и пути.')
    return ret

journal = getFileString('journal.dat')

printList2D(journal)

input()
