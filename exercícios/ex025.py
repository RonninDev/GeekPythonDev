"""
EX025 - Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A fórmula de conversão é:

    M = A * 4048.58

    sendo M a área em metros quadrados e A a área em acres.

"""

acres = float(input('Digite o valor em acres: '))

metro = acres * 4048.58

print('O valor em metros é: {:.2f}'.format(metro))
