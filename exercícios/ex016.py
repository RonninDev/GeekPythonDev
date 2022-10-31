"""
EX016 - Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. A fórmula de conversão é:

    C = P * 2.54

    sendo C o comprimento em centímetros e P o comprimento em polegada.
"""

p = float(input('Digite um valor de comprimento em polegadas: '))

c = p * 2.54

print('valor convertido em centímetros é: {} cm'.format(c))