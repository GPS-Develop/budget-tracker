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
    try:
        amount_input = input("Enter amount: ")
        amount = float(amount_input)
    except ValueError:
        print("❌ Invalid amount. Please enter a numeric value.")
        return

    description = input("Enter description: ").strip()
    if not description:
        print("❌ Description cannot be empty.")
        return

    category = input("Enter category: ").strip().lower()
    if not category:
        print("❌ Category cannot be empty.")
        return

    type_ = input("Enter type (income/expense): ").strip().lower()
    if type_ not in ("income", "expense"):
        print("❌ Type must be 'income' or 'expense'.")
        return

    transaction = {
        "amount": amount,
        "description": description,
        "category": category,
        "type": type_
    }

    transactions.append(transaction)
    try:
        save_transactions(transactions)
        print(f"❌ '{type_}' is invalid. Type must be 'income' or 'expense'.")
    except (IOError, OSError) as e:
        print(f"❌ Failed to save transaction: {e}")