import csv
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (Food, Transport, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!")

def view_expenses():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if len(expenses) <= 1:
        print("No expenses found.")
        return

    for row in expenses:
        print(f"{row[0]:<12} | {row[1]:<10} | ₹{row[2]:<8} | {row[3]}")

def total_expenses():
    total = 0
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[2])
    print(f"💰 Total Expenses: ₹{total}")

def menu():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    init_file()
    menu()
