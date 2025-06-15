import json
import os

BUDGET_FILE = "budget.json"

def load_transactions():
    if os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "r") as f:
            return json.load(f)
    return []

def save_transactions(transactions):
    with open(BUDGET_FILE, "w") as f:
        json.dump(transactions, f, indent=2)

def add_transaction(transactions):
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
    if not transactions:
        print("No transactions found.")
        return

    for i, transaction in enumerate(transactions, start=1):
        if transaction["type"] == "income":
            sign = "+"
        else:
            sign = "-"
        print(f"{i}. {sign}${abs(transaction['amount']):.2f} | {transaction['description']} | {transaction['category']} | {transaction['type']}")


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
                print(f'{deleted_transaction} deleted.')
                return
            else:
                print("❌ Invalid transaction number.")
        except ValueError:
            print("❌ Please enter a valid number.")
    