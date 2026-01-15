import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from financial import Expense, BudgetCategory, BudgetManager


class TestExpense(unittest.TestCase):
    def test_expense_creation(self):
        e = Expense(100.0, "Groceries", "2024-01-15")
        self.assertEqual(e.amount, 100.0)
        self.assertEqual(e.description, "Groceries")
        self.assertEqual(e.date, "2024-01-15")
        self.assertEqual(str(e), "$100.00 for 'Groceries' on 2024-01-15")
        
class TestBudgetCategory(unittest.TestCase):
    def test_add_expense(self):
        cat = BudgetCategory("Food")
        cat.add_expense(20, "Lunch", "2025-01-10")
        self.assertEqual(len(cat.expenses), 1)
        self.assertEqual(cat.total_expenses(), 20.0)

class TestableBudgetManager(BudgetManager):#as a helper class
    def load_data(self):
        # Override to avoid loading from file during tests
        pass

class TestBudgetManager(unittest.TestCase):
    def setUp(self):
        # Create a fresh manager for each test
        self.manager = TestableBudgetManager()  
        self.manager.categories = {}  # avoid loading saved data
        self.manager.income = 10000
        self.manager.savings_goal = 300

    def test_set_income(self):
        self.manager.set_income(2000)
        self.assertEqual(self.manager.income, 2000)

    def test_add_expense_creates_category(self): #proves the system automatically creates a category if it doesn't exist
        self.manager.add_expense("Food", 25.0, "Lunch", "2025-01-10")
        self.assertIn("Food", self.manager.categories)
        self.assertEqual(self.manager.categories["Food"].total_expenses(), 25.0)

    def test_total_expenses(self): #integration-style test to verify multiple categories, expenses and totals across the whole system. also validates that totals expense works correctly.
        self.manager.add_expense("Food", 50, "Lunch", "2025-01-10")
        self.manager.add_expense("Transport", 20, "Bus", "2025-01-11")
        self.assertEqual(self.manager.total_expenses(), 70)

    def test_progress_toward_goal(self): #integration-style test to check how multiple parts work together and validates savings goal logic correctly.income minus expenses and how far the user is from the savings goal.
        self.manager.add_expense("Food", 100, "Groceries", "2025-01-10")
        current_savings, amount_needed = self.manager.progress_toward_goal()
        self.assertEqual(current_savings, 9900)
        self.assertEqual(amount_needed, -9600)  # because goal is 9600
        
        #added edge case test proves your system rejects invalid financial data, secure code requirment
    def test_negative_expense_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_expense("Food", -50, "Refund?", "2025-01-10")


   
        
if __name__ == '__main__':
            unittest.main()


