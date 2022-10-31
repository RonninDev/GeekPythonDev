"""
EX015 - Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é:

    G = R * 180/pi

    sendo G o ângulo em graus e R em radianos e pi.
"""

r = float(input('Digite um ângulo em radianos: '))

g = r * 180 / 3.14

print('O ângulo em radianos {}º em graus é: {:.2f}º '.format(r, g))