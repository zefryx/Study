def fact(x):
    if (x == 1):
        return 1
    x = x * fact(x - 1)
    return x


n = 5
print(f'Fact {n} = ', fact(n))
