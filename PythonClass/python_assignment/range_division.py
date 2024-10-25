firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
thirdNumber = int(input("Enter third number: "))

count = 0

for integer in range (firstNumber, secondNumber + 1):

  if integer % thirdNumber == 0:

   count+=1

print (count)

