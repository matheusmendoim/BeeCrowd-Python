nota1, nota2, nota3, nota4 = map(float, input().split())

peso1, peso2, peso3, peso4 = 2, 3, 4, 1

media = (((nota1*peso1)+(nota2*peso2)+(nota3*peso3)+(nota4*peso4))/(peso1+peso2+peso3+peso4))


if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")

elif media < 5.0:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
    
else:
    exame = float(input())

    nova_media = ((media+exame)/2)

    print(f"Media: {media}")
    print("Aluno em exame.")
    print(f"Nota do exame: {exame:.1f}")

    if nova_media >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {nova_media:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {nova_media:.1f}")
