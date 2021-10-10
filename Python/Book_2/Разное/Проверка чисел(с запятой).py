
# Код для проверки, является ли строка числом
def isDigit(s): #Проверяет является ли строка числом
    startCode = ord('0') #Диапазон проверки для цифр от 0
    stopCode = ord('9') # до 9
    res = True #если False то не число
    tka = False

    p = 0 #счетчик while
    while(p < len(s) and res):
        if(ord(s[p]) == ord('.') and not tka):
            tka = True
        elif(ord(s[p]) < startCode or ord(s[p]) > stopCode):
            res = False
        p += 1
    return res

x = '114.445.345'
print(isDigit(x))

input()
