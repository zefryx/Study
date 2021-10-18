
# печатает число из списка
def printData(a):
	i = len(a) - 1
	while (i >= 0 and a[i] == 0):
		i -= 1

	if (i == -1):
		return 0
	else:
		while(i >= 0):
			print(alphabet[a[i]], end='')
			i -= 1
		print()

# перевод чисел в 10-чную систему
def getData(a, base):
	d = 0
	for i in range(len(a)):
		d += a[i] * base ** i
	return d

# перевод из 10-тичной в другую сс
def perevod(a, base):
    ost = 0
    b = getData(a, 10)
    c = []

    while (b > 0):
        c.append(b % base)
        b //= base

    return c

alphabet = '0123456789ABCDEF'

base1 = 2
base2 = 10

digit1 = [1, 1, 1, 1, 1]
digit2 = [1, 3]

digit3 = perevod(digit2, 16)

printData(digit1)
printData(digit2)
printData(digit3)
