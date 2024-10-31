import cmath

a = float(input("Enter a number a: "))
b = float(input("Enter a number b: "))
c = float(input("Enter a number c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print("The roots are real and distinct:", root1, root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("The root is real and repeated:", root)
else:
    realPart = -b / (2*a)
    imaginaryPart = (abs(discriminant)**0.5) / (2*a)
    root1 = complex(realPart, imaginaryPart)
    root2 = complex(realPart, -imaginaryPart)
    print("The roots are complex:", root1, root2)
