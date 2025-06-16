from file_io import load_transactions, backup_file
from transactions import add_transaction, view_transactions, delete_transaction, view_balance
from filters import filter_transactions
from randomizer import generate_random_transaction

transactions = load_transactions()

while True:
    print("\n📒 Welcome to Budget Tracker CLI")
    print("-" * 40)
    print("\n📌 Select an option:\n")
    print("1️⃣  Add Transaction")
    print("2️⃣  View Transactions")
    print("3️⃣  View Balance")
    print("4️⃣  Delete Transaction")
    print("5️⃣  Filter Transactions")
    print("6️⃣  Generate Random Transaction")
    print("7️⃣  Backup Transactions")
    print("8️⃣  ❌ Quit\n")

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
        print("⚠️ Invalid choice")