# Modules

# Using the math Module
import os
from datetime import datetime
import math
import random

num = 25
num2 = 3.7

sqrt_num = math.sqrt(num)
print(f"Square root of {num} is {sqrt_num}")

value_pi = math.pi
print(f"Value of pi is {value_pi:.3f}")

factorial = math.factorial(6)
print(f"Factorial of 6 is {factorial}")

# Returns the ceiling of x as a float, the smallest integer value greater than or equal to x.
print(math.ceil(num2))
# Returns the floor of x as a float, the largest integer value less than or equal to x.
print(math.floor(num2))
# Truncates the Real x to the nearest Integral toward 0.
print(math.trunc(num2))
print(int(math.pow(2, 3)))  # Return x raised to the power y.

# Using the datetime Module
now = datetime.now()
print("Current Date and Time:", now.strftime("%d/%m/%Y, %H:%M:%S"))
print("Current Year:", now.year)

future_date = datetime(2026, 1, 1)
days_left = (future_date - now).days
print(f"Days left until new year: {days_left} days.")

# Using the random Module
print("Random Integer:", random.randint(1, 20))

choice = random.choice(["Python", "JavaScript", "TypeScript", "Java"])
print("Random Choice:", choice)

# Using the os Module
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)

files_in_dir = os.listdir()
print("Files In Directory:", files_in_dir)

if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
os.chdir("test_folder")  # change the current working directory
print("Current Working Directory:", os.getcwd())