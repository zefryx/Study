# открывает или создает файл
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
# сохраняет файл
def saveFile(text ,filename):
    try:
        f = open(filename, 'w', encoding='UTF-8')
        f.write(text)
        f.close()
    except:
        print('Ошибка создания файла.')
# расшифрование с вычитанием из кода символа числа от 1 до 9
def unCryptCesar(line):
    ret = ''

    count = 1
    for i in line:
        ret += chr(ord(i) - (count % 10))
        count += 1

    return ret

SHstroka = openFile('crypt.txt')
stroka = unCryptCesar(SHstroka)



print(f'Строка, которую нужно расшифровать: {SHstroka}')
print(f'Расшифрованная строка: {stroka}')

saveFile(stroka, 'encrypt.txt')
