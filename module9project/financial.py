import json
import matplotlib.pyplot as plt
from datetime import datetime

# Budget Category Class
class BudgetCategory:

# TO DO: Define __int__, an add_expense() function and an total_expenses() function
    def __init__(self, name):   
        self.name = name
        self.expenses = []  # List to hold expense records

    def add_expense(self, amount, description, date):
        self.expenses.append({"amount": amount, "description": description, "date": date})

    def total_expenses(self):
        return sum(expense["amount"] for expense in self.expenses)



# Budget Manager Class
class BudgetManager:

    def __init__(self):
        self.income = 0.0
        self.savings_goal = 0.0
        self.categories = {}
        self.load_data()

  
# TO DO: Define functions: set_income(), set_savings_goal(), add_expense(), total_expenses(), progress_toward_goal(), save_data(), load_data(), and visualize_expenses().



# Input Validation Functions

# TO DO: Define get_valid_float(), get_valid_date() functions



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
        	# TO DO: Prompt for monthly income as input. Set income and display what income is set to.

        
        elif choice == '2':
        	# TO DO: Prompt for savings goal as input. Set savings goal and display savings goal is set to.
        
        elif choice == '3':
        	# TO DO: 
            #      Prompt for expense category as input. 
            #      Prompt for expense amount as input. 
            #      Prompt for a brief description of the expense. 
            #      Prompt for expense date in the format of (YYYY-MM-DD)
            #      Add expense.
            #      Display added expense.
        
        elif choice == '4':
	        # TO DO: Get total expenses. Display total expenses.
        
        elif choice == '5':
            # TO DO: Get progress towards goal. If on track, display �You are on track!� and also display the 
            #        current savings amount. If not on track, display �Current savings $xxx. You need $xxx to 
            #        reach your goal.�

        elif choice == '6':
	        # TO DO: call visualize_expenses() to show expense graph or pie chart

        
        elif choice == '7':
	        # TO DO: Save data and exit program. Display a message to indicate that data has been saved 
            #        successfully and exiting the program.

        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()