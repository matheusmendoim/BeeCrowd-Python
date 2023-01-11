def troco(valor, notas_em_x):
    notas = valor//notas_em_x
    valor %= notas_em_x
    return notas


valor = int(input())

print(valor)

print(f"""{troco(valor, 100)} nota(s) de R$ 100,00
{troco(valor, 50)} nota(s) de R$ 50,00
{troco(valor, 25)} nota(s) de R$ 25,00
{troco(valor, 10)} nota(s) R$ 10,00
{troco(valor, 5)} nota(s) de R$ 5,00
{troco(valor, 2)} nota(s) de R$ 2,00
{troco(valor, 1)} nota(s) de R$ 1,00""")