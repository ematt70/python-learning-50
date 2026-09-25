"""
Exercise 18 — Sets

Task:
    Create two sets and print:
        - Union
        - Intersection
        - Difference (A-B and B-A)
"""

def main():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print("Union:", a | b)
    print("Intersection:", a & b)
    print("Difference A-B:", a - b)
    print("Difference B-A:", b - a)

if __name__ == "__main__":
    main()
