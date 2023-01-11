idade_dias = int(input())

#quantidade de dia em anos
anos = idade_dias//365
idade_dias %= 365

#quantidade de meses em anos
meses = idade_dias//30

#quantidade de dias = resto
idade_dias %= 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{idade_dias} dia(s)")
