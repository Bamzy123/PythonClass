# Print table header
print("Number\tSquare\tCube")

for number in range(6):
    square = number ** 2
    cube = number ** 3
    print(f"{number}\t{square}\t{cube}")
