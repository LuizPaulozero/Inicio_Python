nome = str(input('Digite seu nome: '))
nome = nome.strip()
upper = nome.upper()
lower = nome.lower()
split = nome.split()
conta = len(nome) - nome.count(' ')
total_1palavra = len(split[0])

print('Em maiúsculo: {} \nEm minúsculo: {} \nTotal letras: {} \nTotal de letras na primeira palavra:{}'.format(upper, lower, conta, total_1palavra))