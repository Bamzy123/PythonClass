principal = int(input("Enter principal (original amount invested): $"))
annual = float(input("Enter annual rate of return: "))
years = int(input("Enter number of years: "))

investment_return = principal * (1 + annual)**years

print(f"The amount after{years}: ${investment_return:}")