"""
Exercise 10 — Mini-Project: Simple Calculator

Task:
    Build a command-line calculator that:
        - Asks the user to choose an operation (+, -, *, /)
        - Asks for two numbers
        - Prints the result
        - Repeats until the user quits

Instructions:
    - Use a while loop for the menu.
    - Use if/elif to handle operations.
    - Handle division by zero gracefully.

Expected Interaction:
    Choose operation: +
    Enter first number: 5
    Enter second number: 3
    Result: 8
"""

def getNumber(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number.")


def getOperation():
    validOperator = False
    while validOperator == False:
        operation = input("Please enter operator (+, -, *, /): ")
        if operation not in ("+", "-", "*", "/"):
            print("Invalid operator.")
        else:
            validOperator = True

    return operation


def calculate(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    else:
        if num2 == 0:
            result = "undefined"
        else:
            result = num1 / num2

    return result


def main():
    # Write your code below:
    
    go = True
    while go == True:

        operator = getOperation()
        firstNumber = getNumber("Please enter the first number: ")
        secondNumber = getNumber("Please enter the second number: ")

        result = calculate(firstNumber, secondNumber, operator)

        print(f"Result: {result}")

        validRepeat = False
        while validRepeat == False:
            repeat = (input("Would you like to perform another operation? (y/n): "))
            if repeat.lower() == "n":
                go = False
                validRepeat = True
                print("Thanks for using the calculator!")
            elif repeat.lower() == "y":
                validRepeat = True
                go = True
            else:
                print("Invalid response.")
                validRepeat = False


if __name__ == "__main__":
    main()
