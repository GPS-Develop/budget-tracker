import unittest
from helpers import calculate_balance
from transactions import format_transaction

class TestHelpers(unittest.TestCase):
    def test_calculate_total_correctly(self):
        transactions = [
            {"amount": 100.0, "type": "income"},
            {"amount": 50.0, "type": "expense"},
            {"amount": 200.0, "type": "income"},
            {"amount": 30.0, "type": "expense"}
        ]
        results = 220.0
        balance = calculate_balance(transactions)
        self.assertEqual(balance, results)

    def test_formats_transaction_correctly(self):
        transaction = {
            "amount": 100.0,
            "description": "Test Transaction",
            "category": "Test Category",
            "type": "income"
        }
        formatted = format_transaction(1, transaction)
        results = "1. +$100.00 | Test Transaction | Test Category | income"
        self.assertEqual(formatted, results)
    

if __name__ == "__main__":
    unittest.main()
