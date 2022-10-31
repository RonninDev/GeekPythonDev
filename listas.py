"""
Listas

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICOS
também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamanho fixo; Qualquer tipo de dados;

Listas em Python são definidas por colchetes: []
"""

type([])

lista1 = [1, 22, 13, 44, 75, 26, 17]

lista2 = ['a', 'b', 'c', 'd']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

lista6 = [1, 2, 34, True, 'Geek', d, [1, 2, 3], 4.5456413]

#utilizando lista com variável

numeros = [1, 2, 3, 4, 5]

# Podemos facilmente checar se determinado valor está contido na lista

num = 7

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Para adicionar elementos em uma lista, utilizamos a função append
print(lista1)
lista1.append(42)
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
lista1.insert(2, 'Novo Valor')
print(lista1)

# Iterando sobre listas

# Exemplo1
soma = 0
for elemento in lista1?
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo2 - utilizando o While

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
            carrinho.append(produto)

for produto in carrinho:
    print(produto)

#Git


