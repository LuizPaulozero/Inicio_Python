num = int(input('Digite um número: '))
seletor = int(input('Digite 1 caso queira converter de decimal para binário, 2 para octal ou 3 para hexadecimal: '))
if seletor == 1:
    print('{} convertido para binário é igual {}'.format(seletor, bin(num)[2:]))
elif seletor == 2:
    print('{} convertido para octal é igual a {}'.format(seletor, oct(num)[2:]))
elif seletor == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(seletor, hex(num)[2:]))
else:
    print('Nenhuma opção válida foi selecionada')
    