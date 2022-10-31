"""
EX006 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é:

    F = C*(9.0/5.0) + 32.0

    sendo F a tempwratura em Fahrenheit e C a temperatura em Celsius.
"""

celsius = float(input('Digite uma temperatura em ºC: '))

fahrenheit = celsius * (9.0 / 5.0) + 32.0

print('A temperatura {}ºC em Fahrenheit é: {}ºF'.format(celsius, fahrenheit))