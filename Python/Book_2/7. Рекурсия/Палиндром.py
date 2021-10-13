def palin(text):
    size = len(text)
    if (size < 2):
        return 'палиндром'
    if (text[0] == text[size - 1]):
        palin(text[1: size - 1])
        return 'палиндром'
    else:
        return 'не палиндром'


slovo = 'крыша'
print(f'Слово {slovo} {palin(slovo.upper())}.')
