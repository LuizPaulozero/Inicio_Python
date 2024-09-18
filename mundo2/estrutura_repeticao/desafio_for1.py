cont_idade_m = 0
cont_nome = 0
cont_sexo_f = 0
cont_idade_f = 0
idade_f = 0
for count in range(1, 5):
    sexo = str(input('Qual o seu sexo, digite m ou f: ')).lower().strip()
    if sexo == 'f':
        cont_sexo_f += 1
        nome = str(input('Digite seu nome: '))
        idade = int(input('Digite sua idade: '))
        idade_f += 1
        if idade_f != 0:
            if idade_f == 1:
                f1 = idade
            elif idade_f == 2:
                f2 = idade
            elif idade_f == 3:
                f3 = idade
            elif idade_f == 4:
                f4 = idade

        if idade < 20:
            cont_idade_f += 1
    elif sexo == 'm':
        nome = str(input('Digite seu nome: '))
        cont_nome += 1
        if cont_nome != 0:
            if cont_nome == 1:
                nm1 = nome
            if cont_nome == 2:
                nm2 = nome
            if cont_nome == 3:
                nm3 = nome
            if cont_nome == 4:
                nm4 = nome
        idade = int(input('Digite sua idade: '))
        cont_idade_m += 1
        if cont_idade_m != 0:
            if cont_idade_m == 1:
                m1 = idade
            elif cont_idade_m == 2:
                m2 = idade
            elif cont_idade_m == 3:
                m3 = idade
            elif cont_idade_m == 4:
                m4 = idade
    else:
        print('Não é uma opção válida.')

if idade_f == 1 and cont_idade_m == 3:
    calculo_media = (m1 + m2 + m3 + f1) / 4
if idade_f == 2 and cont_idade_m == 2:
    calculo_media = (f1 + f2 + m1 + m2) / 4
if idade_f == 3 and cont_idade_m == 1:
    calculo_media = (f1 + f2 + f3 + m1) / 4
if idade_f == 4 and cont_idade_m == 0:
    calculo_media = (f1 + f2 + f3 + f4) / 4
if idade_f == 0 and cont_idade_m == 4:
    calculo_media = (m1 + m2 + m3 + m4) / 4

if cont_idade_m == 4:
    if m1 > m2 and m1 > m3 and m1 > m4:
        print('O mais velho entre os homens é {}'.format(nm1))
    elif m2 > m1 and m2 > m3 and m2 > m4:
        print('O mais velho entre os homens é {}'.format(nm2))
    elif m3 > m1 and m3 > m2 and m3 > m4:
        print('O mais velho entre os homens é {}'.format(nm3))
    elif m4 > m1 and m4 > m2 and m4 > m3:
        print('O mais velho entre os homens é {}'.format(nm4))
if cont_idade_m == 3:
    if m1 > m2 and m1 > m3:
        print('O mais velho entre os homens é {}'.format(nm1))
    elif m2 > m1 and m2 > m3:
        print('O mais velho entre os homens é {}'.format(nm2))
    elif m3 > m1 and m3 > m2:
        print('O mais velho entre os homens é {}'.format(nm3))
if cont_idade_m == 2:
    if m1 > m2:
        print('O mais velho entre os homens é {}'.format(nm1))
    elif m2 > m1:
        print('O mais velho entre os homens é {}'.format(nm2))
if cont_idade_m == 1:
        print('Só há um homem, seu nome é: {} e sua idade é: {}'.format(nm1, m1))
print('Média entre idades do grupo: {}'.format(calculo_media))
print('Quantidade de Mulheres com menos de 20 anos: {}'.format(cont_idade_f))