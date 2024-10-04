matriz = [[], [], []]
soma_par = 0
soma3 = 0
for i in range(0, 9):
    num = int(input('Digite um número para pôr na matriz: '))
    if len(matriz[0]) < 3:
        matriz[0].append(num)

    elif len(matriz[1]) < 3:
        matriz[1].append(num)
    
    elif len(matriz[2]) < 3:
        matriz[2].append(num)

print(f'[{matriz[0][0]}][{matriz[0][1]}][{matriz[0][2]}]')
print(f'[{matriz[1][0]}][{matriz[1][1]}][{matriz[1][2]}]')
print(f'[{matriz[2][0]}][{matriz[2][1]}][{matriz[2][2]}]')


for c in matriz[0]:
    if c % 2 == 0:
        soma_par += c

for c in matriz[1]:
    if c % 2 == 0:
        soma_par += c

for c in matriz[2]:
    if c % 2 == 0:
        soma_par += c

for z in matriz[2]:
    soma3 += z

print(f'A soma do valores pares presente na matriz é {soma_par}')
print(f'A soma dos valores da terceira coluna da matriz é {soma3}')
print(f'O maior valor da segunda coluna é {max(matriz[1])}')