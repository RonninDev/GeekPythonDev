"""
EX036 - Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro circular
é calculado por meio da seguinte fórmula:

    V = pi * raio² * altura
"""

altura = float(input('Digite a altura: '))
raio = float(input('Digite o raio: '))
pi = 3.14

volume = pi * raio ** 2 * altura
print(volume)
