"""
Exercise 31 — Reading Files

Task:
    Read a text file and print:
        - Number of lines
        - Number of words
        - Number of characters
"""

def analyze_file(filename):
    with open(filename, "r") as f:
        text = f.read()

    lines = text.splitlines()
    words = text.split()
    chars = len(text)

    return len(lines), len(words), chars

def main():
    filename = "sample.txt"
    lines, words, chars = analyze_file(filename)
    print("Lines:", lines)
    print("Words:", words)
    print("Characters:", chars)

if __name__ == "__main__":
    main()
