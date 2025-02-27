import re

import bcrypt

USER_DETAILS =  'user_details.txt'

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(user_email, hashed_password):
    with open(USER_DETAILS, 'a') as file:
        file.write(f'{user_email}:{hashed_password.decode('utf-8')}\n')

def register_user():
    while True:
        user_email = input("Enter your user_email: ")
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', user_email):
            print("Please enter a valid user_email")
            continue
        break

    while True:
        password = input("Enter your password: ")
        if not password:
            print("Enter a valid password")
            continue
        break
    save_to_file(user_email, hash_password(password))

def validate_user(user_email, password):
    with open(USER_DETAILS, 'r') as file:
        details = file.read()
        for line in details.split('\n'):
            stored_user_email, stored_password = line.split(':')
            # print(stored_password)
            if user_email == stored_user_email:
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

def login_user():
    user_email = input("Enter your username: ")
    password = input("Enter your password: ")
    if validate_user(user_email, password):
        print("Login successful")
    else:
        print("Invalid details")

def main():
    menu = """
    1. register user
    2. Login user
    3. Exit
    """
    while True:
        choice = input(menu)
        match choice:
            case '1':
                register_user()
            case '2':
                login_user()
            case '3':
                print("Thank you for logging in again")
main()