"""
EX042 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário
tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o slaário-base.
"""

salario_base = float(input('Digite o salário-base do funcionário: '))
gratificacao = salario_base + ((salario_base / 100) * 5)
imposto = salario_base - ((salario_base / 100) * 7)

liquido = salario_base + gratificacao - imposto
print(f'R${liquido}')