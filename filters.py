
from helpers import print_date_and_time
from transactions import format_transaction

def filter_transactions(transactions):
    print_date_and_time()
    if not transactions:
        print("❌ No transactions to filter.")
        return
    
    print("\nFilter by:")
    print("1. type (income/expense)")
    print("2. category")
    filter_choice = input("Choose filter type (1/2): ").strip()
    if filter_choice == "1":
        type_ = input("Enter type (income/expense): ").strip().lower()

        filtered_transactions = []
        for t in transactions:
            if t["type"].lower() == type_:
                filtered_transactions.append(t)

        if not filtered_transactions:
            print(f"❌ No transactions found of type '{type_}'.")
            return
        print(f"Transactions of type '{type_}':")
        for i, transaction in enumerate(filtered_transactions, start=1):
            print(format_transaction(i, transaction))
    elif filter_choice == "2":
        category = input("Enter category to filter by: ").strip().lower()

        filtered_transactions = []
        for t in transactions:
            if t["category"].lower() == category:
                filtered_transactions.append(t)

        if not filtered_transactions:
            print(f"❌ No transactions found in category '{category}'.")
            return

        print(f"Transactions in category '{category}':")
        for i, transaction in enumerate(filtered_transactions, start=1):
            print(format_transaction(i, transaction))