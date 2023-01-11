code_product1, units_product1, price_product1 = map(float, input().split())
code_product2, units_product2, price_product2 = map(float, input().split())

valor = (units_product1*price_product1) + (units_product2*price_product2)

print(f"VALOR A PAGAR: R$ {valor:.2f}")