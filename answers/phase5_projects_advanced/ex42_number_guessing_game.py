"""
Exercise 42 — Number Guessing Game

Task:
    Build a guessing game where:
        - The computer picks a random number 1–100
        - The user guesses until correct
        - The game gives "higher/lower" hints
"""

import random

def main():
    secret = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100...")
    tries = 0

    while True:
        guess = int(input("Guess: "))
        tries += 1

        if guess < secret:
            print("Higher!")
        elif guess > secret:
            print("Lower!")
        else:
            print(f"Correct! You guessed it in {tries} tries.")
            break

if __name__ == "__main__":
    main()
