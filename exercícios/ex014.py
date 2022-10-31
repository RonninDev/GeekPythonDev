"""
EX014 - Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é:

    R = G * 3.14/180

    sendo G o ângulo em graus e R em radianos e Pi.
"""

g = float(input('Digite um ângulo em graus: '))

r = g * 3.14 / 180

print('ângulo {}º em radianos é igual a: {:.2f}'.format(g, r))