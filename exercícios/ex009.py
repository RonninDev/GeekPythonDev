"""
EX009 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de conversão é:

    K = C + 273.15

    Sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

celsius = float(input('Digite um número em Celsius: '))

kelvin = celsius + 273.15

print('A temperatura {}ºC em Kelvin é: {:.2f}°K'.format(celsius, kelvin))