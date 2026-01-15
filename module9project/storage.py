import json
from financial import BudgetCategory, Expense

class JSONStorage:
    @staticmethod
    def save(manager, filename="data.json"):
        data = {
            "income": manager.income,
            "savings_goal": manager.savings_goal,
            "categories": {
                name: [
                    {
                        "amount": e.amount,
                        "description": e.description,
                        "date": e.date
                    }
                    for e in category.expenses
                ]
                for name, category in manager.categories.items()
            }
        }

        with open(filename, "w") as f:
            json.dump(data, f)

    @staticmethod
    def load(manager, filename="data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return

        manager.income = data.get("income", 0)
        manager.savings_goal = data.get("savings_goal", 0)

        for name, expenses in data.get("categories", {}).items():
            category = BudgetCategory(name)
            for e in expenses:
                category.add_expense(e["amount"], e["description"], e["date"])
            manager.categories[name] = category
