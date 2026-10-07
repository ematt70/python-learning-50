"""
Exercise 11 — Lists Intro

Task:
    Create a list of 5 numbers and print:
        - The first element
        - The middle element
        - The last element

Instructions:
    - Use indexing: list[0], list[-1]
    - Use len(list) // 2 to find the middle index
    - Print each value clearly.

Expected Output:
    First: 10
    Middle: 30
    Last: 50
"""

def main():
    # Write your code below:
    numberList = [17, 331, 199, 87, 34]

    print(f"First: {numberList[0]}")
    print(f"Middle: {numberList[len(numberList)//2]}")
    print(f"Last: {numberList[-1]}")

if __name__ == "__main__":
    main()
