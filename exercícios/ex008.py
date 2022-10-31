"""
EX008 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é:

    C = K - 273.15

    Sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

kelvin = float(input('Digite uma temperatura em Kelvin: '))

celsius = kelvin - 273.15

print('A temperatura {}ºK em Celsius é: {:.2f}ºC'.format(kelvin, celsius))