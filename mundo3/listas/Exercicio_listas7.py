pessoas = []
dados = []
pesos_leves = []
pesos_pesados = []
cont = menor_peso = maior_peso = 0

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja contiuar? [S/N] '))
    if continuar in 'Nn':
        break

for c in pessoas:
    cont += 1
    if cont == 1:
        maior_peso = menor_peso = c[1]
        pesos_leves.append(c[0])
        pesos_pesados.append(c[0])
    else:
        if c[1] > maior_peso:
            maior_peso = c[1]
            pesos_pesados = [c[0]]

        elif c[1] == maior_peso:
            pesos_pesados.append(c[0])

        if c[1] < menor_peso:
            menor_peso = c[1]
            pesos_leves = [c[0]]

        elif c[1] == menor_peso:
            pesos_leves.append(c[0])

print(f'Número de pessoas cadastradas:  {len(pessoas)}')
print(f'Pessoa(s) com maior peso: {pesos_pesados}, peso: {maior_peso}')
print(f'Pessoa(s) com menor peso: {pesos_leves}, seu peso: {menor_peso}')
