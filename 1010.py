#split() é uma função que divide uma string em partes, por isso há a necessidade de correção dos tipos

código_1, pecas_1, valor_1 = input().split()
código_2, pecas_2, valor_2 = input().split()

código_1 = int(código_1)
pecas_1 = int(pecas_1)
valor_1 = float(valor_1)

código_2 = int(código_2)
pecas_2 = int(pecas_2)
valor_2 = float(valor_2)

valor_total = pecas_1*valor_1 + pecas_2*valor_2
print(f'VALOR A PAGAR: R$ {valor_total:.2f}')

