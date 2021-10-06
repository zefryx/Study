how = int(input('''How many numbers do you want to check?
'''))

for i in range (how):
    x = int(input('Enter the number: '))
    if (x%2 == 0):
        print (x, '- even.')
    else:
        print (x, '- odd.', 'Remainder =', x%2)
