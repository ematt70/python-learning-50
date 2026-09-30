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
    i = 1
    while (i <= 10):
        print(i)
        i += 1

    print("---")

    j = 10
    while (j > 0):
        print(j)
        j -= 1

if __name__ == "__main__":
    main()
