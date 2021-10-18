def inverse(list):
    Len = len(list)
    for i in range(Len // 2):
        list[i], list[Len - 1 - i] = list[Len - 1 - i], list[i]
    return list
    
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a.copy()

print(f'Список до инверсии    - {a}')
print(f'Список после инверсии - {inverse(b)}')
