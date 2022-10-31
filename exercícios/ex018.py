"""
EX018 - Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A fórmula de conversão é:

    L = 1000 * M

    sendo L o volume em litros e M o volume em metros cúbicos.

"""

m3 = float(input('Digite um valor em metros cúbicos: '))

lt = 1000 * m3

print('O valor em Litros é: {} lts'.format(lt))