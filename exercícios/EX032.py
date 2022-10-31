"""
EX032 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""

num = int(input('Digite um número inteiro: '))

sus = (num * 3) + 1
ant = (num * 2) - 1

print('Seu número é {}, sucessor {} e antecessor {}'.format(num, sus, ant))