"""
Exercise 50 — Capstone Project: Personal Dashboard

Task:
    Build a CLI dashboard that shows:
        - Weather (API call)
        - To-do list (JSON file)
        - Recent expenses (CSV file)
"""

import json
import csv
import requests
from pathlib import Path

TODO_FILE = Path("todo.json")
EXPENSE_FILE = Path("expenses.csv")

def get_weather():
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=41.52&longitude=-90.57&current_weather=true"
        data = requests.get(url).json()
        w = data["current_weather"]
        return f"{w['temperature']}°C, wind {w['windspeed']} km/h"
    except Exception:
        return "Weather unavailable"

def get_tasks_summary():
    if TODO_FILE.exists():
        with open(TODO_FILE, "r") as f:
            tasks = json.load(f)
        pending = sum(1 for t in tasks if not t["done"])
        return f"{pending} pending"
    return "No tasks"

def get_expenses_total():
    total = 0
    if EXPENSE_FILE.exists():
        with open(EXPENSE_FILE, "r") as f:
            reader = csv.reader(f)
            for amount, _ in reader:
                total += float(amount)
        return f"${total:.2f}"
    return "$0.00"

def main():
    print("\n--- DASHBOARD ---")
    print("Weather:", get_weather())
    print("Tasks:", get_tasks_summary())
    print("Expenses:", get_expenses_total())

if __name__ == "__main__":
    main()
