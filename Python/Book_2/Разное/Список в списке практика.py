import random

def printList2D(list):
    for i in range(len(list)):
        print(end='  ')
        for j in range(len(list[i])):
            print(f'{list[i][j]} ', end='')
        print()

a = []

n = 3
m = 3

print()

'''
for i in range (n):
    a.append([])
    for j in range (m):
        a[i].append(i)
'''
a = [[i for i in range(3)] for j in range(3)]
printList2D(a)

b = a.copy()
b[1].sort(reverse=True)

print()

printList2D(b)

input()
