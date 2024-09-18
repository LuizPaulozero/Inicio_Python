frase = str(input('Digite uma frase ou  uma palavra e veerifique se é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
    