import requests

with open('dataset_3378_2.txt', 'r', encoding='utf-8') as txt:
    url_adress = txt.readline().strip()

r = requests.get(url_adress)

ans = r.text.splitlines(keepends=True)

print(len(ans))

with open('ansver.txt', 'w', encoding='utf-8') as txt:
    for i in ans:
        txt.write(i)
