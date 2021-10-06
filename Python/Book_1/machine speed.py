#autoCount = int(input('Enter the number of drivers: '))

speed = int(0)

while (speed != 1000):
    speed = int(input('Enter the speed auto = '))

    if (speed != 1000):
        if (0 < speed < 60):
            print ('Correct speed.')
        elif (speed == 0):
            print('Auto stopped.')
        elif (60 < speed <= 200):
            print('Violation speed!')
        elif (speed < 0 or speed > 200):
            print('Uncorrect speed!')

print ('Thank you! Bye.')
