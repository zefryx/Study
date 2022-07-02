# start
text = ''
ans = ''
count = ''
a = []
b = []

with open('dataset_3363_2.txt') as txt:
    text = txt.readline().strip()

for i in text:
    if i.isdigit():
        count += i
    else:
        a += i
        if count != '':
            b.append(int(count))
            count = ''
b.append(int(count))

for i in range(len(a)):
    ans += a[i]*b[i]

with open('answer.txt', 'w') as ansv:
    ansv.write(ans)
