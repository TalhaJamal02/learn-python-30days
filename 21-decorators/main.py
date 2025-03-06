# What Are Decorators?
# A decorator is a function that wraps another function, allowing you to execute code before and after the wrapped function runs. This is particularly useful for adding functionality like logging, authentication, caching, or performance measurement.

# How Do Decorators Work?
# Consider a simple function that logs when a function is called. Instead of adding logging code inside every function, you can write a decorator to do this.

# Example: Creating a Logging Decorator
# Define the decorator function:
import time


def log_decorator(func):
    def wrapper(*args, **kwargs):
        # Code to execute before calling the function
        print(
            f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")

        # Call the original function
        result = func(*args, **kwargs)

        # Code to execute after calling the function
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a + b


add(5, 5)

# Practice Tasks:

# 1.Create a Decorator to Log Function Calls
# Write a decorator that logs the function name and the arguments passed whenever a function is called.


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is called with arguments {args}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper


@log_decorator
def greet(name):
    return f"Hello, {name}!, How are you?"


greet("Talha")

# 2.Timer Decorator
# Create a decorator that calculates how long a function takes to execute.


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.3f} seconds")
        return result
    return wrapper


@timer_decorator
def calculate_sum(n):
    return sum(range(n))


calculate_sum(100000)

# 3.Uppercase Decorator
# Create a decorator that converts the return value of a function into uppercase letters.


def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase_decorator
def say_hello():
    return "Hello, world!"


print(say_hello())

# Final Practice Task Guide: Advanced Decorator
# 4.Create a decorator that:
# Logs the function name
# Logs the arguments
# Calculates and logs the execution time


def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"\nFunction '{func.__name__}' is called")
        print(f"Arguments: {args}, {kwargs}")

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time:.3f} seconds")
        print(f"Result: {result}")

        return result
    return wrapper


@log_execution
def multiply(a, b):
    time.sleep(1)  # Simulate time delay
    return a * b


multiply(5, 5)