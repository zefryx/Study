# сортировка пузырьком
def puzir(list):
    count = 0
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if (list[j] < list[j + 1]): # сортировка по возрастанию или убыванию
                list[j], list[j + 1] = list[j + 1], list[j]
                count += 1
    return list
# сортировка через объединение вложенных списков в один
def sort2D1(list):
    tmp = []
    ret = []
    count = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            tmp.append(list[i][j])

    tmp = puzir(tmp)

    for i in range(len(list)):
        ret.append([])
        for j in range(len(list[i])):
            ret[i].append(tmp[count])
            count += 1
    return ret

# получение координат списка
def coord(list):
    ret = []
    for i in range(len(list)):
        for j in range(len(list[i])):
            ret.append([])
            ret[(i * len(list) + j)].append(i)
            ret[(i * len(list) + j)].append(j)
    return ret
# сортировка через список с адресами
def sort2D2(list):
    ind = coord(list)
    ret = []
    count = 0

    for i in range(len(ind) - 1):
        for j in range(len(ind) - 1 - i):
            if (list[ind[j][0]][ind[j][1]] < \
                list[ind[j + 1][0]][ind[j + 1][1]]): # сортировка по возрастанию > или убыванию <

                list[ind[j][0]][ind[j][1]], list[ind[j + 1][0]][ind[j + 1][1]] = \
                list[ind[j + 1][0]][ind[j + 1][1]], list[ind[j][0]][ind[j][1]]

                count += 1
    return list

a = [[1, 5, 9, 13],
      [2, 6, 10, 14],
      [3, 7, 11, 15],
      [4, 8, 12, 16]]

print(f'Список до сортировки                   - {a}')
print (f'Список после сортировки пузырьком      - {sort2D2(a)}')
