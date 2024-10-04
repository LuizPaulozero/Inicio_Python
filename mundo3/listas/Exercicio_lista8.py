geral = [[],[]]
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        geral[0].append(num)
    else:
        geral[1].append(num)
geral[0].sort()
geral[1].sort()
print(f'Lista de números pares: {geral[0]}')
print(f'Lista de búmeros ímpares: {geral[1]}')