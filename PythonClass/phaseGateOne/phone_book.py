import sys

def phone_book():
	phone_book = {}

	while True:
		print("Welcome to your phonebook!\n")
		print("1. Add contact.")
		print("2. Remove contact.")
		print("3. Find contact by phone number.")
		print("4. Find contact by first name.")
		print("5. Find contact by last name.")
		print("6. Edit contact.")
		print("7. Exit.")
		choice = input("Choose an option: ")

		if choice == '1':
			name = input("Enter your contact's name: ")
			phone_number = input("Enter your contact's phone number: ")
			phone_book[phone_number] = name
			print("Contact added successfully!\n")

		elif choice == '2':
            		remove_contact = input("Enter the phone number of the contact you want to remove: ")
            		if remove_contact in phone_book:
                		del phone_book[remove_contact]
                		print("Contact removed successfully!\n")
            		else:
                		print("Contact not found!\n")

		elif choice == '3':
            		search_number = input("Enter the phone number to find the contact: ")
            		if search_number in phone_book:
                		print(f"Contact found: {phone_book[search_number]}\n")
            		else:
                		print("Contact not found!\n")

		elif choice == '4':
            		first_name = input("Enter the first name to find contact: ")
            		found_first_name = False
            		for number, name in phone_book.items():
                		if name.startswith(first_name):
                    			print(f"Found contact: {name} - {number}")
                    			found_first_name = True
            		if not found_first_name:
                		print("No contact found with that first name.\n")

		elif choice == '5':
			last_name = input("Enter the last name to find contact: ")
			found_last_name = False
			for number, name in phone_book.items():
				if name.endswith(last_name):
					print(f"Found contact: {name} - {number}")
					found_last_name = True
				if not found_last_name:
					print("No contact found with that last name.\n")

		elif choice == '6':
			number_to_edit = input("Enter the phone number of the contact you want to edit: ")
			if number_to_edit in phone_book:
				new_name = input("Enter the new name for the contact: ")
				phone_book[number_to_edit] = new_name
				print("Contact updated successfully!\n")
			else:
				print("Contact not found!\n")

		elif choice == '7':
			print("Exiting your phonebook.")
			sys.exit()

		else:
			print("Invalid option, please try again.\n")

phone_book()