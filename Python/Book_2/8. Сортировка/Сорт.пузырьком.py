
# сортировка пузырьком
def puzir(list):
    count = 0
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if (list[j] < list[j + 1]): # сортировка по возрастанию или убыванию
                list[j], list[j + 1] = list[j + 1], list[j]
                count += 1
    return f'{list}, количество итераций - {count}'

#a = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(f'Список до сортировки                   - {a}')
print (f'Список после сортировки пузырьком      - {puzir(a)}')
