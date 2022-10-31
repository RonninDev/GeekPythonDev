"""
EX030 - Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
"""

valor = float(input('Digite um valor em R$: '))
dolar = 5.28

cotacao = valor / dolar
print('O valor da cotação de R${} em dólar é: U${}'.format(valor, dolar))