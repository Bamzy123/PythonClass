largest = 0
smallest = 0
for count in range(1,11):
    score = int(input(f"Enter number {count} : "))
    if score > 0 and score <= 100:
      if score > largest:
       largest = score
       smallest = score
print(f"The largest score is {largest}")
print(f"The smallest score is {smallest}")