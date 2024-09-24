num = list()
for i in range(0, 5):
    num.append(int(input('Digite um número: ')))
print(f'O maior valor da lista é:{max(num)} na posição {num.index(max(num)) + 1}')
print(f'O menor valor da lista é:{min(num)} na posição {num.index(min(num)) + 1}')
