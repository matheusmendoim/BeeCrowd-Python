valor = int(input())

print(valor)

notas_100 = valor//100
valor %= 100

notas_50 = valor//50
valor %= 50

notas_25 = valor//20
valor %= 20

notas_10 = valor//10
valor %= 10

notas_5 = valor//5
valor %= 5

notas_2 = valor//2
valor %= 2

notas_1 = valor//1

print(f"""{notas_100} nota(s) de R$ 100,00
{notas_50} nota(s) de R$ 50,00
{notas_25} nota(s) de R$ 20,00
{notas_10} nota(s) de R$ 10,00
{notas_5} nota(s) de R$ 5,00
{notas_2} nota(s) de R$ 2,00
{notas_1} nota(s) de R$ 1,00""")