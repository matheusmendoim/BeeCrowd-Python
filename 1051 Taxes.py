salary = float(input())

taxe = 0

if salary <= 2000:
    print("Isento")

else:
    if salary > 2000 and salary <= 3000:
        salary -= 2000
        taxe = (salary*(8/100))

    elif salary > 3000 and salary <= 4500:
        salary -= 2000
        resto = salary-1000
        taxe += (resto*(18/100))
        taxe += (salary-resto)*(8/100)

    else:
        salary -= 2000
        resto = salary-1000
        taxe += (resto*(18/100))
        taxe += (salary-res
        to)*(8/100)

    print(f"R$ {taxe:.2f}")
