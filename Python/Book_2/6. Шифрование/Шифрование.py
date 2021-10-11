# открывает или создает файл
def openFile(filename):
    ret = ''

    try:
        f = open(filename, 'r', encoding='UTF-8')

        for line in f.readlines():
            ret += line

        f.close()

    except:
        ret = input('Файл не найден. Введите текст, для записи в новый файл: ')
        saveFile(ret, filename)

    return ret
# сохраняет файл
def saveFile(text ,filename):
    try:
        f = open(filename, 'w', encoding='UTF-8')
        f.write(text)
        f.close()
    except:
        print('Ошибка создания файла.')
# шифрование с добавлением к коду символа числа от 1 до 9
def cryptCesar(line):
    ret = ''

    count = 1
    for i in line:
        ret += chr(ord(i) + (count % 10))
        count += 1

    return ret
#шифрование с использованием метода перестановки
def cryptTransp(line, code):
    return 0
#проверка на то, что ввели число
def isDigit(text):
    num = ''
    while(not num.isdigit() or '0' in num):
        num = input(text)
        if (not num.isdigit() or '0' in num):
            print(f'Вы ввели {num}. Это какой-то сучий текст! {text}')
    num = int(num)

    return num

stroka = openFile('forcrypt.txt')

'''
добавить в isDigit необязательный параметр [, res]
для проверки шифра, цифры не повторяются и лежат в диапазоне

lenKey = isDigit('Введите длину ключа шифрования: ')
cryptKeyStr = str(isDigit(f'Введите ключ шифрования, используя цифры от 1 до {lenKey} без повторов: '))

cryptKey = []
unCryptKey = []

for j in cryptKeyStr:       #записывает в список ЧИСЛА
    cryptKey.append(int(j))

for i in range(len(cryptKey)):      #делает ключ для расшифрования
    adda = cryptKey.index(i+1) + 1
    unCryptKey.append(adda)


text = "Hello world."
crText = ""
unCrText = ""

count = 0
cryptKey = [3, 5, 1, 4, 6, 2]
unCryptKey = [3, 6, 1, 4, 2, 5]

for j in range(1, round(len(text)/len(cryptKey))+1):
	for i in cryptKey:
		crText += text[(i -1) + count]
	count += 6

count = 0

for j in range(1, round(len(crText)/len(unCryptKey))+1):
	for i in unCryptKey:
		unCrText += crText[(i -1) + count]
	count += 6

print(text)	
print(crText)
print(unCrText)


def isDigit(text, res = False):
    
    num = ''
    while(not num.isdigit() or '0' in num):
        num = input(text)
        if (not num.isdigit() or '0' in num):
            print(f'Вы ввели {num}. Это какой-то сучий текст! {text}')
    num = int(num)
    
    if res:
    	if (proverka(num, text)):
    
   		 return num

def proverka(x, text):
	
	for i in str(x):
		if (int(i) > y or int(i) < 0):
			print('Неправильно')
			isDigit(text, True)
	return True
		
y = 3

x = isDigit(f'Введите числа от 1 до {y} : ', True)

print(x)
		
	
'''

cryptKey = [3,5,1,6,4,2]
unCryptKey = [3,6,1,5,2,4]
SHstroka = cryptCesar(stroka)


print(f'Строка, которую нужно зашифровать: {stroka}')
print(f'Зашифрованная строка: {SHstroka}')

saveFile(SHstroka, 'crypt.txt')
