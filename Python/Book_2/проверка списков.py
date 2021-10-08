#печатает список по строкам
def printList2D(list):
    for i in range(len(list)):
        print(end='  ')
        for j in range(len(list[i])):
            print(f'{list[i][j]} ', end='')
        print()

#метод сравнения символов списков,
#сравнивает символы одного списка с символами других
def compList(s):
    print(s)
    for j in range(len(s[0])-1):  #главный цикл метода
        print('j',j)
        print('s[0]', s[0])
        cmm = s[0][j]   #переменная, в которой находится символ 1 списка
        nes = 0         #счетчик количество несовпадений при сравнении
#        ex = False      #если True - n'ые символы всех списков равны

#        k = len(s) - 1       #Выбирает последний список, для сравнения с первым

        for o in range(1, len(s)):

            for i in range(len(s[o])):     #помещаем в i поочередно все символы списка o от j до последнего
                q = s[o][i]
                print('cmm',cmm)
                print('q',q)
                if (cmm == q):              #сравнивает символ списка 0 с символом списка k
                    print('nes',nes)
                    if (nes != 0):          #удаляет из списка o символы,
                        print('nes1',nes)
                        for p in range(nes-j):#которые были до первого совпадения
                            print('p',p)
                            s[o].pop(j)     #

                    print('nes2',nes)
#                    ex = compList(s[j:o])     #если совпадают, сравнивает этот же символ со следующим списком
                    nes = 0                 #сбрасывает счетчик ошибок
                    break
                else:           #если символы не совпадают
                    if (nes != (len(s[o]) - 1)):    #проверяет, совпал ли символ cmm хоть с одним символом списка k
                        nes += 1                    # если совпал, то nes += 1
                        print('nes3',nes)
                        print('len[s0]-1',len(s[0])-1)
                    else:                       #если не совпал, удаляет символ cmm и загружает в переменную следующий из s[0]
                        if (i != len(s[0])):
                            s[0].pop(j)
                            cmm = s[0][j]
                            nes = 0
                            qwer = j

#                if ex:  #if (k+1 != len(s) and nes == 0):
#                    return True

    printList2D(s)



a = [[1,2,2,4],
     [1,3,4],
     [1,3,4]]

printList2D(a)
print()
compList(a)

input()
