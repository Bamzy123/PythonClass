from Functions.bank import Banks


def atm_app():
    bank = Banks()

    while True:
        print("\n==== Main Menu ====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Update PIN")
        print("6. Check Balance")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            name = input("Enter your name: ").strip()
            pin = input("Enter your PIN: ").strip()
            try:
                account_number = bank.create_account(pin, name)
                print(f"Account created successfully. Your account number is {account_number}.")
            except Exception as e:
                print(f"Error creating account: {e}")

        elif choice == '2':
            try:
                account_number = int(input("Enter your account number: ").strip())
                amount = float(input("Enter deposit amount: ").strip())
                bank.deposit(account_number, amount)
                print("Deposit successful.")
            except Exception as e:
                print(f"Error during deposit: {e}")

        elif choice == '3':
            try:
                account_number = int(input("Enter your account number: ").strip())
                amount = float(input("Enter withdrawal amount: ").strip())
                pin = input("Enter your PIN: ").strip()
                bank.withdraw(account_number, amount, pin)
                print("Withdrawal successful.")
            except Exception as e:
                print(f"Error during withdrawal: {e}")

        elif choice == '4':
            try:
                sender_account = int(input("Enter your account number: ").strip())
                receiver_account = int(input("Enter receiver's account number: ").strip())
                amount = float(input("Enter amount to transfer: ").strip())
                pin = input("Enter your PIN: ").strip()
                bank.transfer(sender_account, receiver_account, amount, pin)
                print("Transfer successful.")
            except Exception as e:
                print(f"Error during transfer: {e}")

        elif choice == '5':
            try:
                account_number = int(input("Enter your account number: ").strip())
                old_pin = input("Enter your current PIN: ").strip()
                new_pin = input("Enter your new PIN: ").strip()
                bank.update_pin(account_number, old_pin, new_pin)
                print("PIN updated successfully.")
            except Exception as e:
                print(f"Error updating PIN: {e}")

        elif choice == '6':
            try:
                account_number = int(input("Enter your account number: ").strip())
                pin = input("Enter your PIN: ").strip()
                account = bank.get_account(account_number)
                balance = account.check_balance(pin)
                print(f"Your account balance is: {balance}")
            except Exception as e:
                print(f"Error checking balance: {e}")

        elif choice == '7':
            print("Exiting your bank app, Thank you for using our banking system!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    atm_app()