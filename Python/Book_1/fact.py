def fact(a):
    if (a == 0):
        return 1
    F = a * fact(a-1)
    return F
x = int(input('Введите число: '))
FF = fact(x)
print(FF)
