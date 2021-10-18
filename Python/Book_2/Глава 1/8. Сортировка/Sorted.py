a = ['Стол','Стул','Яблоко','Москва','Молоко','Черешня', 'Ананас', 'Апельсин']

print(f'Список до сортировки                   - {a}')
print('Сортировка sorted через цикл for       - ', end='')
for i in sorted(a, reverse = True):
    print(i, '', end='')
print()
print(f'Список после сортировки sorted         - {sorted(a, reverse = True)}')
print(f'Исходный список                        - {a}')
