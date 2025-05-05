segundos = int(input())

horas, minutos = 0, 0

if segundos>=3600:
    horas = int(segundos/3600)
    segundos -= horas*3600

if segundos>=60:
    minutos = int(segundos/60)
    segundos -= minutos*60

print(f'{horas}:{minutos}:{segundos}')