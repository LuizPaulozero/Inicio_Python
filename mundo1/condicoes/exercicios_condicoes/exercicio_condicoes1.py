from random import randint
from time import sleep
n1 = randint(0, 5)
resposta = int(input('Escolha um número entre 0 e 5 e veja se descobriu o número escolhido pela IA: '))
print('PROCESSANDO...')
sleep(3)
if resposta == n1:
    print('Parabéns, você acertou!!!')
else:
    print('Você falhou, que pena. Tente novamente!')
    print('Número ecolhido: {}'.format(n1))