import math
ang = int(input('Digite o valor do ângulo: '))
tan = math.tan(math.radians(ang))
cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
print('Tangente: {:.2f} \nCosseno: {:.2f} \nSeno: {:.2f}'.format(tan, cos, sen))