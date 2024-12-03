"""
def add_number(add):

	return sum([i for i in add])

add = 1,9,2,3,7,4

print(add_number(add))
"""
def add_number(add):

	return sum(map(lambda i:add))

print(add_number(add))