"""
Exercise 05 — String Formatting

Task:
    Build a simple 'mad libs' sentence using user input.
"""

def build_sentence(noun, verb, place):
    return f"Today, the {noun} decided to {verb} at {place}."

def main():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    sentence = build_sentence(noun, verb, place)
    print(sentence)

if __name__ == "__main__":
    main()
