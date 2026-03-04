balance = 0

def show_menu():
    print("\n==== Income Tracker ====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Select an option: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        balance += amount
        print(f"Income added. Current balance: {balance}")

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        balance -= amount
        print(f"Expense recorded. Current balance: {balance}")

    elif choice == "3":
        print(f"Current balance: {balance}")

    elif choice == "4":
        print("Exiting Income Tracker.")
        break

    else:
        print("Invalid option. Try again.")
