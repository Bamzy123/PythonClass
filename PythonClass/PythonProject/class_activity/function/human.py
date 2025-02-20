import bcrypt

USER_DETAILS =  'user_details.txt'

def hashed_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(username, password):
    with open(USER_DETAILS, 'a') as file:
        file.write(f'{username}, {hashed_password.decode('utf-8')}\n')

def register_user():
    while True:
        username = input("Enter your username: ")
        if not username:
            print("Enter a valid username")
            continue
        break

    while True:
        password = input("Enter your password: ")
        if not password:
            print("Enter a valid password")
            continue
        break
    save_to_file(username, password)

def validate_user(username, password):
    with open(USER_DETAILS, 'r') as file:
        details = file.read()
        for line in details.split('\n'):
            stored_username, stored_password = line.split(':')
            print(stored_password)
            if username == stored_username:
                return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if validate_user(username, password):
        print("Login successful")

def main():
    menu = """
    1. register user
    2. Login user
    3. Exit
    """

    choice = input(menu)
    match choice:

        case '1':
            register_user()
        case '2':
            login_user()
        case '3':
            print("Thank you for logging in again")