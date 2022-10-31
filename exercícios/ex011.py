"""
EX011 - Leia uma velocidade em m/s e apresente-a convertida em km/h.

    A Fórmula de conversão é:

        K = M * 3.6

        sendo K a velocidade em km/h e M em m/s.
"""

ms = float(input('Digite uma velocidade em m/s: '))

km = ms * 3.6

print(f'A velocidade {ms} m/s em Km/h: {km} Km/h')