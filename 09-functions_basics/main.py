# Functions:
def square(num):
    return num ** 2

print(square(4))

def greet(name):
    return f"Hello, {name} have a nice day"

print(greet("Talha"))

def add(a, b):
    return a + b

print(add(10, 15))

# Function with default parameter values:
def rectangle_area(length=5, width=3):
    return length * width

print(rectangle_area())

def square_and_cube(num):
    return num ** 2, num ** 3


square, cube = square_and_cube(4)
print(f"Square: {square}, Cube: {cube}")

# Global vs. Local Scope:
x = 10


def change_x():
    x = 5  # Local variable
    print("Inside function:", x)

change_x()
print("Outside function:", x)


# Tip Calculator:
def calculate_tip(total_bill, tip_percentage):
    """Calculate the tip amount based on the total bill and tip percentage."""
    tip = total_bill * tip_percentage/100
    return tip

bill_amount = float(input("Enter the total bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))

tip = calculate_tip(bill_amount, tip_percent)
print(f"Tip: ${tip:.2f}")

# Temperature Converter:
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


# Example usage:
temp = 28

temp_fahrenheit = celsius_to_fahrenheit(temp)
print(f"{temp}°C is {temp_fahrenheit}°F")

temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit}°F is {temp_celsius:.1f}°C")

# Lambda Functions:
def square_lambda(num): return num ** 2

print(square_lambda(4))

def add_lambda(a, b): return a + b

print(add_lambda(10, 15))

# Recursive Function:
def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:  # Base Case
        return 1
    else:
        return n * factorial(n-1)  # Recursive Case

print(factorial(5))