"""
Exercise 11 — Lists Intro

Task:
    Create a list of 5 numbers and print:
        - The first element
        - The middle element
        - The last element
"""

def main():
    numbers = [10, 20, 30, 40, 50]
    print("First:", numbers[0])
    print("Middle:", numbers[len(numbers) // 2])
    print("Last:", numbers[-1])

if __name__ == "__main__":
    main()
