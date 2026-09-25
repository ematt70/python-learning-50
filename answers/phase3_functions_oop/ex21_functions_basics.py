"""
Exercise 21 — Functions Basics

Task:
    Write a function called is_prime(n) that returns True if n is prime,
    otherwise False. Then:
        - Ask the user for a number
        - Call the function
        - Print whether the number is prime
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")

if __name__ == "__main__":
    main()
