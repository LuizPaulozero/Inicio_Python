r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('Valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os valores da reta formam um triângulo.')
    if r1 == r2 and r2 == r3 and r3 == r1:
        print('As retas formam um triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('As retas formam um triângulo isósceles.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('As retas formam um triângulo escaleno.')
else:
    print('Os valores não formam um triângulo')
    