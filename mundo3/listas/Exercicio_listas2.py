numeros = []
while True:
    num = int(input('Digite um número: '))
    if num in numeros:
        print('Esse número já existe na lista.')
    else:
        numeros.append(num)
        print('Número adicionado com sucesso')
    continuar = str(input('Deseja continuar? ')).lower()
    if 's' not in continuar:
        break
print(numeros)
