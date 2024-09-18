from datetime import date
sexo = str(input('(Digite m ou f) \nDigite o seu sexo: '))
busca = 'm' in sexo
if busca:
    debito = str(input('(Responda com s ou n)\n Você já se alistou no exército? ')).lower()
    busca = 'n' in debito
    if busca:
        nascimento = int(input('Digite o ano em que você nasceu: '))
        data_atual = date.today().year
        calculo = data_atual - nascimento
        if calculo == 18:
            print('Já tá na hora de se alistar mano.')
        elif calculo < 17:
            print('Fique atento, faltam {} anos para seu alistamento obrigátorio.'.format(18 - calculo))
        elif calculo > 18:
            print('Passou da hora de se alistar, irmão. Está em em débito com o serviço de alistamento há {} anos.'.format(calculo - 18))
    else:
        print('Tudo certo então, tenha um bom dia!')
else:
    print('O serviço é obrigatório para homens, está liberada.')
