"""
Exercise 18 — Sets

Task:
    Create two sets and print:
        - Union
        - Intersection
        - Difference (A-B and B-A)

Instructions:
    - Use | for union.
    - Use & for intersection.
    - Use - for difference.

Expected Output:
    Union: {1, 2, 3, 4, 5, 6}
    Intersection: {3, 4}
    Difference A-B: {1, 2}
    Difference B-A: {5, 6}
"""

def main():
    # Write your code below:
    setOne = {1, 2, 3, 4}
    setTwo = {3, 4, 5, 6}
    union = setOne | setTwo
    intersection = setOne & setTwo
    differenceAB = setOne - setTwo
    differenceBA = setTwo - setOne

    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
    print(f"Difference A-B: {differenceAB}")
    print(f"Difference B-A: {differenceBA}")

if __name__ == "__main__":
    main()
