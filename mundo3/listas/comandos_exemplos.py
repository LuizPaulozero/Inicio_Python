numeros = [3,4,5,6,7,9,8]
numeros.sort #Organiza os números em ordem crescente
numeros.sort(reverse=True) #Organiza os números de trás para frente
numeros.append(10) #Adiciona um elemento ao final da lista
numeros.insert(1, 78) #Adiciona um elemento na posição indicada
numeros.pop(1) #Deleta um elemento, caso não indique a posição, deleta o ultimo elemento
valores = []
valores.append(1)
valores.append(2)
valores.append(3)
print(valores)
for n, i in enumerate(valores): #Enumerate recebe a chave e a posição do elemento
    print(f'{n}...{i}')
a = [1,2,3,5]
b = a #Cria uma ligação entre as listas
b = a[:] #Cria uma cópia da lista 'a'
