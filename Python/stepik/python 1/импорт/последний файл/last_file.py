import requests

check = False

with open('dataset_3378_3.txt', 'r', encoding='utf-8') as txt:
    url_list = txt.readline().strip().split('/')
    url_name = url_list[-1]
    url_list[-1] = ''
    url_link = '/'.join(url_list)


while check == False:

    url_address = url_link + url_name
    r = requests.get(url_address)
    print(r.text)

    if r.text[0:2] == 'We':
        check = True
    else:
        url_name = r.text.strip()

with open('answer.txt', 'w', encoding='utf-8') as txt:
    txt.write(r.text)
