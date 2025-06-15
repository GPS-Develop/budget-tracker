import finance

transactions = finance.load_transactions()

while True:
    print("\n1. Add transaction")
    print("2. Quit")

    choice = input("Choose: ")

    if choice == "1":
        finance.add_transaction(transactions)
    elif choice == "2":
        break
    else:
        print("Invalid choice")