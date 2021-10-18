import random
# возвращает введенное число в список, исключая начальные нули
def createData(a):
	digit = []
	i = len(a) - 1

	while (a[i] >= 0 and a[i] == 0):
		i -= 1

	if (i == -1):
		return 0
	else:
		while(i >= 0):
			digit.append(int(alphabet(a[i])))
			i -= 1

	return digit

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

# преобразование чисел в 10-чную систему
def getData(a, base):
	d = 0
	for i in range(len(a)):
		d += a[i] * base ** i
	return d

# суммирует длинные числа
def sumDigit(a, b, base):
		i = 0
		razr = [0, 0]

		while (i < len(a) + 1 or i < len(b) + 1):
			x, y= 0, 0

			try:
				x = a[i]
			except:
				x = 0
			try:
				y = b[i]
			except:
				y = 0

			summ = x + y + razr[i]
			if summ >= base:
				summ -= base
				razr[i + 1] = 1
			summDigit.append(summ)
			razr.append(0)
			i += 1

alphabet = ''
alphabet += '0123456789'
alphabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet += 'abcdefghijklmnopqrstuvwxyz'
alphabet += 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet += 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# основание
base = 2
# длина чисел
n = 100

longDigit1 = [random.randint(0, base - 1) for i in range(n)]
longDigit2 = [random.randint(0, base - 1) for i in range(n)]

summDigit = []
sumDigit(longDigit1, longDigit2, base)

print(f'Число 1 в системе счисления {base}: ', end = '')
printData(longDigit1)
print(f'Число 2 в системе счисления {base}: ', end = '')
printData(longDigit2)
print('Сумма чисел равна = ', end = '')
printData(summDigit)
print(f'Число {summDigit} в системе счисления {base} равно {getData(longDigit1, base)} в 10-тичной системе счисления')
