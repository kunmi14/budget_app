class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
    # Title centered with stars, total width = 30
        title = "\n" + self.name.center(40, "*") + "\n"

        items = ""
        for value in self.ledger:
            # Description max 23 characters (truncate if longer)
            desc = value["description"][:30]

            # Amount right aligned, 2 decimal places, width 7
            amount = f"${value['amount']:.2f}"

            """ 
            Format:
            The description is pushed to the left (<) in a 23-character space, 
            and the amount is pushed to the right (>) in a 7-character space.
            """
            items += f"{desc:<30}{amount:>10}\n"

        total = f"\nTotal: {f'${self.get_balance():.2f}':>33}\n"

        return title + items + total


    def deposit(self, amount, desc=""): 
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if not isinstance(desc, str):
            raise TypeError("Description must be a string")

        self.ledger.append(
            {
            "amount": amount,
            "description": desc
            }
        )
        return True
    
    # Loop through the list
    # Access each dictionary
    # Get its "amount"
    # Add them together
    def get_balance(self):
        total = 0
        for value in self.ledger:
            total += value["amount"]
        return total
    
    def withdraw(self, amount, desc=""):
        balance = self.get_balance()
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if not isinstance(desc, str):
            raise TypeError("Description must be a string")
        
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": desc})
            return True
        return False
    
    def transfer(self, amount, receiver, desc=""):
        balance = self.get_balance()

        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if not isinstance(desc, str):
            raise TypeError("Description must be a string")

        if self.check_funds(amount):
            # Withdraw from sender
            self.withdraw(amount, f"Transfer to {receiver.name}")
            # Deposit into receiver
            receiver.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")

        if amount > balance:
            return False
        
        return True

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

    return title + chart.rstrip("\n")


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
