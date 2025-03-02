# 1. What is Exception Handling?
# An exception is an error that occurs during execution. Python provides the try, except, and finally blocks to handle errors gracefully.

# try and except
# The try block tests code for errors, while the except block handles the error.

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")

# Multiple Except Blocks:
# You can handle different types of exceptions separately.

try:
    num = int("Hello!")
except ValueError:
    print("ValueError occurred")
except TypeError:
    print("TypeError occurred")

# else Block:
# The else block executes if no exception occurs.

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input!")
else:
    print("Input was processed successfully!")

# finally Block
# The finally block always executes whether the exception is raised or not.

try:
    file = open("sample..txt", "r")
    print(file.read())
    print("File opened successfully!")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing the file...")

# Raise Custom Exceptions
# You can manually raise exceptions using the raise keyword.

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Access granted!")

try:
    check_age(16)
except ValueError as e:
    print(e)


# Practice Tasks:

# 1.Create a function that divides two numbers and handles:
# ZeroDivisionError
# ValueError

def divide(x, y):
    try:
        result = x / y
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Please enter a valid number!")

divide(12, 0)

# 2.Write a program that asks the user to enter a filename and reads the file, handling FileNotFoundError.

try:
    filename = input("Enter a filename: ")
    file = open(filename, "r")
    content = file.read()
    print("\nFile Content:")
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program execution completed!")