from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Category:
    name: str
    ledger: List[Dict[str, float]] = field(default_factory=list)

    def __str__(self):
        title = "\n" + self.name.center(40, "*") + "\n"

        items = ""
        for value in self.ledger:
            desc = value["description"][:30]
            amount = f"${value['amount']:.2f}"
            items += f"{desc:<30}{amount:>10}\n"

        total = f"\nTotal: {f'${self.get_balance():.2f}':>33}\n"
        return title + items + total

    def get_balance(self):
        return sum(value["amount"] for value in self.ledger)

    def check_funds(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a Number")

        if amount > self.get_balance():
            return False
        return True

    def deposit(self, amount, desc=""):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a Number")

        if not isinstance(desc, str):
            raise TypeError("Description must be a string")

        if amount < 0:
            raise ValueError("Amount must be greater than 0")

        self.ledger.append({
            "amount": amount,
            "description": desc
        })

        return True

    def withdraw(self, amount, desc=""):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a Number")

        if not isinstance(desc, str):
            raise TypeError("Description must be a string")

        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": desc
            })
            return True

        return False

    def transfer(self, amount, receiver, desc=""):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a Number")

        if not isinstance(desc, str):
            raise TypeError("Description must be a string")

        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {receiver.name}")
            receiver.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

# We are creating a function: It takes a list of Category objects (like Food, Clothing, Auto).
def create_spend_chart(categories):
    title = "Percentage spent by category".center(40, "*") + "\n"

    # 1️⃣ Calculate Money Spent
    # spent will store how much each category spent.
    # total_spent will store the total spent across ALL categories.
    spent = []
    total_spent = 0

    # Loop through each category (Food, Clothing, etc.).
    for category in categories:
        category_total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                category_total += -item["amount"]
        spent.append(category_total)
        total_spent += category_total

    # 2️⃣ Calculate percentages rounded DOWN to nearest 10
    percentages = []
    for amount in spent:
        percent = (amount / total_spent) * 100
        percentages.append(int(percent // 10) * 10)

    # 3️⃣ Build chart body
    chart = ""

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # 4️⃣ Add horizontal line
    chart += " " * 3 + "-" * (len(categories) * 3 + 1) + "\n"

    # 5️⃣ Write Category Names Vertically
    max_length = max(len(category.name) for category in categories)

    for i in range(max_length):
        line = " " * 5
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        chart += line + "\n"

    return title + chart

# Use case
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
food.check_funds(1000)
print(food)

food = Category("Food")
food.deposit(1000)
food.withdraw(105.55)

clothing = Category("Clothing")
clothing.deposit(500)
clothing.withdraw(33.40)

auto = Category("Auto")
auto.deposit(1000)
auto.withdraw(15)

print(create_spend_chart([food, clothing, auto]))


