n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
n3 = float(input('Digite só mais um número: '))
if n1 == n2 and n1 == n3:
    print('Todos os números possuem valores iguais')
if n1 > n2 and n1 > n3:
    print('O número {} é maior que {} e que {}.'.format(n1, n2, n3))

if n2 > n1 and n2 > n3:
    print('O número {} é maior que {} e que {}.'.format(n2, n1, n3))

if n3 > n1 and n3 > n2:
    print('O número {} é maior que {} e que {}.'.format(n3, n1, n2))

if n1 < n2 and n1 < n3:
    print('O menor número, entre os três, é {}.'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor número, entre os três, é {}.'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor número, entre os três, é {}.'.format(n3))
    