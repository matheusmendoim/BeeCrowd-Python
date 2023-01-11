A, B, C = map(float, input().split())

PI = 3.14159

triangulo = (A*C)/2
circulo = PI*(C**2)
trapezio = 0.5*(A+B)*C
quadrado = B**2
retangulo = A*B

print(f"""TRIANGULO: {triangulo:.3f}
CIRCULO: {circulo:.3f}
TRAPEZIO: {trapezio:.3f}
QUADRADO: {quadrado:.3f}
RETANGULO: {retangulo:.3f}""")