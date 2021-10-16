# сортировка пузырьком
def puzir(list):
    count = 0
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if (list[j] < list[j + 1]): # сортировка по возрастанию или убыванию
                list[j], list[j + 1] = list[j + 1], list[j]
                count += 1
    return f'{list}, количество итераций - {count}'

# сортировка перестановками
def perestan(list):
    count = 0
    for i in range(1, len(list)):
        per = list[i]
        j = i - 1
        while (j >= 0 and list[j] < per): # сортировка по возрастанию или убыванию
            list[j + 1] = list[j]
            j -= 1
            count += 1
        list[j + 1] = per
    return f'{list}, количество итераций - {count}'

# быстрая сортировка
def qsort(list):
    if (len(list) == 2):
        if (list[0] <  list[1]): # сортировка по возрастанию > или убыванию <
            list[0], list[1] = list[1], list[0]
        sch[0] += 1
        return list
    elif(len(list) > 2):
        avr = sum(list) // len(list)
        sp1 = []
        sp2 = []
        sp3 = []
        for i in list:
            if (i > avr):   # сортировка по возрастанию < или убыванию >
                sp1.append(i)
            elif (i < avr): # сортировка по возрастанию > или убыванию <
                sp3.append(i)
            else:
                sp2.append(i)
            sch[0] += 1
        return qsort(sp1) + sp2 + qsort(sp3)
    else:
        return list

#a2 = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16]]
sch = [0]
a2 = [[16, 15, 14, 13],
      [12, 11, 10, 9],
      [8, 7, 6, 5],
      [4, 3, 2, 1]]
#a = [5, 4, 3, 2, 1]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b, c, d = a.copy(), a.copy()

print(f'Список до сортировки                   - {a}')
print (f'Список после сортировки пузырьком      - {puzir(a)}')
print (f'Список после сортировки перестановками - {perestan(b)}')
print (f'Список после быстрой сортировки        - {qsort(c)}, количество итераций - {sch[0]}')
