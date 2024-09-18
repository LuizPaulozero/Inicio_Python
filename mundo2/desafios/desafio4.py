import random
from time import sleep
escolha_user = int(input('Vamos jogar um jokenpô \nDigite 1 para Tesoura, 2 para Papel ou 3 para Pedra: '))

jogadas = ['Papel', 'Tesoura', 'Pedra']
computer = random.choice(jogadas)
print('Decidindo o ganhador...')
sleep(3)
if escolha_user == 1 and computer == jogadas[0]:
    print('Você ganhou! Sua escolha: Tesoura Escolha do computador: {}'.format(computer))
elif escolha_user == 1 and computer == jogadas[1]:
    print('Empate! Sua escolha: Tesoura Escolha do computador: {}'.format(computer))
elif escolha_user == 1 and computer == jogadas[2]:
    print('Você perdeu! Sua escolha: Tesoura, Escolha do computador: {}'.format(computer))

if escolha_user == 2 and computer == jogadas[2]:
    print('Você ganhou! Sua escolha: Papel, Escolha do computador: {}'.format(computer))
elif escolha_user == 2 and computer == jogadas[0]:
    print('Empate! Sua escolha: Papel, Escolha do computador: {}'.format(computer))
elif escolha_user == 2 and computer == jogadas[1]:
    print('Você perdeu! Sua escolha: Papel, Escolha do computador: {}'.format(computer))

if escolha_user == 3 and computer == jogadas[1]:
    print('Você ganhou! Sua escolha: Pedra Escolha do computador: {}'.format(computer))
elif escolha_user == 3 and computer == jogadas[2]:
    print('Empate! Sua escolha: Pedra, Escolha do computador: {}'.format(computer))
elif escolha_user == 3 and computer == jogadas[0]:
    print('Você perdeu! Sua escolha: Pedra, Escolha do computador: {}'.format(computer))
    