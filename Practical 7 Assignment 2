# Initial balance
balance = 0

# Function to display balance
def display_balance():
    print("Current Balance:", balance)

# Function to deposit amount
def deposit_amount():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully.")

# Function to withdraw amount
def withdraw_amount():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Amount withdrawn successfully.")

# Menu loop
while True:
    print("\nBANK ACCOUNT MENU")
    print("1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_balance()
    elif choice == "2":
        deposit_amount()
    elif choice == "3":
        withdraw_amount()
    elif choice == "4":
        print("Thank you for using the Bank App!")
        break
    else:
        print("Invalid choice! Please try again.")
