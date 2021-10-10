import random

#расшифровка комманд
def decode(s):
	dcd = ''
	for i in s:
		if(ord(i) in codeList):
			dcd += i
	return dcd

#выбор команды для использования
def oneComm(s):
	txt = ''
	txt = s[0]
	for i in range(len(s)-1):
		i += 1
		if(len(txt) > len(s[i])):
			txt = s[i]
	return txt
'''
#сравнение количества команд s - список команд, l - размер списка(количество команд)
def sravn(s, l):
	if(len(s) < 2):
		return True #А вот что вернуть то???
	j = 0
	cmm = ''
	cmm = s[0,j]
	ex = False
	o = 1
	for i in s[o]:
		if(cmm == i):

			ex = sravn(s.pop(o), len(s.pop(o)))

		if(ex):
			j += 1
			cmm = s[0,j]
			ex = False
Сначала сравнить первые символы кодов, если совпадают - сравнить вторые и тд.
Если не совпадают, сравнить первый символ первого кода с остальными символами других кодов.
Если есть совпадения во всех трех символах - начать сравнивать второй, лишние удалить.
Если совпадений нет, удалить этот символ, из первого кода, и сравнивать следующие
'''
code = 'WSADE0123'
codeList = []
for i in range(len(code)):
	codeList.append(ord(code[i]))

command = input('Введите команды Копатыча: ')
dCommand = ''
dCommList = []
clCommand = []

print()

#создание трех отправленных команд
for o in range(3):

	#создание помех в команде
	i = 0
	while (i < (len(command))):
		if(random.randint(0, 0) < 1 and i < (len(command) - 1) ):
			dCommand += command[i]
			i += 1
		for j in range(random.randint(1,5)):
			dCommand += chr(random.randint(65, 122))
		dCommand += command[i]
		i += 1

	dCommList.append(dCommand)
	print(f'Строка с помехами №{o}: {dCommand}')
	dCommand = ''

print()

#расшифровка команды
for i in range(len(dCommList)):
	clCommand.append(decode(dCommList[i]))
	print(f'Очищенная строка №{i}: {clCommand[i]}')

print(f'\nВыбранная для исполнения команда: {oneComm(clCommand)}')
input()
