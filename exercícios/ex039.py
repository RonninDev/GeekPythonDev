"""
EX039 - A importância de R$ 780.000,00 será divida entre três ganhadores de um concurso. Sendo que da quantia total:

    - O Primeiro ganhador receberá 46%.
    - O segundo receberá 32%.
    - O terceiro receberá o restante.

    Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

montante = float(780000)

p1 = (montante / 100) * 46
p2 = (montante / 100) * 32
p3 = montante - p1 - p2
print(f'''O Primeiro receberá R${p1} o segundo R${p2} e o terceiro R${p3}.''')