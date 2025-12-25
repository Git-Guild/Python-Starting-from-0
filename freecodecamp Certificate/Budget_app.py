#TODO: Build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

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
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
        output = title + items + "Total: " + str(self.get_balance())
        return output

def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    total_spent = sum(spent_amounts)
    percentages = []
    if total_spent > 0:
        for amount in spent_amounts:
            percentages.append(int((amount / total_spent) * 100) // 10 * 10)
    else:
        percentages = [0] * len(categories)

    header = "Percentage spent by category\n"
    chart = ""
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names) if names else 0
    names_str = ""
    for i in range(max_len):
        names_str += "     "
        for name in names:
            if i < len(name):
                names_str += name[i] + "  "
            else:
                names_str += "   "
        if i < max_len - 1:
            names_str += "\n"

    return header + chart + footer + names_str