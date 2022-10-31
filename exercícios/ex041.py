"""
EX041 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""

hora_trabalhada = int(input('Digite o número de horas trabalhadas: '))
valor_hora = float(input('Valor da hora trabalhada: '))

total_trabalhado = hora_trabalhada * valor_hora
adicional = (total_trabalhado / 100) * 10

total = total_trabalhado + adicional
print(f'R${total}')