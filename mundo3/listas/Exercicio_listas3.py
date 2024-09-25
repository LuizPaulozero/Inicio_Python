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
                print(pos)
                if pos == 0:
                    print('Número adicionado ao inicio da lista')
                else:
                    print('Número adicionado no meio da lista')
                break
            pos += 1
print(numeros)