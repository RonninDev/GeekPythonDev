"""
EX013 - Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de conversão é:

    M = K/1.61

    Sendo K a distância em quilômetros e M em milhas.
"""

km = float(input('Digite uma distância em Km/h: '))

m = km / 1.61

print('A distância {} Km/h convertida para milhas é: {:.2f} milhas'.format(km, m))