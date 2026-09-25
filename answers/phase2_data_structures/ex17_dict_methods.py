"""
Exercise 17 — Dictionary Methods

Task:
    Practice:
        - keys()
        - values()
        - items()
        - get()
"""

def main():
    person = {
        "name": "Erich",
        "age": 42,
        "city": "Davenport",
    }

    print("Keys:", list(person.keys()))
    print("Values:", list(person.values()))
    print("Items:", list(person.items()))
    print("Get name:", person.get("name"))
    print("Get country:", person.get("country", "Unknown"))

if __name__ == "__main__":
    main()
