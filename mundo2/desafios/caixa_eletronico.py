valor_sacar = int(input('Valor a sacar: '))
valor_total = 0
nota_cinquenta = 0
nota_vinte = 0
nota_dez = 0
nota_um = 0
while valor_sacar - valor_total != 0:
    if valor_sacar > 50:
        nota_cinquenta = valor_sacar // 50
        valor_sacar -= nota_cinquenta * 50
    if nota_cinquenta != 0 or valor_sacar <= 40:
        nota_vinte = valor_sacar // 20
        valor_sacar -= nota_vinte * 20
    if nota_vinte != 0 or valor_sacar >= 10:
        nota_dez = valor_sacar // 10
        valor_sacar -= nota_dez * 10
    if nota_vinte != 0 or valor_sacar < 9:
        nota_um = valor_sacar // 1
        valor_sacar -= nota_um * 1
    valor_total = valor_sacar
    if valor_total == 0:
        break

if nota_cinquenta != 0:
    print(f'TOTAL DE {nota_cinquenta} NOTAS DE 50')
if nota_vinte != 0:
    print(f'TOTAL DE {nota_vinte} NOTAS DE 20')
if nota_dez != 0:
    print(f'TOTAL DE {nota_dez} NOTAS DE 10') 
if nota_um != 0:
    print(f'TOTAL DE {nota_um} NOTAS DE 1')


