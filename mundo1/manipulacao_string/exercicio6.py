nome_completo = str(input('Digite seu nome completo: ')).upper().strip().split()
first_name = nome_completo[0]
last_name = nome_completo[len(nome_completo) - 1]
print('Seja bem vindo!')
print('Seu primeiro nome é: {}'.format(first_name))
print('Seu último nome é: {}'.format(last_name))
