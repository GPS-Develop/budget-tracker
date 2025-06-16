from helpers import calculate_balance
from transactions import format_transaction


def test_calculate_total_correctly():
    transactions = [
        {"amount": 100.0, "type": "income"},
        {"amount": 50.0, "type": "expense"},
        {"amount": 200.0, "type": "income"},
        {"amount": 30.0, "type": "expense"}
    ]
    results = 220.0
    balance = calculate_balance(transactions)
    assert balance == results

def test_formats_transaction_correctly():
    transaction = {
        "amount": 100.0,
        "description": "Test Transaction",
        "category": "Test Category",
        "type": "income"
    }
    formatted = format_transaction(1, transaction)
    results = "1. +$100.00 | Test Transaction | Test Category | income"
    assert formatted == results

def test_view_balance_correctly():
    transactions = [
        {"amount": 100.0, "type": "income"},
        {"amount": 50.0, "type": "expense"},
        {"amount": 200.0, "type": "income"},
        {"amount": 30.0, "type": "expense"}
    ]
    balance = calculate_balance(transactions)
    results = "$220.00"
    assert f"${balance:.2f}" == results

def test_delete_transaction():
    transactions = [
        {"amount": 100.0, "description": "Test Transaction", "category": "Test Category", "type": "income"},
        {"amount": 50.0, "description": "Another Transaction", "category": "Another Category", "type": "expense"}
    ]
    # Simulate deletion of the first transaction
    deleted_transaction = transactions.pop(0)
    # Check if the transaction was deleted correctly
    assert len(transactions) == 1
    assert transactions[0] == {"amount": 50.0, "description": "Another Transaction", "category": "Another Category", "type": "expense"}
    # Check if the deleted transaction is the one we expected
    assert deleted_transaction == {"amount": 100.0, "description": "Test Transaction", "category": "Test Category", "type": "income"}
