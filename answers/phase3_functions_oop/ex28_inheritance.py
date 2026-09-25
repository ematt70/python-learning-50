"""
Exercise 28 — Inheritance

Task:
    Create a base class Animal with a speak() method.
    Create subclasses Dog and Cat that override speak().
"""

class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def main():
    Dog().speak()
    Cat().speak()

if __name__ == "__main__":
    main()
