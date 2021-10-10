#печатает список по строкам
def printList2D(list):
    for i in range(len(list)):
        print(end='  ')
        for j in range(len(list[i])):
            print(f'{list[i][j]} ', end='')
        print('  Средний балл: ', getAverage(list[i]))

#считывает данные с файла построчно и выдает в виде списка
def getFileString(filename):
    ret = []

    try:
        f = open(filename, 'r', encoding='utf-8')

        for line in f.readlines():
            line = line.replace('\n', '')
            line = line.split('#')
            ret.append(line)

        f.close()
    except:
        print('Ошибка открытия файла! Проверьте правильность имени и пути.')
    return ret

#считает средне-арифметическое из списка
def getAverage(line):
    avr = 0
    count = 0
    summ = 0

    for i in range(1, len(line)):
        if (line[i].isdigit()):
            summ += int(line[i])
            count += 1

    avr = summ / count
    avr = int(avr * 10) / 10

    return avr

#подготовка данных для записи в файл
def getStringToFile(arr):
    ret = ''

    for i in range(len(arr)):
        ret += arr[i][0] + '#' + str(getAverage(arr[i])) + '\n'

    return ret

#записвает переданную информацию в файл
def saveToFile(strToFile, filename):

    try:
        f = open(filename, 'w', encoding='UTF-8')
        f.write(strToFile)
        f.close()
    except:
        print('Ошибка создания файла.')

journal = getFileString('journal.dat')

print('Оценки учеников:')
printList2D(journal)
print()

for i in range(len(journal)):
    print(f'{journal[i][0]}, средний балл: {getAverage(journal[i])}')

saveToFile(getStringToFile(journal), 'average.dat')

input()
