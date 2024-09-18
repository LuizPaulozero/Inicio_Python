frase = str(input('Digite um frase qualquer: ')).strip().lower()
contagem = frase.count('a')
posicao = frase.find('a') + 1
last = frase.rfind('a') + 1
print('Quantidade de letras a presente na frase: {} \nPosição que aparece pela primeira vez: {} \nPosição que aparece pela última vez: {}'.format(contagem, posicao, last))