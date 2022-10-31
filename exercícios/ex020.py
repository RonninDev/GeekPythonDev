"""
EX020 - Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de conversão é:

    L = K / 0.45

    sendo K a massa em quilogramas e L a massa em libras.
"""

kg = float(input('Digite um valor de massa em quilôgramas: '))

lb = kg / 0.45

print(f'O valor da massa convertido para libras é {:.2f}'.format(lb))