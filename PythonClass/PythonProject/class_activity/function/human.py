import string

name = 'ayo'
print (name)
print(id(name))
my_name = 'ayo'
print(my_name)
print(id(my_name))

my_name = name
print(id(my_name))
name += " mide"
print (name)
print(id(name))

print(name.split(" "))

print(name.strip())

names = ['esther', 'bimbola', 'stephen', 'moses']
print(", ".join(names))
letters = string.ascii_letters
print(letters)
print(list(letters))
print(", ".join(letters))
print("-".join(letters))
print("_".join(letters))
print(name)

username =  input("Enter your username: ")
if username.isspace():
    username = input("Enter your username: ")