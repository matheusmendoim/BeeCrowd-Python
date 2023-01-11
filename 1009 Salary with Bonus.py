nome_empregado = input()
salario_fixo = float(input())
vendas_empregado = float(input())

salario_bonus = (salario_fixo)+(vendas_empregado*0.15)

print(f"TOTAL = R$ {salario_bonus:.2f}")