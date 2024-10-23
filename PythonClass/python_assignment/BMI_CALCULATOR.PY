weightInPounds = float(input("Enter weight in pounds: "))
heightInches = float(input("Enter height in inches: "))

bmi = weightInPounds * 703 / heightInches * heightInches

print (f"Your BMI is {bmi} ")