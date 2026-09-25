"""
Exercise 44 — API Calls

Task:
    Call a public JSON API and print selected fields.
"""

import requests

def fetch_todo(todo_id=1):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    try:
        data = fetch_todo(1)
        print("Title:", data["title"])
        print("Completed:", data["completed"])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
