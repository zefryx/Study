month = int(input('Enter the number of days in a month: '))

for i in range (month):
    T = int(input('Enter the temperature for this day: '))
    if (T < -50 or T > 50):
        print('Seriously?! Temperature =', str(T) + '?!')
    elif (-50 <= T < 5):
        print('Day', i+1, 'Cold. Temperature', T)
    elif (5 <= T < 15):
        print('Day', i+1, 'Good. Temperature', T)
    elif (15 <= T < 25):
        print('Day', i+1, 'Nice! Temperature', T)    
    else:
        print('Day', i+1, 'Hot! Temperature', T) 
