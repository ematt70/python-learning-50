"""
Exercise 40 — Mini-Project: Expense Tracker

Task:
    Build a CLI expense tracker that:
        - Adds expenses (amount + category)
        - Saves them to expenses.csv
        - Shows total expenses
        - Shows totals by category
"""

import csv

def add_expense():
    amount = float(input("Amount: "))
    category = input("Category: ")
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([amount, category])
    print("Expense added.")

def total_expenses():
    total = 0
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            for amount, _ in reader:
                total += float(amount)
    except FileNotFoundError:
        print("No expenses yet.")
        return
    print("Total expenses:", total)

def expenses_by_category():
    totals = {}
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            for amount, category in reader:
                totals[category] = totals.get(category, 0) + float(amount)
    except FileNotFoundError:
        print("No expenses yet.")
        return

    for cat, total in totals.items():
        print(f"{cat}: {total}")

def main():
    while True:
        print("\n1) Add  2) Total  3) By Category  4) Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            total_expenses()
        elif choice == "3":
            expenses_by_category()
        elif choice == "4":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
