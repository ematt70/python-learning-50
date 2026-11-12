"""
Exercise 22 — Parameters & Default Arguments

Task:
    Write a function greet(name, greeting="Hello") that prints a greeting.
    Demonstrate calling it with:
        - Only a name
        - A name and a custom greeting

Instructions:
    - Use a default parameter for greeting.
    - Print the final message inside the function.

Expected Output:
    Hello, Erich!
    Welcome, Erich!
"""

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

def main():
    # Write your code below:
    
    yourName = str(input("Please enter a name: "))
    yourGreeting = str(input("Please enter a greeting, or <ENTER> for default greeting: "))
    
    if(yourGreeting.strip()):
        greet(yourName, yourGreeting)
    else:
        greet(yourName)


if __name__ == "__main__":
    main()
