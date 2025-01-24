first_number = int(input("enter number between 100 to 999: "))
result1: int = (first_number // 100)
result2: int = (first_number // 10) % 10
result3: int = (first_number % 10)

print (result3, result2, result1)

odd_counter = 0
even_counter = 0

if (result3 % 2 ==0):
	even_counter+=1
else:
	odd_counter+=1

if (result2 % 2 ==0):
	even_counter+=1
else:
	odd_counter+=1

if (result1 % 2 ==0):
	even_counter+=1
else:
	odd_counter+=1

print ("even number is", even_counter)
print ("odd number is", odd_counter)