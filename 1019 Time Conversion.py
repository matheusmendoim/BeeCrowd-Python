duracao = int(input())

horas = duracao//(60*60)
duracao = duracao%(60*60)

minutos = duracao//60
duracao = duracao%60

segundos = duracao%60

print(f"{horas}:{minutos}:{segundos}")
