#import Шифрование

def openFile(filename):
    ret = ''

    try:
        f = open(filename, 'r', encoding='UTF-8')

        for line in f.readlines():
            ret += line

        f.close()

    except:
        input('Файл не найден. Создайте зашифрованный файл.')
#Если файла с зашифрованным текстом нет, импортируется и выполняется код из "Шифрование"
        import Шифрование
#Замет снова вызывается метод открытия файла, т.к. в этот раз файл уже должен быть создан
        ret = openFile(filename)

    return ret

def saveFile(text ,filename):
    try:
        f = open(filename, 'w', encoding='UTF-8')
        f.write(text)
        f.close()
    except:
        print('Ошибка создания файла.')


SHstroka = openFile('crypt.txt')
stroka = ''

# шифрование с добавлением к коду символа числа от 1 до 9
code = 1
for i in SHstroka:
    stroka += chr(ord(i) - (code % 10))
    code += 1

print(f'Строка, которую нужно расшифровать: {SHstroka}')
print(f'Расшифрованная строка: {stroka}')

saveFile(stroka, 'encrypt.txt')
