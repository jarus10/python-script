import hashlib
import getpass

pasword_manager = {}

def create_account():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    pasword_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in pasword_manager.keys() and pasword_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password")

def main():
    while True:
        choice = input(" (1) Create an account or (2) Login? (0 to quit): ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice.lower() == '0':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":  # Run the main function
    main()

