"""
EX031 - Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
"""
num = int(input('Digite um número inteiro: '))
ant = num -1
sus = num +1

print('O número é {}, seu antecessor é {} e o sucessor é {}'.format(num, ant, sus))