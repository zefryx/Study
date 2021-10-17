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
    return list, count

# сортировка пузырьком
def puzir(list):
    count = 0
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if (list[j] < list[j + 1]): # сортировка по возрастанию или убыванию
                list[j], list[j + 1] = list[j + 1], list[j]
                count += 1
    return list, count

# сортировка списка с символами
def alph(list):
    code = []
    for i in list:
        code.append(ord(i))
    code, count = puzir(code)
#    code = perestan(code)

    list.clear()

    for i in code:
        list.append(chr(i))

    return f'{list}, количество итераций - {count}'

a = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н']
#a = ['Н', 'М', 'Л', 'К', 'Й', 'И', 'З', 'Ж', 'Е', 'Д', 'Г', 'В', 'Б', 'А']

print(f'Список до сортировки                   - {a}')
print (f'Список после сортировки пузырьком      - {alph(a)}') # тоолько для символов
