'''Программа "Учимся считать"
начало 25.09.2020 19:20'''

import random

x = 0           #число 1
y = 0           #число 2
z = 0           #результат операции
result = ''     #результат, который вводит игрок

diff = ''   #уровень сложности примеров (1, 2, 3)
game = True     #играем дальше или не играем
qua = ''        #для сравнения с game и окончания игры
score = 0       #количество набранных очков
count = 0       #количество примеров
right = 0       #количество правильных ответов

minDiap = 1     #минамальная граница диапазона
maxDiap = 99    #верхняя граница диапазона

sign = 0        #знак операции (0 + ; 1 - ; 2 * ; 3 / )

input('''Здравствуй дорогой пользователь.
Перед тобой стоит простая задача - решить показанные примеры и ввести ответ в программу.
При правильном ответе тебе будут начислены очки, при неправильном очки будут списаны.
В программе предусмотрено изменение сложности: 1 - просто, 2 - средне, 3 - сложно.
Для выхода из программы потребуется ввести 'Выход', будет выведена небольшая статистика и программа завершится.

Для продолжения нажми Ввод.
''')

while(not diff.isdigit()):
    diff = input(f'Выберите сложность: 1 - легко, 2 - нормально, 3 - сложно \n')

diff = int(diff)

if(diff == 1):
    maxDiap = 99
elif(diff == 2):
    maxDiap = 999
elif(diff == 3):
    minDiap = -999
    maxDiap = 999

while (game):

    sign = int(random.randint(0,3))                 #генерирует тип операции
    if(sign == 0):
        sign = '+'
    elif(sign == 1):
        sign = '-'
    elif(sign == 2):
        sign = '*'
    elif(sign == 3):
        sign = '/'

#блок генерации чисел для суммы (результат не больше 99)
    if(sign == '+'):
        z = random.randint(minDiap + 1, maxDiap)    #генерируется результат Z
        x = random.randint(minDiap, z - 1)          #генерируется число Х
        y = z - x                                   #вычисляется число Y
#блок генерации чисел для разности (результат не меньше 0)
    elif(sign == '-'):
        z = random.randint(minDiap, maxDiap - 1)    #генерируется результат Z
        x = random.randint(z + 1, maxDiap)          #генерируется число Х
        y = x - z                                   #генерируется число Y
#блок генерации чисел для умножения (результат не больше 99)
    elif(sign == '*'):
        x = random.randint(minDiap, maxDiap // 2 )  #генерируется число Х
        y = random.randint(minDiap, maxDiap // x)   #генерируется число Y
        z = x * y                                   #вычисляется результат Z
#блок генерации чисел для деления (результат не меньше 0)
    elif(sign == '/'):
        z = random.randint(minDiap + 1, maxDiap // 4 + 1)   #генерируется результат Z
        y = random.randint(minDiap+1, maxDiap // z)         #генерируется число Y
        x = y * z                                           #вычисляется число X

    result = str(input(f'Решите данный пример: {x} {sign} {y} = '))

    while(not result.isdigit()
          and result.upper() != 'ВЫХОД'
          and result.upper() != 'STOP'):

        if(result.upper() == 'HELP'
           or result.upper() == 'H'
           or result.upper() == '?'):
            result = ''
            if (z > 9):
                print(f'Последняя цифра ответа {z % 10}.')
            else:
                print('Ответ меньше 10.')
            score -= 10
            if(score < 0):
                score = 0
        elif(not result[1:].isdigit()):
            result = input(f'Введено {result}, это не число. Нужно ввести число.')
        elif(abs(int(result)) > 0):
            break

    if(result.upper() == 'ВЫХОД' or result.upper() == 'STOP'):
        game = False

    if(game == True):
        if(int(result) == int(z)):
            score += 10
            right += 1
            count +=1
            qua = input(f'Правильно! Набрано {score} очков. Продолжим? ')

            if(qua.upper() == 'ВЫХОД' or qua.upper() == 'STOP'):
                game = False

        else:
            score -= 10
            count +=1
            if(score < 0):
                score = 0
            qua = input(f'\nНеравильно! Ответ {z}. Набрано {score} очков. Продолжим? ')

            if(qua.upper() == 'ВЫХОД' or qua.upper() == 'STOP'):
                game = False

print(f'\nСпасибо за игру! Вы набрали {score} очков и решили {right} из {count} примеров. До встречи.')
if(count > 0):
    print(f'Процент правильных ответов {count / right * 100}%')
else:
    print(f'Процент правильных ответов 0%')
