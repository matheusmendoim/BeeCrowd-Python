valor = float(input())

notas_100 = valor//100
valor %= 100

notas_50 = valor//50
valor %= 50

notas_20 = valor//20
valor %= 20

notas_10 = valor//10
valor %= 10

notas_5 = valor//5
valor %= 5

notas_2 = valor//2
valor %= 2

moedas_100 = valor//1
valor %= 1

moedas_50 = valor//0.50
valor %= 0.50

moedas_25 = valor//0.25
valor %= 0.25

moedas_10 = valor//0.10
valor %= 0.10

moedas_5 = valor//0.05
valor %= 0.05

moedas_1 = valor//0.01
valor %= 0.01

print(f"""NOTAS:
{notas_100:.0f} nota(s) de R$ 100.00
{notas_50:.0f} nota(s) de R$ 50.00
{notas_20:.0f} nota(s) de R$ 20.00
{notas_10:.0f} nota(s) de R$ 10.00
{notas_5:.0f} nota(s) de R$ 5.00
{notas_2:.0f} nota(s) de R$ 2.00
MOEDAS:
{moedas_100:.0f} moeda(s) de R$ 1.00
{moedas_50:.0f} moeda(s) de R$ 0.50
{moedas_25:.0f} moeda(s) de R$ 0.25
{moedas_10:.0f} moeda(s) de R$ 0.10
{moedas_5:.0f} moeda(s) de R$ 0.05
{moedas_1:.0f} moeda(s) de R$ 0.01""")