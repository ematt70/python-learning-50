"""
Exercise 21 — Functions Basics

Task:
    Write a function called is_prime(n) that returns True if n is prime,
    otherwise False. Then:
        - Ask the user for a number
        - Call the function
        - Print whether the number is prime

Instructions:
    - A prime number is greater than 1 and divisible only by 1 and itself.
    - Use a loop to check divisibility.
    - Return True/False from the function.

Expected Output (example):
    Enter a number: 11
    11 is prime.
"""

def is_prime(userNumber: int):
    if(userNumber <= 1):
        return False
    for i in range(2, int(userNumber ** 0.5)):
        if(userNumber % i == 0):
            return False
    return True
    

def main():
    number = int(input("Please enter a number: "))

    if(is_prime(number) == True):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")

if __name__ == "__main__":
    main()
