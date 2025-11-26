#Step 3
import bcrypt
import os

#Step 4
def hash_password(text_password):
    #Converts password into bytes.
    text_password = text_password.encode("utf-8")
    #Generates a random salt.
    salt = bcrypt.gensalt()
    #Hash the password with the random salt.
    hashed_password = bcrypt.hashpw(text_password, salt)
    #Converts the hashed_password from bytes to UTF-8.
    return hashed_password.decode("utf-8")

#Step 5
def verify_password(text_password, hashed_password):
    #Converts the password into bytes.
    password_1 = text_password.encode("utf-8")
    #Converts the hash into bytes.
    hash_2 = hashed_password.encode("utf-8")
    #Compares both the password & hash.
    return bcrypt.checkpw(password_1, hash_2)

#Step 6
USER_DATA_FILE = "users.txt"

#Step 7
def register_user(username, password):
    #Checks if username already exists.
    if user_exists(username):
        print(f"Error: Username '{username}' already exists.")
        return False
    else:
        #Hash the password.
        hashed_password = hash_password(password)
        #Opening "users.txt" file in append mode.
        with open(USER_DATA_FILE, "a") as f:
            f.write(f"{username},{hashed_password}\n")
        print(f"Success: User '{username}' registered successfully.")
        return True

#Step 8
def user_exists(username):
    #Checks "users.txt" file if the data exists.
    if not os.path.isfile(USER_DATA_FILE):
        return False
    #Opens "users.txt" file in read mode.
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            stored_username = line.strip(). split(",", 1)[0]
            if username == stored_username:
                return True
    return False

#Step 9
def login_user(username, password):
    #If no username data found in "users.txt" then displays a text.
    if not os.path.exists(USER_DATA_FILE):
        print("Username does not exist.")
        return False

    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            stored_username, stored_hash = line.strip().split(",", 1)
            if username == stored_username:
                #Verify if both the password & stored_hash are the same then display a text.
                if verify_password(password, stored_hash):
                    print(f"Success: Welcome, {username}!")
                    return True
                else:
                    print("Error: Invalid password.")
                    return False
    #Loop ends only If no correct username is typed.
    print("Error: Username not found.")
    return False

#Step 10
def validate_username(username):
    #Checks the length of the username & displayed a text if condition is not met.
    if len(username) < 3 or len(username) > 20:
        return False, "Username must be between 3 and 20 characters."
    #Checks if the user is alphanumeric & displayed a text if condition is false.
    if not username.isalnum():
        return False, "Username must contain only letters and numbers."
    return True, ""

def validate_password(password):
    if len(password) < 6 or len(password) > 50:
        return False, "Password must be between 6-50 characters."
    return True, ""

#Step 11
def display_menu():
    """Displays the main menu options."""
    print("\n" + "=" * 50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("=" * 50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-" * 50)


def main():
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()

            # Validate username
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            password = input("Enter a password: ").strip()
            # Validate password
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            # Confirm password
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue

            # Register the user
            register_user(username, password)

        elif choice == '2':
            # Login flow
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Attempt login
            if login_user(username, password):
                print("\nYou are now logged in.")
                print("(In a real application, you would now access the dashboard.)")

                # Optional: Ask if they want to logout or exit
                input("\nPress Enter to return to main menu...")

        elif choice == '3':
            # Exit
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break

        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()