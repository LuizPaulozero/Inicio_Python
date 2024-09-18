qtd_km = float(input('Quantos km foram percorridos pelo veículo?'))
qtd_dias = int(input('Por quantos dias o carro foi alugado?'))

pagar_km = qtd_km * 0.15
pagar_carro = qtd_dias * 60

print('Valor pela quantidade de km rodados: {:.2f} \nValor total por dias de uso do carro: {} \nValor total: {}R$'.format(pagar_km, pagar_carro, (pagar_carro + pagar_km)))
