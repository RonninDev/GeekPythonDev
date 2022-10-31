"""
EX023 - Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula de conversão é:

    J = M / 0.91

    sendo J o comprimento em jardas e M o comprimento em metros.

"""

metro = float(input('Digite o comprimento em metros: '))

jarda = metro / 0.91

print('O valor convertido em jardas é: {:.2f}jrd'.format(jarda))