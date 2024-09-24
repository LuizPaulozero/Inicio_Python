from random import randint
tupla = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
menor_valor = maior_valor = tupla[0]
print(f'Números gerados: {tupla}')
print(f'O menor é igual a: {min(tupla)}')
print(f'O maior valor é igual a: {max(tupla)}')
