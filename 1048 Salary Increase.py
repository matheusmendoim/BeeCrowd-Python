salary = float(input())


def salary_increase(salary, percentual):
    new_salary = salary+(salary*(percentual))
    readjustment = new_salary-salary
    percentual *= 100

    print(f"Novo salario: {new_salary:.2f}")
    print(f"Reajuste ganho: {readjustment:.2f}")
    print(f"Em percentual: {percentual:.0f} %")


if salary <= 400:
    salary_increase(salary, percentual=(15/100))

elif salary > 400 and salary <= 800:
    salary_increase(salary, percentual=(12/100))

elif salary > 800 and salary <= 1200:
    salary_increase(salary, percentual=(10/100))

elif salary > 1200 and salary <= 2000:
    salary_increase(salary, percentual=(7/100))

else:
    salary_increase(salary, percentual=(4/100))
