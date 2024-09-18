a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 0
while cont < 10:
    cont += 1
    an = a1 + (cont - 1) * r
    print('Termo{} = {}'.format(cont, an))
    if cont == 10:
        pergunta = str(input('Deseja que o program mostre mais algum termo? [S/N]'))
        if 's' in pergunta:
            new_cont = cont
            new = int(input('Quantos termos? '))
            while cont < (new_cont + new):
                cont += 1
                an += r
                print('Termo{} = {}'.format(cont, an))
                