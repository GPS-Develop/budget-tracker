from file_io import load_transactions, backup_file
from transactions import add_transaction, view_transactions, delete_transaction, view_balance
from filters import filter_transactions
from randomizer import generate_random_transaction

transactions = load_transactions()

while True:
    print("\n1. Add transaction")
    print("2. View transactions")
    print("3. View Balance")
    print("4. Delete transactions")
    print("5. Filter transactions")
    print("6. Generate random transaction")
    print("7. Backup transactions")
    print("8. Quit")

    choice = input("Choose: ")

    if choice == "1":
        add_transaction(transactions)
    elif choice == "2":
        view_transactions(transactions)
    elif choice == "3":
        view_balance(transactions)
    elif choice == "4":
        delete_transaction(transactions)
    elif choice == "5":
        filter_transactions(transactions)
    elif choice == "6":
        generate_random_transaction(transactions)
    elif choice == "7":
        backup_file()
    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice")