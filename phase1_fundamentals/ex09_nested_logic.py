"""
Exercise 09 — Nested Logic

Task:
    Ask the user for a grid size and print a grid of '*' characters.

Instructions:
    - Use nested loops OR string repetition.
    - Each row should contain size number of '*'.

Expected Output (size=3):
    * * *
    * * *
    * * *
"""

def printGrid(width, height):
    i = 1
    while i <= height:
        j = 1
        while j <= width:
            if j < width:
                print(" *", end="")
            else:
                print(" *")
            j += 1
        i += 1
        

def main():
    # Write your code below:
    gridWidth = int(input("Please enter width of grid: "))
    gridHeight = int(input("Please enter height of grid: "))

    printGrid(gridWidth, gridHeight)


if __name__ == "__main__":
    main()
