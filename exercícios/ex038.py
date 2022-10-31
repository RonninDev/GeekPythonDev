"""
EX038 - Leia o salário de um funcionario. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
"""
salario = float(input('Informe o salário: '))
aumento = (salario / 100) * 25

total = salario + aumento
print(f"R${total}")