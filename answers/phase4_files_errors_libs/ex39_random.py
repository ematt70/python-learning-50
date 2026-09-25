"""
Exercise 39 — random Module

Task:
    Build a password generator that:
        - Generates a random password of length 12
        - Uses letters, digits, and symbols
"""

import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def main():
    password = generate_password(12)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
