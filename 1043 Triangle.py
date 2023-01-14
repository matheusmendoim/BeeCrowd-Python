a, b, c = map(float, input().split())

if not((c>abs(a-b)) and (c<(a+b))):
    area_trapezio = ((a+b)*c)/2
    print(f"Area = {area_trapezio:.1f}")
else:
    perimetro = a+b+c
    print(f"Perimetro = {perimetro:.1f}")
