peso = float(input('Digite o seu peso atual: '))
altura = float(input('Digite a sua altura atual: '))
imc = peso/(altura ** 2)
if imc <= 18.5:
    print('Você está abaixo do peso recomendado, seu IMC: {:.2f}. O IMC ideal é entre 18.5 e 25.'.format(imc))
elif 18.5 < imc <= 25:
    print('Você está com o peso ideal, seu IMC: {:.2f}.'.format(imc))
elif 26 < imc <= 30:
    print('Você está com sobrepeso, seu IMC: {:.2f}.'.format(imc))
elif 30 < imc <= 40:
    print('Você está com obesidade, seu IMC: {:.2f}.'.format(imc))
elif 40 > imc:
    print('Você está com obesidade mórbida, seu IMC: {:.2f}.'.format(imc))
    