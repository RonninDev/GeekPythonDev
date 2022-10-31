"""
EX043 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

    - O total com desconto de 10%;
    - O valor de cada parcela, no parcelamento de 3x sem juros;
    - A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
    - A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

"""

valor = float(input('Digite o valor: '))
desconto = (valor / 100) * 10
tipo_de_venda = int(input('[1] Parcelado ou [2] à vista: '))
    if tipo_de_venda == 1:
        print('venda parcelada')
    elif tipo_de_venda == 2:
        print('venda à vista')
    else:
        print('tente outra vez')
