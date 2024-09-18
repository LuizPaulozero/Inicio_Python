km_rodados = float(input('Quantos km foram percorrigos?  '))
if km_rodados <= 200:
    print('Valor total: {} R$'.format(km_rodados * 0.5))
else:
    print('Valor total da viagem: {} R$'.format(km_rodados * 0.45))
