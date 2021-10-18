
def createData(a):
	digit = []
	for i in range(len(a)):
		digit.append(int(a[len(a) - 1 - i]))
	return digit

def getData(a):
	digit = 0
	for i in range (len(a)):
		digit += a[i] * 10 ** i
	return digit

def sumDigit(a, b):
		i = 0
		razr = [0, 0]
		summa = []
		
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
				
			summ = x + y
			if summ > 9:
				summ -= 10
				razr[i + 1] = 1
				
			summa.append(summ + razr[i])
			
			razr.append(0)
			i += 1
				
		return summa
		
strDigit1 = input('Введите первое число: ')
strDigit2 = input('Введите второе число: ')

longDigit1 = createData(strDigit1)
longDigit2 = createData(strDigit2)

print(f'Число 1 : {getData(longDigit1)} \nЧисло 2 : {getData(longDigit2)}')

print(f'\nСумма чисел равна = {getData(sumDigit(longDigit1, longDigit2))}')
