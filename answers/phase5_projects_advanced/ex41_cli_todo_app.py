"""
Exercise 41 — CLI To‑Do App

Task:
    Build a command-line to-do app that:
        - Adds tasks
        - Lists tasks
        - Marks tasks as done
        - Saves tasks to todo.json
        - Loads tasks at startup
"""

import json
from pathlib import Path

FILE = Path("todo.json")

def load_tasks():
    if FILE.exists():
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Added.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else " "
        print(f"{i+1}. [{status}] {t['task']}")

def complete_task(tasks):
    list_tasks(tasks)
    idx = int(input("Complete which number? ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print("Completed.")
    else:
        print("Invalid index.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1) Add  2) List  3) Complete  4) Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
