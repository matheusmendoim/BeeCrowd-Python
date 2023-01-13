a, b, c, d = map(int, input().split())
confirmador = False

if b>c and d>a:
    if (c+d)>(a+b):
        if c>0 and d>0:
            if a%2==0:
                confirmador = True

if confirmador == True:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
