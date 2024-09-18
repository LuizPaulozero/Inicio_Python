v = int(input('Digite a velocidade do veículo e verifique se recebeu uma multa, caso sim verá o valor da mesma: '))
if v > 80:
    print('Sua condulta foi imprudente e por isso você foi multado em: {} R$, se esforce para que nao aconteça novamente.'.format( (v * 7) - 560))
if v == 80:
    print('Você está no limite da velocidade, cuidado para não ultrapassar.')
else:
    print('Você está dirigindo prudentemente, continue assim.')