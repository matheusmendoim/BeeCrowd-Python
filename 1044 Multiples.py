a, b = map(int, input().split())

lista = [a, b]
lista.sort()

if (lista[1]%lista[0]) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
