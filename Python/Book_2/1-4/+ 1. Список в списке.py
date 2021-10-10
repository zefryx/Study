import random

def printList2D(list):
    for i in range(len(list)):
        print(end='  ')
        for j in range(len(list[i])):
            print(f'{list[i][j]} ', end='')
        print()

a = []

n = 5
m = 9

print()

for i in range (n):
    a.append([])
    for j in range (m):
        x = random.randint(10,99)
        a[i].append(x)

printList2D(a)

mx = 0
mn = 99

for i in range (n):
    for j in range (m):
        if (mx < a[i][j]):
            mx = a[i][j]
        if (mn > a[i][j]):
            mn = a[i][j]

print(f'\n \n  Максимальный элемент списка: {mx} \n  Минимальный элемент списка: {mn}')

#b = sum(a, [])
#print (b)
#mx = max(b)
#mn = min(b)
#print(f'\n \n  Максимальный элемент списка: {mx} \n  Минимальный элемент списка: {mn}')

input()
