def fib(x, y, i):
    print(y)
    if (i < n - 2):
        i += 1
        y += fib(y, x + y, i)
    return y


n = 10
print('0')
print('Summ = ', fib(0, 1, 0))
