salario = float(input('Digite quanto você ganha atualmente: '))
if salario > 1250:
    print('Seu sálario {} + um aumento de 10%, valor final: {}'.format(salario, salario + salario * 0.1))
if salario < 1250:
    print('Seu sálario {} + um aumento de 15%, valor final: {}'.format(salario, salario + salario * 0.15))
if salario == 1250:
    print('Nenhum aumento disponível.')
    