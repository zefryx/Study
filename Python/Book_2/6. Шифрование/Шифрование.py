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

def saveFile(text ,filename):
    try:
        f = open(filename, 'w', encoding='UTF-8')
        f.write(text)
        f.close()
    except:
        print('Ошибка создания файла.')


stroka = openFile('forcrypt.txt')
SHstroka = ''

# шифрование с добавлением к коду символа числа от 1 до 9
code = 1
for i in stroka:
    SHstroka += chr(ord(i) + (code % 10))
    code += 1

print(f'Строка, которую нужно зашифровать: {stroka}')
print(f'Зашифрованная строка: {SHstroka}')

saveFile(SHstroka, 'crypt.txt')

input()
