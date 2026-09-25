"""
Exercise 48 — Unit Testing with unittest

Task:
    Write tests for a simple add(a, b) function.
"""

import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(add(0, 5), 5)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
