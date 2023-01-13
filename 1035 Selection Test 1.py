a, b, c, d = map(int, input().split())
confirmador = False

if b > c and d > a:
    confirmador == True
if (c+d)>(a+c):
    confirmador == True
if c > 0 and d > 0:
    confirmador == True
if a % 2 == 0:
    confirmador == True

if confirmador == True:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")