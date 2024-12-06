def atm_app():
	account_name = ""
	balance = 0.0
	pin = -1
	choice = 0

	while choice != 8:
		print("Welcome to the ATM!")
		print("1. Account Name")
		print("2. Create your pin")
		print("3. Deposit")
		print("4. Withdraw")
		print("5. Check Balance")
		print("6. Change Pin")
		print("7. Transfer to another account")
		print("8. Close account")
		choice = int(input("Choose an option: "))

		if choice == 1:
			account_name = input("Enter your First and Last name: ")
			print(f"Account name set to: {account_name}")

		elif choice == 2:
			pin = int(input("Enter your pin: "))
			print("Pin set successfully.")

		elif choice == 3:
			deposit_amount = float(input("Enter amount to deposit: "))
			if deposit_amount > 0:
				balance += deposit_amount
				print(f"Deposited: ${deposit_amount}")
			else:
				print("Please enter a valid amount.")

		elif choice == 4:
			withdraw_amount = float(input("Enter amount to withdraw: "))
			if withdraw_amount > 0 and withdraw_amount <= balance:
				balance -= withdraw_amount
				print(f"Withdrawn: ${withdraw_amount}")
			else:
				print("Invalid withdrawal amount.")

		elif choice == 5:
			print(f"Current balance: ${balance}")

		elif choice == 6:
			old_pin = int(input("Enter your old pin: "))
			if old_pin == pin:
				new_pin = int(input("Enter your new pin: "))
				pin = new_pin
				print("Pin changed successfully.")
			else:
				print("Incorrect old pin. Please try again.")

		elif choice == 7:
			input_pin = int(input("Enter your pin: "))
			if input_pin == pin:
				transfer_amount = float(input("Enter amount you want to transfer: "))
				if transfer_amount > 0 and transfer_amount <= balance:
					balance -= transfer_amount
					print(f"Transferred: ${transfer_amount}")
				else:
					print("Transfer failed: Insufficient funds or invalid amount.")

			else:
				print("Incorrect pin. Transfer not possible.")

		elif choice == 8:
			print("THANKS FOR USING THE ATM, GOODBYE!")
        
		else:
			print("Invalid option. Please try again.")


atm_app()