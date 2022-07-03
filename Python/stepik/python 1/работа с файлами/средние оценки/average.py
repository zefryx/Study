#text = []
ans = []
ma, fy, ru = 0, 0, 0

with open('dataset_3363_4.txt', 'r', encoding='utf-8') as txt:
    for line in txt.readlines():
        #text += line.strip().split(';')
        text = line.strip().split(';')

        ma += int(text[1])
        fy += int(text[2])
        ru += int(text[3])

        avr = ( int(text[1]) + int(text[2]) + int(text[3]) ) / 3

        ans.append(round(avr, 9))

ans.append(f'{round(ma / len(ans), 9)} {round(fy / len(ans), 9)} {round(ru / len(ans), 9)}')

for i in ans:
    print(i)

with open('ansver.txt', 'w') as txt:
    for line in ans:
        txt.write(str(line) + '\n')
