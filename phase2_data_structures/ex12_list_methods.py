"""
Exercise 12 — List Methods

Task:
    Practice common list methods:
        - append()
        - remove()
        - sort()
        - pop()

Instructions:
    - Start with an empty list.
    - Append three items.
    - Remove one item.
    - Sort the list.
    - Pop the last item and print it.

Expected Output (example):
    After append: ['apple', 'banana', 'cherry']
    After remove: ['apple', 'cherry']
    After sort: ['apple', 'cherry']
    Popped: cherry
    Final list: ['apple']
"""

def main():
    # Write your code below:
    fruitList = []
    
    fruitList.append('apple')
    fruitList.append('banana')
    fruitList.append('cherry')
    print(f"After append: {fruitList}")
    
    fruitList.remove('banana')
    print(f"After remove: {fruitList}")

    fruitList.sort()
    print(f"After sort: {fruitList}")

    popped = fruitList.pop(-1)
    print(f"Popped: {popped}")

    print(f"Final list: {fruitList}")




if __name__ == "__main__":
    main()
