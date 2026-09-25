"""
Exercise 07 — While Loops

Task:
    - Count from 1 to 10 using a while loop.
    - Then count from 10 down to 1.
"""

def count_up(start, end):
    i = start
    while i <= end:
        print(i)
        i += 1

def count_down(start, end):
    i = start
    while i >= end:
        print(i)
        i -= 1

def main():
    count_up(1, 10)
    print("---")
    count_down(10, 1)

if __name__ == "__main__":
    main()
