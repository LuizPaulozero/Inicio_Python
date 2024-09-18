from datetime import date
cont = 0
conta = 0
for i in range(1, 4):
    idade = int(input('Digite o ano em que você nasceu: '))
    ano_atual = date.today().year
    calculo = (ano_atual - idade)
    if calculo >= 21:
        cont += 1
    elif calculo < 21:
        conta += 1
print('Quantidade de pessoas que já são maiores de idade {}'.format(cont))
print('Quantidade de pessoas que ainda são menores de idade {}'.format(conta))
