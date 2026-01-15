import json
import matplotlib.pyplot as plt
from datetime import datetime
from storage import JSONStorage

# Expense Class
class Expense:
    def __init__(self, amount: float, description: str, date: str):
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")  # added validation for negative expense
        if not description:
            raise ValueError("Description cannot be empty.") # validate description
        self.amount = amount
        self.description = description
        self.date = date

    def __str__(self) -> str:
        return f"${self.amount:.2f} for '{self.description}' on {self.date}"


# Budget Category Class
class BudgetCategory:
    def __init__(self, name: str):
        self.name = name
        self.expenses = []

    def add_expense(self, amount: float, description: str, date: str) -> Expense:
        expense = Expense(amount, description, date)
        self.expenses.append(expense)
        return expense

    def total_expenses(self) -> float:
        return sum(e.amount for e in self.expenses)      
    #(expense.amount for expense in self.expenses was replaced for e.amount for e in self.expenses for brevity)
 #to delegates validation to Expense.

# Budget Manager Class
class BudgetManager:
    def __init__(self):
        self.income = 0.0
        self.savings_goal = 0.0
        self.categories = {}
        self.load_data()

    def set_income(self, amount: float) -> None:
        self.income = amount

    def set_savings_goal(self, amount: float) -> None:
        self.savings_goal = amount

    def add_expense(self, category_name: str, amount: float, description: str, date: str) -> Expense:
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.") # added validation for negative expense
        if category_name not in self.categories:
            self.categories[category_name] = BudgetCategory(category_name)
        return self.categories[category_name].add_expense(amount, description, date)

    def total_expenses(self) -> float:
        return sum(category.total_expenses() for category in self.categories.values())

    def progress_toward_goal(self) -> tuple[float, float]:
        total_spent = self.total_expenses()
        current_savings = self.income - total_spent
        amount_needed = self.savings_goal - current_savings
        return current_savings, amount_needed

    def save_data(self) -> None:
        JSONStorage.save(self)

    def load_data(self) -> None:
        JSONStorage.load(self)

    def visualize_expenses(self) -> None:
        if not self.categories:
            print("No expenses to visualize.")
            return

        categories = list(self.categories.keys())
        expenses = [self.categories[cat].total_expenses() for cat in categories]

        plt.figure(figsize=(10, 6))
        plt.bar(categories, expenses, color='skyblue')
        plt.xlabel('Categories')
        plt.ylabel('Total Expenses')
        plt.title('Expenses by Category')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# Input Validation Functions
def get_valid_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive number.")


def get_valid_date(prompt: str) -> str:
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")


# Main Program
def main():
    manager = BudgetManager()
    print("Welcome to Personal Budgeting Application!")

    while True:
        print("\nMenu:")
        print("1. Set Income")
        print("2. Set Savings Goal")
        print("3. Add Expense")
        print("4. View Total Expenses")
        print("5. View Savings Progress")
        print("6. Visualize Expenses")
        print("7. Save & Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            amount = get_valid_float('Enter your monthly income: ')
            manager.set_income(amount)
            print(f"Income is set to: ${manager.income:.2f}")

        elif choice == '2':
            amount = get_valid_float('Enter your savings goal: ')
            manager.set_savings_goal(amount)
            print(f"Savings goal is set to: ${manager.savings_goal:.2f}")

        elif choice == '3':
            category = input("Enter expense category: ")
            amount = get_valid_float("Enter expense amount: ")
            description = input("Enter a brief description of the expense: ")
            date = get_valid_date("Enter expense date (YYYY-MM-DD): ")
            manager.add_expense(category, amount, description, date)
            print(f"Added expense: ${amount:.2f} for '{description}' on {date} in category '{category}'")

        elif choice == '4':
            print(f"Total expenses: ${manager.total_expenses():.2f}")

        elif choice == '5':
            current_savings, amount_needed = manager.progress_toward_goal()
            if amount_needed <= 0:
                print(f"You are on track! Current savings: ${current_savings:.2f}")
            else:
                print(f"Current savings: ${current_savings:.2f}. You need ${amount_needed:.2f} to reach your goal.")

        elif choice == '6':
            manager.visualize_expenses()

        elif choice == '7':
            manager.save_data()
            print("Data saved successfully. Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
