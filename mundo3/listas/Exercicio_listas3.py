numeros = []
for i in range(5):
    num = int(input('Digite um número: '))
    if i == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Número adicionado ao final da lista')
    else: 
        pos = 0
        while pos < len(numeros):
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Número adicionado na {pos} da lista')
                break
            pos += 1
print(numeros)