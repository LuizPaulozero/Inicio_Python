from random import randint
a = randint(1, 10)
b = randint(1, 10)
c = randint(1, 10)
d = randint(1, 10)
e = randint(1, 10)
tupla = (a, b, c, d, e)
menor_valor = maior_valor = tupla[0]
for cont in tupla:
    if menor_valor > cont:
        menor_valor = cont
    if maior_valor < cont:
        maior_valor = cont
print(f'Números gerados: {tupla}')
print(f'O menor é igual a: {menor_valor}')
print(f'O maior valor é igual a: {maior_valor}')