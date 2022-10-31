"""
EX029 - Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

print('A média das notas é {:.2f}'.format(media))