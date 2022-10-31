"""
EX037 - Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.
"""

valor_produto = float(input("Digite o valor do Produto em R$: "))
desconto = (valor_produto / 100) * 12

valor_final = valor_produto - desconto
print(valor_final)