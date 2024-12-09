# Expense Tracker and Analyzer
# This program helps users track their daily expenses and analyze their spending.
# Users can input expense details such as amount, category, and date. Each expense
# entry is saved to a file. The program provides analysis by category and month,
# including total and average spending. This helps users understand and manage
# their spending habits.

import json
from datetime import datetime


# Function to add an expense entry
def add_expense():
    """
    Prompts the user to enter details for a new expense, including the amount,
    category, and date. The function then saves the expense data to a file.
    """
    # Get input for the expense details
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the category (e.g., food, entertainment, bills): ").strip()
        date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ").strip()
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')  # Default to today's date if none entered
        # Validate the date format
        datetime.strptime(date, '%Y-%m-%d')  # Raises ValueError if format is wrong
    except ValueError:
        print("Invalid input. Please ensure the amount is a number and date is in YYYY-MM-DD format.")
        return

    # Save the expense data in a dictionary format
    expense = {"amount": amount, "category": category, "date": date}

    # Append the expense data to the file in JSON format
    with open("expenses.json", "a") as file:
        file.write(json.dumps(expense) + "\n")

    print("Expense added successfully!\n")  # Confirmation message for user


# Function to analyze expenses by category and month
def analyze_expenses():
    """
    Reads all saved expense entries from the file, calculates and displays
    total and average spending by category and by month.
    """
    expenses = []

    # Read each line from the file, converting JSON strings back into Python dictionaries
    try:
        with open("expenses.json", "r") as file:
            for line in file:
                expenses.append(json.loads(line.strip()))
    except FileNotFoundError:
        print("No expense records found. Please add expenses first.")
        return

    # Calculate total spending by category
    category_totals = {}
    monthly_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        date = expense["date"]
        month = date[:7]  # Get the year-month part for monthly analysis

        # Update category totals
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

        # Update monthly totals
        if month in monthly_totals:
            monthly_totals[month] += amount
        else:
            monthly_totals[month] = amount

    # Display category analysis results
    print("\nExpense Analysis by Category:")
    for category, total in category_totals.items():
        print(f" - {category}: ${total:.2f}")

    # Display monthly analysis results
    print("\nExpense Analysis by Month:")
    for month, total in monthly_totals.items():
        print(f" - {month}: ${total:.2f}")


# Function to display average spending per day
def daily_average():
    """
    Calculates the average daily spending based on the total number of days
    recorded in the expenses file. Helps users see their spending patterns.
    """
    expenses = []
    with open("expenses.json", "r") as file:
        for line in file:
            expenses.append(json.loads(line.strip()))

    # Gather unique dates and calculate daily average
    dates = {expense["date"] for expense in expenses}
    total_spent = sum(expense["amount"] for expense in expenses)
    average = total_spent / len(dates) if dates else 0

    print(f"\nAverage Daily Spending: ${average:.2f}")


# Main program loop for the user interface
def main():
    """
    Displays the main menu for the program, allowing the user to choose between
    adding a new expense, analyzing expenses, viewing average daily spending, or exiting.
    """
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. Analyze Expenses")
        print("3. View Average Daily Spending")
        print("4. Exit")

        # Get user menu choice and handle it
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            analyze_expenses()
        elif choice == "3":
            daily_average()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Run the main function to start the program
if __name__ == "__main__":
    main()