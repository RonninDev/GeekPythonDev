"""
EX012 - Leia uma distância em milhas e apresente-a convertida em quilômetros. A Fórmula de conversão é:

    K = 1.61 * M

    sendo K a distância em quilômetros e M em milhas.
"""

m = float(input('Digite a distância em milhas: '))

k = 1.61 * m

print(f'A distância em milhas de {m} é: {k} Km/h')