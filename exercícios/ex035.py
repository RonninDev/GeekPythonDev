"""
EX035 - Sejam "A" e "B" os catetos de um triângulo, onde a hipotenusa é obtida pela equação:

    hipotenusa = raiz de a² + b²

    Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação.
    Imprima o resultado dessa operação
"""

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

hip = (a ** 2) + (b ** 2) **2
print(hip)