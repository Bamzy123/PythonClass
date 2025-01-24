my_dict = {

	"name": "Stephen",
	"age": "20",
	"city": "Lagos",
	"skill": "Software Engineer",
}

#if "city" in my_dict:
#	print("city is in the dictionary")

#print(my_dict.get("names", "Not available"))

#for Key in my_dict:

#	print(Key, end = " ")

#for value in my_dict.values():

#	print(value, end = ' ')

#for Key, value in my_dict.items():

#	print(f"{Key}: {value}")

#squared = {x:x**2 for x in range(1, 6)}
#print(squared)

Keys = ["name", "age", "city"]
values = ["alice", "25", "new york"]

for Key,value in zip(Keys,values):
	my_dict[Key] = value
print(my_dict)