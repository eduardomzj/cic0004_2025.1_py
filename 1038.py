precos = [4.0, 4.5, 5.0, 2.0, 1.5]

codigo, quantidade = map(int, input().split())

total = precos[codigo-1]*quantidade

print(f'Total: R$ {total:.2f}')