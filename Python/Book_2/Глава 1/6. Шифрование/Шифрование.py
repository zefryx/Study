import random
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
def cryptCesar(text):
    ret = ''

    count = 1
    for i in text:
        ret += chr(ord(i) + (count % 10))
        count += 1

    return ret
#шифрование с использованием метода перестановки
def cryptTransp(text, key):
    ret = ''
    lenKey = len(key)
    #добавление недостащих символов
    ostatok = lenKey - len(text) % lenKey
    if (len(text) % lenKey != 0):
        text += '_'
        for p in range(ostatok - 1):
            text += chr(random.randint(ord('!'), ord('=')))

    #шифрование / расшифрование
    count = 0
    for i in range(int(len(text)/lenKey)):
    	for j in key:
    		ret += text[(j -1) + count]
    	count += lenKey

    return ret
#проверка на то, что ввели число
def isDigit(text, exam = False, lenKey = None):
    num = ''
    TRUE = False
    while(not num.isdigit() or '0' in num or int(num) < 2 or TRUE):
        num = input(text)
        if (not num.isdigit() or '0' in num or int(num) < 2):
            print(f'Вы ввели {num}. Это не соответствует критериям вводных данных.')
        else:
            ex = True
        #при вводе ключа запускается блок проверки соответствия ключа требованиям
        if (exam and ex):
            TRUE = proverka(num, text, lenKey)

    num = int(num)
    return num
#проверка ключа на соответствие критериям
def proverka(num, text, lenKey = None):
    exam = False
    #проверка длины ключа
    if (len(str(num)) < lenKey):
        print('Недопустимый размер ключа.')
        exam = True
    #проверка, что в ключе только символы из диапазона
    ii = 0
    while (not exam and ii < lenKey):
        i = ''
        i = str(num)[ii]
        if (int(i) > lenKey or int(i) < 0):
            print('Недопустимый символ в ключе.')
            exam = True
        ii += 1
    #проверка, что в ключе нет повторяющихся символов
    keyList = []
    keyList.extend(str(num))
    j = 1
    while (not exam and j < (lenKey + 1)):
        x = keyList.count(str(j))
        if (x != 1):
            print('Недопустимые повторы в ключе.')
            exam = True
        j += 1
    #если что-то не так, запрашивает ключ заного
    if exam:
        return True
    #если все хорошо возвращает истину
    return False

cryptKey = []
unCryptKey = []

lenKey = isDigit('Введите длину ключа шифрования (от 2 до ~): ')
cryptKeyStr = str(isDigit(f'Введите ключ шифрования, используя цифры от 1 до {lenKey} без повторов: ', True, lenKey))

for i in cryptKeyStr:       #записывает в список ЧИСЛА
    cryptKey.append(int(i))

for i in range(len(cryptKey)):      #создает ключ для расшифрования
    ucKcount = cryptKey.index(i+1) + 1
    unCryptKey.append(ucKcount)

print('Ключ шифрования: ', cryptKey)
print('Ключ расшифрования: ', unCryptKey)

stroka = openFile('forcrypt.txt')
#SHstroka = cryptCesar(stroka) # шифр цезаря
SHstroka = cryptTransp(stroka, cryptKey) # шифрование перестановкой

print(f'Строка, которую нужно зашифровать: {stroka}')
print(f'Зашифрованная строка: {SHstroka}')

saveFile(SHstroka, 'crypt.txt')
