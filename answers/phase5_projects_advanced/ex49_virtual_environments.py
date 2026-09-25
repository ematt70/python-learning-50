"""
Exercise 49 — Virtual Environments

Task:
    Demonstrate how to:
        - Create a virtual environment
        - Activate it
        - Install a package
        - Freeze dependencies
"""

def print_instructions():
    print("""
To create a virtual environment:

    python -m venv venv

Activate it:
    macOS/Linux: source venv/bin/activate
    Windows:     venv\\Scripts\\activate

Install a package:
    pip install requests

Freeze dependencies:
    pip freeze > requirements.txt
""")

def main():
    print_instructions()

if __name__ == "__main__":
    main()
