accounts = {}
def display_welcome_message():
    print("Welcome to the Bank Management System!")

def display_menu():
    print("\nPlease select an option:")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in accounts and accounts[username]["password"] == password:
        print("Login successful!")
        account_menu(username)
    else:
        print("Invalid username or password. Please try again.")

def create_account():
    username = input("Enter a username: ")
    if username in accounts:
        print("Username already exists. Please choose another one.")
        return

    password = input("Enter a password: ")
    initial_balance = float(input("Enter initial balance: "))

    accounts[username] = {
        "password": password,
        "balance": initial_balance
    }
    print("Account created successfully!")

def view_account_details(username):
    print("\nAccount Details:")
    print("Username:", username)
    print("Balance:", accounts[username]["balance"])

def deposit(username):
    amount = float(input("Enter deposit amount: "))
    if amount <= 0:
        print("Invalid deposit amount.")
        return
    accounts[username]["balance"] += amount
    print("Deposit successful.")

def withdraw(username):
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid withdrawal amount.")
        return
    if amount > accounts[username]["balance"]:
        print("Insufficient balance.")
        return
    accounts[username]["balance"] -= amount
    print("Withdrawal successful.")

def transfer(username):
    recipient = input("Enter recipient's username: ")
    if recipient not in accounts:
        print("Recipient account not found.")
        return

    amount = float(input("Enter transfer amount: "))
    if amount <= 0:
        print("Invalid transfer amount.")
        return
    if amount > accounts[username]["balance"]:
        print("Insufficient balance.")
        return

    accounts[username]["balance"] -= amount
    accounts[recipient]["balance"] += amount
    print("Transfer successful.")

def logout():
    print("Logged out successfully.")

def save_accounts_to_file(filename):
    with open(filename, "w") as file:
        for username, account_info in accounts.items():
            file.write(f"{username},{account_info['password']},{account_info['balance']}\n")

def load_accounts_from_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                username, password, balance = line.strip().split(",")
                accounts[username] = {
                    "password": password,
                    "balance": float(balance)
                }
    except FileNotFoundError:
        pass

def account_menu(username):
    while True:
        print("\nAccount Menu:")
        print("1. View Account Details")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            view_account_details(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            withdraw(username)
        elif choice == "4":
            transfer(username)
        elif choice == "5":
            logout()
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    load_accounts_from_file("accounts.txt")

    while True:
        display_welcome_message()
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            create_account()
        elif choice == "3":
            save_accounts_to_file("accounts.txt")
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
