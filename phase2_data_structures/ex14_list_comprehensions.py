"""
Exercise 14 — List Comprehensions

Task:
    Create:
        - A list of squares from 1 to 10
        - A list of even squares only

Instructions:
    - Use [expression for item in iterable].
    - Use an if condition inside the comprehension.

Expected Output:
    Squares: [1, 4, 9, ..., 100]
    Even squares: [4, 16, 36, 64, 100]
"""

def main():
    # Write your code below:
    squareList = []
    evenSquareList = []
    for number in range(1, 11):
        squareList.append(number ** 2)
        if ((number ** 2) % 2 == 0):
            evenSquareList.append(number ** 2)

    print(f"Squares: {squareList}")
    print(f"Even squares: {evenSquareList}")
    

if __name__ == "__main__":
    main()
