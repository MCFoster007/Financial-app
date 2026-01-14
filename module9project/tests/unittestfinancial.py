import unittest
from module9project.financial import Expense, Income, FinancialTracker
class TestFinancialTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = FinancialTracker()
    
    def test_add_expense(self):
        self.tracker.add_expense("Food", 50.0, "Groceries", "2024-01-15")
        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertEqual(self.tracker.expenses[0].category, "Food")
        self.assertEqual(self.tracker.expenses[0].amount, 50.0)
    
    def test_add_income(self):
        self.tracker.add_income(2000.0, "Salary", "2024-01-01")
        self.assertEqual(len(self.tracker.incomes), 1)
        self.assertEqual(self.tracker.incomes[0].amount, 2000.0)
    
    def test_total_expenses(self):
        self.tracker.add_expense("Food", 50.0, "Groceries", "2024-01-15")
        self.tracker.add_expense("Transport", 20.0, "Bus fare", "2024-01-16")
        total = self.tracker.total_expenses()
        self.assertEqual(total, 70.0)
    
    def test_total_income(self):
        self.tracker.add_income(2000.0, "Salary", "2024-01-01")
        self.tracker.add_income(500.0, "Freelance", "2024-01-10")
        total = self.tracker.total_income()
        self.assertEqual(total, 2500.0)
    def test_progress_toward_goal(self):
        self.tracker.set_savings_goal(1000.0)
        self.tracker.add_income(2000.0, "Salary", "2024-01-01")
        self.tracker.add_expense("Food", 500.0, "Groceries", "2024-01-15")
        current_savings, amount_needed = self.tracker.progress_toward_goal()
        self.assertEqual(current_savings, 1500.0)
        self.assertEqual(amount_needed, -500.0)  # Over the goal
if __name__ == '__main__':
    unittest.main()
                       [vars(expense) for expense in category.expenses]
                for name, category in self.categories.items()   
            }
        with open("budget_data.json", "w") as f:
            json.dump(data, f)
    def load_data(self: BudgetManager) -> None:
        try:
            with open("budget_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            self.income = data.get("income", 0.0)
            self.savings_goal = data.get("savings_goal", 0.0)
            categories_data = data.get("categories", {})
            for name, expenses in categories_data.items():
                category = BudgetCategory(name)
                for exp in expenses:
                    category.add_expense(exp["amount"], exp["description"], exp["date"])
                self.categories[name] = category
        except FileNotFoundError:
            pass
            data = json.load(f)
            self.income = data.get("income", 0.0)
            self.savings_goal = data.get("savings_goal", 0.0)
            categories_data = data.get("categories", {})
            for name, expenses in categories_data.items():
                category = BudgetCategory(name)
                for exp in expenses:
                    category.add_expense(exp["amount"], exp["description"], exp["date"])
                self.categories[name] = category
        except FileNotFoundError:
            pass
            data = json.load(f)
        except FileNotFoundError:
            pass