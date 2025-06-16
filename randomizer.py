import random
from helpers import print_date_and_time
from file_io import save_transactions

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