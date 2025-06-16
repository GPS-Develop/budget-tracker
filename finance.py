import json
import os
import random
from datetime import datetime

BUDGET_FILE = "budget.json"

def load_transactions():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as f:
            return json.load(f)
    return []

def print_date_and_time():
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def save_transactions(transactions):
    with open(BUDGET_FILE, "w") as f:
        json.dump(transactions, f, indent=2)

def backup_file():
    print("Files in current dir:")
    print(os.listdir())
    if os.path.exists("budget.json"):
        os.rename("budget.json", "budget_backup.json")

def format_transaction(i, transaction):
    sign = "+" if transaction["type"] == "income" else "-"
    return f"{i}. {sign}${abs(transaction['amount']):.2f} | {transaction['description']} | {transaction['category']} | {transaction['type']}"

def generate_random_transaction(transactions):
    print_date_and_time()
    amount = random.uniform(1, 1000)
    description = random.choice(["Groceries", "Utilities", "Salary", "Entertainment", "Rent"])
    category = random.choice(["Food", "Bills", "Experiences", "Leisure"])
    type_ = random.choice(["income", "expense"])

    transaction = {
        "amount": round(amount, 2),
        "description": description,
        "category": category,
        "type": type_
    }

    transactions.append(transaction)
    try:
        save_transactions(transactions)
        print("✅ Random transaction added.")
    except (IOError, OSError) as e:
        print(f"❌ Failed to save transaction: {e}")

def add_transaction(transactions):
    print(datetime.now().strftime("\n%Y-%m-%d %H:%M:%S\n"))
    while True:
        amount_input = input("Enter amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("❌ Invalid amount. Please enter a numeric value.")

    while True:
        description = input("Enter description: ").strip()
        if description:
            break
        print("❌ Description cannot be empty.")

    while True:
        category = input("Enter category: ").strip().lower()
        if category:
            break
        print("❌ Category cannot be empty.")

    while True:
        type_ = input("Enter type (income/expense): ").strip().lower()
        if type_ in ("income", "expense"):
            break
        print("❌ Type must be 'income' or 'expense'.")

    transaction = {
        "amount": amount,
        "description": description,
        "category": category,
        "type": type_
    }

    transactions.append(transaction)
    try:
        save_transactions(transactions)
        print("✅ Transaction added.")
    except (IOError, OSError) as e:
        print(f"❌ Failed to save transaction: {e}")


def view_transactions(transactions):
    print_date_and_time()
    if not transactions:
        print("❌ No transactions found.")
        return

    for i, transaction in enumerate(transactions, start=1):
        print(format_transaction(i, transaction))

def calculate_balance(transactions):
    balance = 0.0
    for transaction in transactions:
        if transaction["type"] == "income":
            balance += transaction["amount"]
        else:
            balance -= transaction["amount"]
    return balance

def view_balance(transactions):
    balance = calculate_balance(transactions)
    print(f"Current balance: ${balance:.2f}")


def delete_transaction(transactions):
    print_date_and_time()
    view_transactions(transactions)
    if not transactions:
        return

    while True:
        try:
            index = int(input("Enter the transaction number to delete: ")) - 1
            if 0 <= index < len(transactions):
                deleted_transaction = transactions[index]["category"]
                del transactions[index]
                save_transactions(transactions)
                print(f'✅ {deleted_transaction} deleted.')
                return
            else:
                print("❌ Invalid transaction number.")
        except ValueError:
            print("❌ Please enter a valid number.")

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
            if t["type"] == type_:
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
            if t["category"] == category:
                filtered_transactions.append(t)

        if not filtered_transactions:
            print(f"❌ No transactions found in category '{category}'.")
            return

        print(f"Transactions in category '{category}':")
        for i, transaction in enumerate(filtered_transactions, start=1):
            print(format_transaction(i, transaction))



