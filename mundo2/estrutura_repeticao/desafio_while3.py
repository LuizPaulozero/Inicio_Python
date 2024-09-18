continuar = ''
num = 0
soma = 0
maior = 0
menor = 0
contador = 0
while continuar.lower() != 'n':
    continuar = str(input('Deseja prosseguir com o programa? [S/N]')).lower()
    if continuar.lower() != 'n':
        num = int(input('Digite um número inteiro qualquer: '))
        contador += 1
        soma += num
        media = soma/contador
        if contador == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
print('A média de todos os números digitados é igual a {:.2f}'.format(media))
print('O maior  número é igual a {} e o menor é igual a {}'.format(maior, menor))
