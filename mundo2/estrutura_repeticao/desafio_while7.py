from random import randint
from time  import sleep
n1 = 0
cont = 0
resposta = 1
n1 = randint(0, 10)
while n1 != resposta:
    resposta = int(input('Escolha um número entre 0 e 5 e veja se descobriu o número escolhido pela IA: '))
    print('PROCESSANDO...')
    sleep(1)
    if resposta == n1:
        print('Parabéns, você acertou!!!')
        print('Número ecolhido: {}'.format(n1))
    else:
        print('Você falhou, que pena. Tente novamente!')
    if resposta != n1 and resposta > n1:
        print('Um pouco Menos')
    elif resposta != n1 and resposta < n1:
        print('Um pouco Mais')
        cont += 1
    if resposta == n1:
        print('Número de tentativas até acertar: {}'.format(cont))
