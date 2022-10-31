"""
EX024 - Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A fórmula de conversão é:

    A = M * 0.000247

    sendo M a área em metros quadrados e A a área em acres.

"""

metro = float(input('Digite o valor da área em metros: '))

acre = metro * 0.000247

print('Convertido em acres, o resultado é: {:.2f}'.format(acre))