weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))

kilogram = weight * 0.45359237
meter = height * 0.0254

bmi = kilogram / (meter)**2

print(f"your BMI is: {bmi:.4f}")