# List Comprehensions

# Basic syntax:
# new_list = [expression for item in iterable]

# Example: Creating a List of Squares
sqaure_nums = [x**2 for x in range(1, 11)]
print(sqaure_nums)

#  Adding a Condition (Filtering Data)
# new_list = [expression for item in iterable if condition]

# Example: Filtering Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [num for num in numbers if num % 2 == 0]
print(even)

# Example: Filtering Odd Numbers
odd = [num for num in numbers if num % 2 != 0]
print(odd)

# Using an if-else Condition
# new_list = [expression_if_true if condition else expression_if_false for item in iterable]

# Example: Labeling Even & Odd Numbers
labels = ["even" if num % 2 == 0 else "odd" for num in range(1, 11)]
print(labels)

# Working with Strings
# new_list = [expression for item in iterable]

# Example: Converting a List of Strings to Uppercase
fruits = ["apple", "banana", "cherry", "date", "grape"]
uppercase_words = [word.upper() for word in fruits]
print(uppercase_words)

# Nested Loops in List Comprehensions
# new_list = [expression for item1 in iterable1 for item2 in iterable2]

# Example: Creating a Multiplication Table
table = [(x, y, x*y) for x in range(1, 4) for y in range(1, 4)]
print(table)

# ✅ Practice Tasks:

# 1️.Create a list of cubes (x³) for numbers 1 to 10.
cube_nums = [y**3 for y in range(1, 11)]
print(cube_nums)

# 2️.Extract words from a sentence that are longer than 4 letters.
sentence = "Python is an amazing programming language"
words = sentence.split()

long_words = [word for word in words if len(word) > 4]
print(f"Words with more than 4 letters: {long_words}")

# 3️.Convert a list of temperatures from Celsius to Fahrenheit using the formula F = (C x 9/5) + 32
celsius_temp = [20, 30, 23, 45, 43, 18, 12]
fahrenheit_temps = [f"{(c * 9/5) + 32} °F" for c in celsius_temp]
print(f"Temperatures in Fahrenheit: {fahrenheit_temps}")

# 4.Generate a list of vowels from a given string.
text = str(input("Enter your text: "))
vowels = [char for char in text if char.lower() in "aeiou"]
print(f"Vowels in the text: {vowels}")

# 5️.Create a list of squares for even numbers between 1 and 20.
nums = range(1, 21)
squares_of_even = [num**2 for num in nums if num % 2 == 0]
print(f"Squares of even numbers: {squares_of_even}")
