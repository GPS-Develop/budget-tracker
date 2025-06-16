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

def backup_file():
    print("Files in current dir:")
    print(os.listdir())
    if os.path.exists("budget.json"):
        os.rename("budget.json", "budget_backup.json")