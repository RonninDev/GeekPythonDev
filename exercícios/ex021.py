"""
EX021 - Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é:

    K = L * 0.45

    sendo K a massa em quilogramas e L a massa em libras.

"""

lb = float(input('Digite um número em libras: '))

kg = lb * 0.45

print('O resultado em quilogramas é: {} kg'.format(kg))