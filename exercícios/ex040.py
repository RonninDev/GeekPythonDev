"""
EX040 - Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados
pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""
num_dias = int(input('Digite o número de dias trabalhados: '))
valor_dia = 30

dias_trabalhados = valor_dia * num_dias
imposto = (dias_trabalhados / 100) * 8

total =  dias_trabalhados - imposto
print(total)
