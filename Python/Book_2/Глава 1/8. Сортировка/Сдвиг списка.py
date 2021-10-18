def sdvig(dir):
    Len = len(a)

    if dir == 'left':
        tmp = a[0]
        for i in range(Len - 1):
            a[i] = a[i + 1]
        a[Len - 1] = tmp
        return a, 'влево'

    elif dir == 'right':
        tmp = a[Len - 1]
        for i in range(Len - 1, 0, -1):
            a[i] = a[i - 1]
        a[0] = tmp
        return a, 'вправо'

    else:
        print('Введены некорректные данные.')
        return 0, 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Список до сдвига    - {a}')

a, side = sdvig('left')

print(f'Список после сдвига {side} - {a[0:5]}')
