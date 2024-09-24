cont = 0
pares = 0
tup = ()
for i in range(1, 5):
    num = int(input('Digite um número: '))
    cont += 1
    tup += (num,)
    if num % 2 == 0:
        pares += 1
print(f'O número nove aparece {tup.count(9)} vezes')
if 3 in tup:
    print(f'O número três apareceu na posição {tup.index(3) + 1}°')
else:
    print(f'O número três não foi digitado em nenhuma posição')
print(f'Números pares digitados: ')
for numeros in tup:
    if numeros % 2 == 0:
        print(numeros, end=' ')