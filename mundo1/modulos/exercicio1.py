import math
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valo do cateto adjacente: '))
h = math.hypot(n1, n2)
print('Aqui: {:.2f} '.format(h))
