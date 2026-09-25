"""
Exercise 32 — Writing Files

Task:
    Ask the user for a message and write it to a file.
"""

def write_message(filename, msg):
    with open(filename, "w") as f:
        f.write(msg + "\n")

def main():
    msg = input("Enter a message to save: ")
    write_message("output.txt", msg)
    print("Message written to output.txt")

if __name__ == "__main__":
    main()
