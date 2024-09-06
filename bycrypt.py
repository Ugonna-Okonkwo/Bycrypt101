import bcrypt
import getpass

#Dictionary to store username and hashed password
password_manager = {}

def create_account():
    username = input("\nEnter your username: ")
    if not username:
        print("Username cannot be empty!")
        return
    password = getpass.getpass("\nEnter your password: ").encode()  #Ensure password is encoded
    if not password:
        print("Password cannot be empty!")
        return
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())  #Hash password with salt using bycrypt
    password_manager[username] = hashed_password
    print("\nAccount created successfully!")

def login():
    username = input("\nEnter your username: ")
    if not username:
        print("Username cannot be empty!")
        return
    password = getpass.getpass("\nEnter your password: ").encode()  #Ensure password is encoded
    if not password:
        print("Password cannot be empty!")
        return
    hashed_password = password_manager.get(username)
    if hashed_password and bcrypt.checkpw(password, hashed_password):  #Verify password input
        print("\nLogin successful!")
    else:
        print("\nInvalid username or password. Please try again!")

def main():
    while True:
        choice = input("What would you like to do?"
                       "\n[1] Create an account"
                       "\n[2] Login"
                       "\n[3] Exit"
                       "\n "
                       "\nChoice = ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("\nInvalid choice. Please select a number from the list of options!")

if __name__ == "__main__":
    main()