import cProfile
import pdb
from functools import lru_cache

# Debugging with pdb
def divide(a, b):
    pdb.set_trace()  # Debugger starts here
    return a / b

print(divide(10, 2))  # Works fine
print(divide(10, 0))  # Causes ZeroDivisionError

#  Profiling with cProfile (Finding Slow Code)
def slow_func():
    total = sum(i**2 for i in range(1000000))
    return total

cProfile.run('slow_func()')


# Practice Task: Debug a Python Script Using pdb

def factorial(n):
    """Returns the factorial of a given number n."""
    if n == 0 or n == 1:
        return 1

    pdb.set_trace()  # Debugger starts here

    return n * factorial(n - 1)

num = 6
result = factorial(num)
print(f"Factorial of {num} is: {result}")


# Task 1: Debugging a Complex Function
def find_primes(n):
    """Finds all prime numbers upto n"""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        pdb.set_trace()  # Debugger starts here

        if is_prime:
            primes.append(num)

    return primes

n = 20
print(f"Prime number uupto {n}: {find_primes(n)}")


# Task 2: Profile a Slow Function
@lru_cache(maxsize=None)
def fibonacci(n):
    """Returns nth Fibonacci number (but it's slow!)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


cProfile.run('print(fibonacci(30))')
