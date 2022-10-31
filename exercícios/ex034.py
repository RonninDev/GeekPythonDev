"""
EX034 - Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do círculo é:

    Pi * raio²

    considerando Pi = 3.141592
"""

raio = float(input('Digite o valor do raio: '))
pi = 3.14
circunferencia = pi * raio ** 2
print(circunferencia)