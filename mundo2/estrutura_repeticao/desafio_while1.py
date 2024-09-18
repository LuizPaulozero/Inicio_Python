permanecer = ''
total = 0
caro = 0
barato = 0
cont = 0
while 'n' not in permanecer:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total += preco
    cont += 1
    if preco > 1000:
        caro += 1
    if cont == 1:
        barato = preco
        nomebarato = nome
    if barato > preco:
        barato = preco
        nomebarato = nome
    permanecer = str(input('Quer continuar? '))
print(f'Preço total da compra: {total}')
print(f'Produtos com preço acima de 1000R$: {caro}')
print(f'Produto com menor preço: {nomebarato}, seu preço {barato}')
