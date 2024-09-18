nome_cidade = str(input('Digite o nome da cidade em que você nasceu: ')).lower().strip()
consulta = (nome_cidade[:5] == 'santo')
print('Resultado: {}'.format(consulta))
