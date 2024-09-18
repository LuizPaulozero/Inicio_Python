largura= float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
qtd_tinta = area / 2
print('A área da parede é: {} m2 \nA quantidade de tinta necessária para pinta a parede é: {} latas'.format(area, qtd_tinta))

preco_bruto = float(input('Digite o valor do produto, por litro de tinta: '))
preco_lqd = preco_bruto * qtd_tinta
print('O valor final do produto é: {}'.format(preco_lqd))
