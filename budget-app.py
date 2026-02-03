class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        result = title + "\n"
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"
            result += f"{desc:<23}{amt:>7}\n"
        result += f"Total: {self.get_balance():.2f}"
        return result


def create_spend_chart(categories):
    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)
    percentages = [(s / total_spent) * 100 for s in spent]
    percentages = [int(p // 10 * 10) for p in percentages]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name for cat in categories]

    for i in range(max_len):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart
