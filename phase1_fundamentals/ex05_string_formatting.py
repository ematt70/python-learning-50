"""
Exercise 05 — String Formatting

Task:
    Build a simple 'mad libs' sentence using user input.

Instructions:
    - Ask for a noun, verb, and place.
    - Use an f-string to build the final sentence.

Expected Output:
    Today, the cat decided to sleep at the couch.
"""

def main():
    # Write your code below:
    noun = str(input("Please provide a noun: "))
    verb = str(input("Please provide a verb: "))
    place = str(input("Please provide a place: "))

    print(f"Today, the {noun} decided to {verb} at the {place}.")

if __name__ == "__main__":
    main()
