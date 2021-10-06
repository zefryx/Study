from random import randint
import time

sit01 = 0   #что делает лошадка 0 - вперед, 1 - стоит, 2- назад, 3 - буст
sit = 0     #что произойдет с лошадкой 1 - встанет, 2 - назад, 3 - буст
boost = ''
state01 = randint(1, 5)

for i in range (10):

    def problem():
        global sit, sit01, boost

        j = 0

        maxRand = 15

        if(randint(0, maxRand) < 10):
            sit = randint(1, 3)

        if(sit01 != 1):

            if(randint(0, maxRand) < state01 * 5 and sit == 1):
                print('лошадка скинула жокея и стоит')
                sit01 = 1
            elif(randint(0, maxRand) < state01 * 5 and sit == 2):
                print('лошадка бежит обратно')
                sit01 = 2

            if(boost == '' or not '1' in boost):
                if(randint(0, maxRand) < state01 * 5 and sit == 3):
                    print('лошадка ускорилась')
                    sit01 = 3
                    boost += '1'

    def move():

        if('1' in boost or sit01 == 3):
            print('ускорение')

        if(sit01 != 1):
            if(sit01 != 2):
                print('перемещение вперед')
            else:
                print('перемещение назад')

        problem()

    move()
