
# быстрая сортировка
def qsort1(list):
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
        return qsort1(sp1) + sp2 + qsort1(sp3)
    else:
        return list
# быстрая сортировка методом
def qsort2(b, start, stop):

    if (start >= stop):
        return
    else:
        avr = sum(b[start:stop]) // (stop - start)   # через среднего арифметическое
        #avr = a[start + (stop - start) // 2]         # через центральный элемент списка

        first = start
        last = stop

        while (first <= last):
            # поиск элемента больше среднего с начала списка
            while (b[first] > avr): # сортировка по возрастанию < или убыванию >
                first += 1
            # поиск элемента больше среднего с конца списка
            while (b[last] < avr): # сортировка по возрастанию > или убыванию <
                last -= 1
            # меняем местами элементы
            if (first <= last):
                b[first], b[last] = b[last], b[first]
                first += 1
                last -= 1
                sch2[0] += 1

        qsort2(b, start, last)
        qsort2(b, first, stop)

sch = [0]
sch2 = [0]

#a = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
b = a.copy()

print(f'Список до сортировки                   - {a}')
print (f'Список после сортировки пузырьком      - {qsort1(a)}, количество итераций - {sch}')
qsort2(b, 0, len(b) - 1)
print (f'Список после сортировки пузырьком      - {b}, количество итераций - {sch2}')
