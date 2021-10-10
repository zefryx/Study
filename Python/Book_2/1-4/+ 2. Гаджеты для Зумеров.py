import random

def printList2D(list, joob):
    for i in range(len(list)):
        print('  ', joob[i+1], ' - ', end = ' ')
        for j in range(len(list[i])):
            print(f'{list[i][j]} ', end='')
        print()

a = []

job = [i for i in range (71)]

n = 70 #Количество человек
m = 12 #Количество месяцев
zp = 0 #Средняя зарплата за год
zp1 = 0 #Средняя зарплата сотрудника за год
count = 0 #Счетчик сколько человек получили ЗП больше средней

print()

for i in range (n):
    a.append([])
    for j in range (m):
        x = random.randint(25000,150000)
        a[i].append(x)
        zp += a[i][j]

zp = round(zp / n)

for i in range (n):
    zp1 = 0
    for j in range (m):
        zp1 += a[i][j]
        if (zp1 > zp and j == m-1):
            count += 1

printList2D(a, job)
print(f'\n \n  Средняя зарплата за год равна: {zp} \n ')
print(f'  Количество сотрудников, получивших ЗП выше средней равно: {count}')

####################################
'''
b = sum(a, [])
bb = sum(b,0)
#print (bb)
zpp = round(bb / n)
print(f'\n \n  Средняя зарплата за год равна: {zpp} \n ')
'''
#####################################

input()
