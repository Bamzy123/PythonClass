num = int(input("Enter a number between 0 and 1000: "))

calculate = num // 100
calculate1 = num % 100
calculate2 = calculate1 // 10
calculate3 = calculate2 % 10

sum = calculate + calculate2 + calculate3

print(sum)