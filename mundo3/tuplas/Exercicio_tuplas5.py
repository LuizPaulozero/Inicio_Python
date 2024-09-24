carrinho = ()
continuar = 1
print('-=' * 30 + '\n               Seja Bem Vindo ao nosso caixa\n' + '-=' * 30)
while True: 
    nome_produto = str(input('Por favor, digite o nome do Produto: '))
    preco_produto = float(input('Por favor, digite o preço do produto: '))
    carrinho += ((nome_produto, preco_produto))
    continuar = int(input('Digite 0 para finalizar: '))
    if continuar == 0:
        for i in range(0, len(carrinho)):
            if i % 2 == 0:
                print(f'{carrinho[i]:.<30}', end='')
            else:
                print(f'R$ {carrinho[i]:>7.2f}')
        break
