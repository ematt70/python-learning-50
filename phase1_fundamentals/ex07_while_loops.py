"""
Exercise 07 — While Loops

Task:
    - Count from 1 to 10 using a while loop.
    - Then count from 10 down to 1.

Instructions:
    - Initialize counters.
    - Update counters inside the loop.

Expected Output:
    1
    2
    ...
    10
    ---
    10
    9
    ...
    1
"""

def main():
    # Write your code below:
    for i in range(1, 11):
        print(i)

    print("---")

    for j in reversed(range(1, 11)):
        print(j)

if __name__ == "__main__":
    main()
