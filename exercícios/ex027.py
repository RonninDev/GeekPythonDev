"""
EX027 - Leia um valor de área em hectares e apresente-o convertido em metros quadrados m². A fórmula de conversão é:[

    M = H * 10000

    sendo M a área em metros quadrados e H a área em hectares.
"""

hec = float(input('Digite uma área em hectares: '))

mq = hec * 10000

print('A área em {}hec convertida em m² é: {:.2f}m²'.format(hec, mq))