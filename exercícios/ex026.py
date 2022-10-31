"""
EX026 - Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares. A fórmula de conversão é:

    H = M * 0.0001

    sendo M a área em metros quadrados e H a área em hectares.
"""

mq = float(input('Digite um número em m²: '))

hec = mq * 0.0001

print('A área {}m² convertida em hectares é: {:.2f}hec'.format(mq, hec))