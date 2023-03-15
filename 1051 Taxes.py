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
        rest = salary-1000
        taxe += (rest*(18/100))
        taxe += ((salary-rest)*(8/100))

    else:
        salary -= 2000
        rest = salary-1000
        rest2 = salary-2500
        taxe += rest2*(28/100)
        taxe += abs(rest-rest2)*(18/100)
        taxe += abs(salary-rest)*(8/100)
        
    print(f"R$ {taxe:.2f}")