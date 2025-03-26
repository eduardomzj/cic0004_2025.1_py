a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

maior_ab = int((a + b + abs(a-b)) / 2)
maior_bc = int((b + c + abs(b-c)) / 2)

if maior_ab > maior_bc:
    maior_numero = maior_ab
else:
    maior_numero = maior_bc

print(f'{maior_numero} eh o maior')

"""
versao com operador ternário 

maior_numero = maior_ab if maior_ab > maior_bc else maior_bc
"""

