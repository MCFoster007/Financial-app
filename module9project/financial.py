import json
import matplotlib.pyplot as plt
from datetime import datetime


#add class expense
class Expense:

    def __init__(self: Expense, amount: float, description: str, date: str):
        self.amount = amount
        self.description = description
        self.date = date

    def __str__(self: Expense) -> str:
        return f"${self.amount: .2f} for '{self.description}' on {self.date}"


# Budget Category Class
class BudgetCategory:

    # TO DO: Define __int__, an add_expense() function and an total_expenses() function
    def __init__(self: BudgetCategory, name: str):
        self.name = name
        self.expenses = []  #list to hold expense dictionaries

    def add_expense(self: BudgetCategory, amount: float, description: str, date: str) -> Expense:
        expense = Expense(amount, description, date)
        self.expenses.append(expense)
        return expense

    def total_expenses(self: BudgetCategory) -> float:
        return sum(expense.amount for expense in self.total_expenses)


# Budget Manager Class


class BudgetManager:

    def __init__(self: BudgetManager):
        self.income = 0.0
        self.savings_goal = 0.0
        self.categories = {}
        self.load_data()


# TO DO: Define functions: set_income(), set_savings_goal(), add_expense(),
# total_expenses(), progress_toward_goal(), save_data(), load_data(),&
#visualize_expenses().


    def set_income(self: BudgetManager, amount: float) -> None:
        self.income = amount


    def set_savings_goal(self: BudgetManager, amount: float) -> None:
        self.savings_goal = amount


    def add_expense(self: BudgetManager, category_name: str, amount: float, description: str,
                    date: str) -> Expense:
        if category_name not in self.categories:
            self.categories[category_name] = BudgetCategory(category_name)
        return self.categories[category_name].add_expense(amount, description,date)


    def total_expenses(self: BudgetManager) -> float:
        return sum(category.total_expenses()
                   for category in self.categories.values())


    def progress_toward_goal(self: BudgetManager) -> tuple[float, float]:
        total_spent = self.total_expenses()
        current_savings = self.income - total_spent
        amount_needed = self.savings_goal - current_savings
        return current_savings, amount_needed


    def save_data(self: BudgetManager) -> None:
        data = {
            "income": self.income,
            "savings_goal": self.savings_goal,
            "categories": {
                name: [
                    {"amount": e.amount,
                    "description": e.description,
                    "date": e.date} 
                    for e in category.expenses
                ]
                for name, category in self.categories.items()
            }
        }
        with open("budget_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)


# Input Validation Functions
    def load_data(self: BudgetManager) -> None:
        try:
            with open("budget_data.json", "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    print("Warning: Could not load data, File is corrupted or invalid.")
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")
            return
        #if no errors prceed to load values

        self.income = data.get("income", 0.0)
        self.savings_goal = data.get("savings_goal", 0.0)
        for name, expenses in data.get("categories", {}).items():
            category = BudgetCategory(name)
            for expense in expenses:
                category.add_expense(expense["amount"], expense["description"],
                                     expense["date"])
            self.categories[name] = category


# TO DO: Define get_valid_float(), get_valid_date() functions


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
            print(
                "Invalid date format. Please enter date in YYYY-MM_DD format.")

    def visualize_expenses(self: BudgetManager):
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
        plt.ticks(rotation=45)
        plt.tight_layout()
        plt.show()


# Main Program
def main():
    manager = BudgetManager()
    print("Welcome to Personal Budgeting Application!")
    while True:
        print("\nMenu:")
        print("1. Set Income")
        print("2. Set Savings Goal")
        print("3.Add Expense")
        print("4. View Total Expenses")
        print("5. View Savings Progress")
        print("6. Visualize Expenses")
        print("7. Save & Exit")

        choice = input("Choose an option (1-7): ")

    if choice == '1':
        # TO DO: Prompt for monthly income as input. Set income&display what income is set to.
        amount = get_valid_float('Enter your monthly income: ')
        manager.set_income(amount)
        print(f"Income is set to: ${manager.income:.2f}")

    elif choice == '2':
        # TO DO: Prompt for savings goal as input. Set savings goal and display savings goal is set to.
        amount = get_valid_float('Enter your savings goal:')
        manager.set_savings_goal(amount)
        print(f"Savings goal is set to: ${manager.savings_goal: .2f}")

    elif choice == '3':
        # TO DO:
        #      Prompt for expense category as input.
        #      Prompt for expense amount as input.
        #      Prompt for a brief description of the expense.
        #      Prompt for expense date in the format of (YYYY-MM-DD)
        #      Add expense.
        #      Display added expense.
        category = input("Enter expense category: ")
        amount = get_valid_float("Enter expense amount: ")
        description = input("Enter a brief description of the expense: ")
        date = get_valid_date("Enter expense date (YYYY-MM-DD): ")
        manager.add_expense(category, amount, description, date)
        print(
            f"Added expense: ${amount:.2f} for '{description}'on {date} in category'{category}'"
        )

# TO DO: Get total expenses. Display total expenses.
    elif choice == '4':
        print(f"Total expenses: ${manager.total_expenses():.2f}")

        # TO DO: Get progress towards goal. If on track, display
        #�You are on track!� and also display the
        # current savings amount. If not on track, display
        #�Current savings $xxx. You need $xxx to
        #reach your goal.�

    elif choice == '5':
        current_savings, amount_needed = manager.progress_toward_goal()
        if amount_needed <= 0:
            print(
                f"You are on track! Current savings: ${current_savings: .2f}")
        else:
            print(
                f"Current savings: ${current_savings: .2f}. You need ${amount_needed: .2f} to reach your goal."
            )

# TO DO: call visualize_expenses() to show expense graph or pie chart

    elif choice == '6':
        manager.visualize_expenses()

    elif choice == '7':
        # TO DO: Save data and exit program. Display a message to indicate that data has been saved
        #        successfully and exiting the program.
        manager.save_data()
        print("Data saved successfully. Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
 
if __name__ == "__main__":
    main()
