
count = 0
n = 100 # диапазон проверки чисел на простоту
x = [i for i in range(n)]
y = []

for i in x:
    exam = False
    for j in range(2, i):
        count += 1
        if (i % j == 0):
            exam = True
    if not exam:
        y.append(i)

print(f'Список простых чисел в диапазоне от 0 до {n} - {y}')
print(f'Количество проверок - {count}')
