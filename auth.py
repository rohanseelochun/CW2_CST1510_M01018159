import bcrypt
import os

USER_DATA_FILE = "users.txt"

# Hash password
def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode('utf-8')

# Verify password
def verify_password(plain_text_password, hashed_password):
    password_bytes = plain_text_password.encode('utf-8')
    hashed_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

# Check if user exists
def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, "r") as f:
        for line in f.readlines():
            user, _ = line.strip().split(",", 1)
            if user == username:
                return True
    return False

# Register user
def register_user(username, password):
    if user_exists(username):
        print(f"Error: Username '{username}' already exists.")
        return False
    hashed = hash_password(password)
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username},{hashed}\n")
    print(f"Success: User '{username}' registered!")
    return True

# Login user
def login_user(username, password):
    if not os.path.exists(USER_DATA_FILE):
        print("Error: No users registered yet.")
        return False
    with open(USER_DATA_FILE, "r") as f:
        for line in f.readlines():
            user, hashed = line.strip().split(",", 1)
            if user == username:
                if verify_password(password, hashed):
                    print(f"Success: Welcome, {username}!")
                    return True
                else:
                    print("Error: Invalid password.")
                    return False
    print("Error: Username not found.")
    return False

# Menu
def display_menu():
    print("\n" + "="*50)
    print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print(" Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)

def main():
    print("\nWelcome to the Week 7 Authentication System!")
    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()
        if choice == '1':
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()
            password = input("Enter a password: ").strip()
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue
            register_user(username, password)
        elif choice == '2':
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            login_user(username, password)
        elif choice == '3':
            print("\nThank you for using the authentication system.")
            break
        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()