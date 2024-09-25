lista_geral = []
lista_par = []
lista_impar = []
while True:
    lista_geral.append(int(input('Digite um número inteiro: ')))
    continuar = str(input('Deseja continuar? '))
    if 'n' in continuar: 
        break
for i in lista_geral:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print(f'Lista composta por todos os números: {lista_geral}')
print(f'Lista composta apenas pelos números ímpares: {lista_impar}')
print(f'Lista composta apenas por números pares: {lista_par}')
