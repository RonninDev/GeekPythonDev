"""
EX022 - Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é:

    M = 0.91 * J

    sendo J o comprimento em jardas e M o comprimento em metros.

"""

jarda = float(input('Digite um valor em jardas: '))

metro = 0.91 * jarda

print('O valor em metros é: {} m'.format(metro))