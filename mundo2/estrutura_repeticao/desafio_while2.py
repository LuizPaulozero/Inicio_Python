from random import randint
print(25*'-')
print('Vamos jogar Impar ou Par!')
print(25*'-')
contv = 0
contd = 0
while contd == 0:
    ia = randint(0, 10)
    jogador = int(input('Escolha um número entre 0 e 10: '))
    escolha = str(input('Par ou Ímpar? ')).lower()
    if 'p' in escolha and (jogador + ia) % 2 == 0 or 'i' in escolha and (jogador + ia) % 2 != 0:
        print('Você ganhou, vamos de novo')
        contv += 1
    else:
        contd += 1
        if (jogador + ia) % 2 == 0:
            a = 'Par'
        else:
            a = 'Impar'
        print(f'Game over, you lose my friendo! Você escolheu {jogador} e o computar escolheu {ia}, {jogador} + {ia} dá {jogador + ia} e o resultado é {a}')
        print(f'Você venceu {contv} vezes')
        