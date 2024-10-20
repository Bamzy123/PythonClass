principal = int(input("Enter principal loan amount: $"))
annual_interest_rate = float(input("Enter annual interest rate (as a percentage): ")) / 100
duration_years = int(input("Enter the duration of the loan in years: "))

monthly_interest_rate = annual_interest_rate / 12
    
total_payments = duration_years * 12
    
monthly_payment = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments / ((1 + monthly_interest_rate) ** total_payments - 1)

print(f"\nYour monthly mortgage payment is: ${monthly_payment:.2f}")
