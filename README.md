# 📒 Budget Tracker CLI

A simple and interactive command-line app to help you manage your income and expenses, built in Python.

---

## 🚀 Features

- ✅ Add income or expense transactions
- 📄 View all transactions
- 📊 See your current balance
- 🗑️ Delete specific transactions
- 🔍 Filter by category or type
- 🎲 Generate random test transactions
- 💾 Backup your data to a JSON file

---

## 🖥️ Demo

```bash
**📒 Welcome to Budget Tracker CLI
----------------------------------------

📌 Select an option:

1️⃣  Add Transaction
2️⃣  View Transactions  
3️⃣  View Balance  
4️⃣  Delete Transaction  
5️⃣  Filter Transactions  
6️⃣  Generate Random Transaction  
7️⃣  Backup Transactions  
8️⃣  ❌ Quit**
```
🛠️ Installation

1.   Clone the repo:
   ```
     git clone https://github.com/GPS-Develop/budget-tracker.git
     cd budget-tracker
```
     
2.	(Optional) Create a virtual environment:
   ```
     python3 -m venv venv
     source venv/bin/activate
```
3.	Install dependencies(if any)
   ```
pip install -r requirements.txt
```
Note: This app currently does not require external packages, but pytest is recommended for testing.

🧪 Running Tests
```
pytest
```

📁 File Structure
```
budget-tracker/
├── main.py                   # Main app logic
├── file_io.py                # Load/save and backup handling
├── transactions.py           # Add, view, delete, and balance functions
├── filters.py                # Category/type filtering
├── randomizer.py             # Generate dummy transactions
├── helpers.py                # Reusable utilities like balance calculation
├── test_helpers.py           # Pytest tests for helpers
├── test_transactions.py      # Pytest tests for formatting
├── transactions.json         # Your saved data
└── backup.json               # Optional backup copy
```
## 📌 Future Ideas
	•	Add date range filtering
	•	Export CSV summaries
	•	Add monthly budgeting reports
 ---

🙌 Author

Made with ❤️ by GPS-Develop

📜 License

This project is open source and free to use.
