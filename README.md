# 💰 Budget App (Category Class & Spend Chart)

A simple object-oriented **budget management system** built with Python.

This project demonstrates:
- Object-Oriented Programming (OOP)
- Data structures (lists & dictionaries)
- String formatting
- Algorithmic thinking (percentage calculations & chart generation)


## 🚀 Features

### 📦 Category Class

The `Category` class allows you to:

- ✅ Deposit money
- ✅ Withdraw money (with balance validation)
- ✅ Transfer funds between categories
- ✅ Check available funds
- ✅ Display a formatted ledger
- ✅ Get current balance

Each category maintains its own transaction history (ledger).


## 📊 Spend Chart

The `create_spend_chart()` function:

- Calculates total withdrawals per category
- Computes percentage spent (rounded down to nearest 10)
- Generates a vertical bar chart
- Displays category names vertically
- Returns a formatted string representation of the chart

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")
