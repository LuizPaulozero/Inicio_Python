continuar = ''
contm = 0
contf = 0
contf2 = 0
cont_geral = 0
while 'n' not in continuar:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: '))
    if 'm' in sexo:
        contm += 1
    if 'f' in sexo:
        contf += 1
        if idade < 20:
            contf2 += 1
    if idade >= 18:
        cont_geral += 1
    continuar = str(input('Deseja continuar? '))
print(f'Quantidade de pessoas maiores de idade {cont_geral}')
print(f'Quantidade de homens cadastrados {contm}')
print(f'Quantidade de mulheres menores de 20 anos {contf2}')
