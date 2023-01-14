produto, quantidade = map(int, input().split())

if produto == 1:
    total = quantidade*(4.00)

elif produto == 2:
    total = quantidade*(4.50)

elif produto == 3:
    total = quantidade*(5.00)

elif produto == 4:
    total = quantidade*(2.00)

elif produto == 5:
    total = quantidade*(1.50)

print(f"Total: R$ {total:.2f}")
