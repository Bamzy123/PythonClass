message = """enter 1 for java
enter 2 for python: """

options = int (input(message))
match options:
	case 1:
		print("This is java")
	case 2:
		print("python is great")
	case _:
		print("default")