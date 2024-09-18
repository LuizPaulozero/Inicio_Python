opcoes = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
while opcoes != 6:
    opcoes = int(input('''Digite o número referente ao que deseja:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] DIVISÃO
    [4] MAIOR ENTRE
    [5] ALTERAR NÚMEROS
    [6] SAIR: '''))
    if opcoes == 1:
        print('A soma entre {} e {} é igual a: {}'.format(num1, num2, num1 + num2))
    if opcoes == 2:
        print('O produto entre {} e {} é igual a: {}'.format(num1, num2, num1 * num2))
    if opcoes == 3:
        print('O quociente entre {} e {} é igual a: {}'.format(num1, num2, num1 / num2))
    if opcoes == 4:
        if num1 > num2:
            print('Entre {} e {} o maior é igual a: {}'.format(num1, num2, num1))
        else:
            print('Entre {} e {} o maior é igual a: {}'.format(num1, num2, num2))
    if opcoes == 5:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    if opcoes == 6:
        print('Obrigado por usar o programa! Tenha um bom dia.')
        