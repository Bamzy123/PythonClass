import math
polygon = int(input("Enter number of polygon sides: "))
length = float(input("Enter number one length of the sides: "))

area = (polygon * length**2) / (4 * math.tan(3.142857143 / polygon))

print  (f"The area is: {area}")