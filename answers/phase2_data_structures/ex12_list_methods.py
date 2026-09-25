"""
Exercise 12 — List Methods

Task:
    Practice common list methods:
        - append()
        - remove()
        - sort()
        - pop()
"""

def main():
    items = []

    items.append("apple")
    items.append("banana")
    items.append("cherry")
    print("After append:", items)

    items.remove("banana")
    print("After remove:", items)

    items.sort()
    print("After sort:", items)

    popped = items.pop()
    print("Popped:", popped)
    print("Final list:", items)

if __name__ == "__main__":
    main()
