valor_produto = float(input('Digite o valor total da compra: '))
print('AVISO: Compras à vista em dinheiro ou em cheque recebem 10% de desconto.\nÀ vista no cartão recebe 5% de desconto. \n3x ou mais no cartão possui 20% de juros.  ')
forma_escolha = int(input('Formas de pagamento: Digite 0 para Dinheiro, 1 para Cheque, e 2 para Cartão: '))
if forma_escolha == 0:
    print('Você escolheu Dinheiro como forma de pagamento.')
    print('Valor final da compra: {}'.format(valor_produto - valor_produto * 0.1))
elif forma_escolha == 1:
    print('Você escolheu Cheque como forma de pagamento.')
    print('Valor final da compra: {}'.format(valor_produto - valor_produto * 0.1))
elif forma_escolha == 2:
    vista = str(input('Será à vista ou parcelado? (Digite V para à vista e P para parcelado)')).lower()
    if 'v' in vista:
        print('Valor final da compra: {}'.format(valor_produto - valor_produto * 0.05))
    elif 'p' in vista:
        parcela = int(input('Deseja parcelar em quantas vezes? '))
        if parcela <= 2:
            print('Valor final da compra: {}'.format(valor_produto))
        elif parcela >= 3:
            parcelamento = ((valor_produto * 0.2 + valor_produto) / parcela)
            valor_final = parcelamento * parcela
            print('Valor final da compra: {}\n O valor ficou por {:.2f} em {} vezes'.format(valor_final, parcelamento , parcela))
else:
    print('Opção inválida de pagamento.')