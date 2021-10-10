import random

def printList2D(list):
    for i in range(len(list)):
        print(end='  ')
        for j in range(len(list[i])):
            print(f'{list[i][j]} ', end='')
        print()

a = [i for i in range(9999)]
b = [i for i in range(9999)]

x = []
y = []

count = 0

for i in range(len(a)):
    for j in range(len(b)):
        for o in range(4::-1):
            x.append(round((a[i]-x)/10**(o-1)))

        if sum(x) and sum(x)%sum(y) and sum(y):
            count += 1
        x.clear()
        y.clear()
'''
x.extend(str(a[5124]))
xx = sum(int(x))

print(x, xx)

input()
