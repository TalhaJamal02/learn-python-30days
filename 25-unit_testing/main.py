# What is Unit Testing?
# Unit testing is the process of testing individual parts (units) of a program to ensure they work correctly. A unit can be a function, a class method, or a module.

# Think of it like this:

# You are building an e-commerce website. Before launching, you want to ensure the "Add to Cart" button works as expected. Instead of testing the entire website manually every time, you write unit tests to verify that clicking the button correctly adds an item to the cart.

# Why is Unit Testing Important?

# Catches bugs early
# Ensures code reliability
# Makes refactoring easier without breaking existing features
# Saves time in large projects

import pytest
import unittest


def add(a, b):
    return a + b


class TestMathOperators(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 4), 6)
        self.assertEqual(add(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()

# What is Pytest?
# Pytest is a popular Python testing framework that simplifies writing and running tests. It provides:
# Easy syntax (less boilerplate than unittest)
# Powerful assertions (better error reporting)
# Fixtures (for setting up test data)
# Parametrization (run tests with multiple inputs easily)

# Real-world Example:

# Imagine you work on a banking application, and you need to test if the withdrawal function correctly reduces the account balance. Instead of manually checking different inputs, Pytest lets you automate this:


def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient funds"
    return balance - amount


def test_withdraw():
    assert withdraw(100, 50) == 50
    assert withdraw(100, 150) == "Insufficient funds"


if __name__ == "__main__":
    pytest.main()

# Example: Unit Testing with unittest and pytest

# unittest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, 2), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 5), 0)


if __name__ == "__main__":
    unittest.main()


# pytest
def test_add():
    assert add(3, 5) == 8
    assert add(-2, 2) == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5