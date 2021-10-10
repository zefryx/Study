import random

txt = 'Привет! Как дела?'
toWord = 'ВГ ДЕЁЖЗ ИЙКЛМН ОПРСТУ ФХЦ ЧШЩЬЫЪЭЮ Яабв геёжзи йкл мно прсту фхцчшщ ьыъ эюя'
#tx = []
ctxt = ''
dtxt = ''
o = 0

#tx.extend(txt)

for i in range (len(txt)):
    x = random.randint(1, 5)

    for j in range(x):
        y = random.randint(0, len(toWord)-1)
        ctxt += toWord[j]

    ctxt += chr(random.randint(ord('А'),ord('Б'))) + txt[i] #случайный символ А или Б + символ из сообщения txt
#    tx.insert(i+i, chr(random.randint(ord('А'),ord('Б'))))
#    ctxt += tx[i+i] + tx[i+i+1]  Это то же, только с использованием списка

while (o < len(ctxt)-1):
    if (ctxt[o] == 'А' or ctxt[o] == 'Б'):
        dtxt += ctxt[o+1]
        o += 2
    else:
        o += 1

print(txt)
#print(tx)
print(ctxt, '\n')

print(dtxt)

input()
