"""
EX019 - Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A fórmula de conversão é:

    M = L / 1000

    sendo L o volume em litros e M o volume em metros cúbicos.

"""

lt = float(int('Digite o volume em litros: '))

m = lt / 1000

print(f'O valor em metros cúbicos é {lt}')