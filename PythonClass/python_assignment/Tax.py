first_income = int(input("enter first persons income: "))
second_income = int(input("enter second person income: "))
third_income = int(input("enter third person income: "))

income_list = first_income, second_income, third_income
first_tax_rate = 15 / 100
second_tax_rate = 20 / 100

for a in income_list:
    if a > 0 and a <= 30000:
        rate = a * first_tax_rate
        print(rate)
    elif a > 30000:
        rate = a * second_tax_rate
        print(rate)
