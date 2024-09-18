valor_casa = float(input('Digite o valor da casa: '))
valor_salario = float(input('Digite o seu salário: '))
valor_salario_maximo = valor_salario * 0.3
qtd_anos = int(input('Em quantos anos deseja pagar? '))
prestacao_mensal = valor_casa / (qtd_anos * 12)
if prestacao_mensal > valor_salario_maximo:
    print('Essa casa, infelizmente, está indiponivel para o senhor(a). Recomendo procuras outras residencias que caibam em seu orçamento.')
else:
    print('Aqui está a prestação mensal da residencia: {:.2f} R$.'.format(prestacao_mensal))
    