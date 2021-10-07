import random

#расшифровка комманд
def decode(s):
	dcd = ''
	for i in s:
		if(ord(i) in codeList):
			dcd += i
	return dcd

code = 'WSADE0123'
codeList = []
for i in range(len(code)):
	codeList.append(ord(code[i]))

command = input('Введите команды Копатыча: ')
dCommand = ''
dCommList = []
clCommand = []
txt = ''
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

#выбор команды для использования
txt = clCommand[0] 

for i in range(len(clCommand)-1):
	i += 1
	if(len(txt) > len(clCommand[i])):
		txt = clCommand[i]
		
print(f'\nВыбранная для исполнения команда: ', txt)
input()
