from datetime import datetime

def print_date_and_time():
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_balance(transactions):
    balance = 0.0
    for transaction in transactions:
        if transaction["type"] == "income":
            balance += transaction["amount"]
        else:
            balance -= transaction["amount"]
    return balance