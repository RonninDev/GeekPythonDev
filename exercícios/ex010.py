"""
EX010 - Leia uma velocidade em Km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo).
A fórmula de conversão é:

    M = K/3.6

    Sendo K a velocidade em km/h e M em m/s
"""

velocidade = float(input('Digite uma velocidade em Km/h: '))

ms = velocidade / 3.6

print('A velocidade {} Km/h em m/s é: {:.1f} m/s'.format(velocidade, ms))