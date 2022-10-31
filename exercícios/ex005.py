"""
EX005 - Leia um número real e imprima a quinta parte deste número
"""
num = float(input('Digite um número: '))

quinta_parte_div = num // 5
quinta_parte_mult = quinta_parte_div * 5

print('O número {} tem sua quinta parte:  {}'.format(num, quinta_parte_div))
