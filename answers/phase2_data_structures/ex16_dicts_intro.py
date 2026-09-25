"""
Exercise 16 — Dictionaries Intro

Task:
    Create a dictionary representing a person with:
        - name
        - age
        - city
"""

def main():
    person = {
        "name": "Erich",
        "age": 42,
        "city": "Davenport",
    }

    print("Name:", person["name"])
    print("Age:", person["age"])
    print("City:", person["city"])

if __name__ == "__main__":
    main()
