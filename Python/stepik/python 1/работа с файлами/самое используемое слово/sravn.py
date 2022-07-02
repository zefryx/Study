'''
s, d, m, w = str(), dict(), 0, str()
with open("dataset_3363_3.txt", "r", encoding='utf-8') as f:
    s = f.read().lower().strip().split()
s.sort()
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    if d[word] > m:
        m = d[word]
        w = word
print(w, m)
'''
'''
ans = ['', 0]
word = {}
text = ''

with open('dataset_3363_3.txt', encoding='utf-8') as txt:
    for line in txt.readlines():
        text += line.strip() + ' '
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
            ans[0] = text_copy[text.index(i)]

print(ans[0], ans[1])

with open('answer.txt', 'w') as txt:
    txt.write(f'{ans[0]} {ans[1]}')
'''

w, c = '', 0
words = {}

with open('dataset_3363_3.txt', encoding='utf-8') as txt:
    text = txt.read().strip().split()

for word in text:
    if word.lower() in words:
        words[word.lower()] += 1
    else:
        words[word.lower()] = 1

    if words[word.lower()] > c:
        c = words[word.lower()]
        w = word
    elif c == words[word.lower()]:
        if word.lower() < w:
            w = word.lower()

print(w, c)

with open('answer.txt', 'w') as txt:
    txt.write(f'{c} {w}')
