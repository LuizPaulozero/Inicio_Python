lista = []
while True:
    lista.append(input('Digite um número: '))
    pergunta = str(input('Deseja continuar? '))
    total_numeros = len(lista)
    if 'n' in pergunta:
        break
if '5' in lista:
    print('O número cinco foi digitado e faz parte da lista.')
else:
    print('O número cinco não foi digitado')
lista.sort(reverse=True)
print(f'Total de números digitados: {total_numeros}')
print(f'Lista de valores em forma decrescente: {lista}')

