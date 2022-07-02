ans = ['', 0]
#word = set()
word = {}
text = ''

with open('dataset_3363_3.txt') as txt:
    for line in txt.readlines():
        text += line.strip() + ' '
        #text = line.strip()
        ##{word.add(i.lower()) for i in text.split()}
        #word.update({i.lower(): None for i in text.split()})
    word.update({i.lower(): None for i in text.split()})
    text_copy = text.split()
    text = text.lower().split()

for i in word:
    count = text.count(i)
    word[i] = count

    if count > ans[1]:
        ans[1] = count
        ans[0] = text_copy[text.index(i)]
    elif count == ans[1]:
        if i < ans[0].lower():
            ans[1] = count
            ans[0] = text_copy[text.index(i)]

print(ans[0], ans[1])

with open('answer.txt', 'w') as txt:
    txt.write(f'{ans[0]} {ans[1]}')
