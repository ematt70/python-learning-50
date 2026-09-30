"""
Exercise 08 — For Loops & Ranges

Task:
    Print all even numbers from 1 to 100.

Instructions:
    - Use range().
    - Use modulo (%) to check even numbers.

Expected Output:
    2
    4
    6
    ...
    100
"""

def main():
    # Write your code below:
    for i in range(2, 101, 2):
        if i % 2 == 0:
            print(i)
        

if __name__ == "__main__":
    main()
