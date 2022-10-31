"""
EX007 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula de conversão é:

    C = 5.0 * (F - 32.0)/9.0

    Sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""

fahrenheit = float(input('Digite uma temperatura em Fahrenheit: '))

celsius = 5.0 * (fahrenheit - 32.0)/9.0

print('A temperatura {}°F em Celsius é: {:.2f}°C'.format(fahrenheit, celsius))
