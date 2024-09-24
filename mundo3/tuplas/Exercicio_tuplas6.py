palavras = ('Arroz', 'Cuscuz', 'Feijão', 'Batata', 'Avião', 'Sul', 'Frio', 'Gincana', 'Futuro', 'Presente', 'Passado')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos: ', end='')
    for vogais in i:
        if vogais.lower() in 'ãâàáaêeiíoóu':
            print(f'{vogais.lower()}', end='')
