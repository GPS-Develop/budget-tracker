import finance

transactions = finance.load_transactions()

while True:
    print("\n1. Add transaction")
    print("2. View transactions")
    print("3. View Balance")
    print("4. Delete transactions")
    print("5.Filter transactions")
    print("6. Quit")

    choice = input("Choose: ")

    if choice == "1":
        finance.add_transaction(transactions)
    elif choice == "2":
        finance.view_transactions(transactions)
    elif choice == "3":
        finance.view_balance(transactions)
    elif choice == "4":
        finance.delete_transaction(transactions)
    elif choice == "5":
        finance.filter_transactions(transactions)
    elif choice == "6":
        break
    else:
        print("Invalid choice")