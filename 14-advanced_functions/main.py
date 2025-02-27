# Advanced Functions: lambda functions, map(), filter(), and reduce()
from functools import reduce

# Lambda functions
# lambda arguments: expression
add = lambda x, y: x + y
print(add(5, 5))

# map() Function
# map(function, iterable)
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)

# filter() Function
# filter(function, iterable)
nums = [10, 15, 20, 25, 30]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

# reduce() Function
# reduce(function, iterable)
nums = [1, 2, 3, 4, 5, 6]
product = reduce(lambda x, y: x * y, nums)
print("Product of nums:", product)

# Practice Tasks:
# 1.Write a lambda function that multiplies two numbers.
multiply = lambda x, y: x * y
print(multiply(5, 5))

# 2.Use map() to double the elements of a list [2, 4, 6, 8].
doubled = [x * 2 for x in [2, 4, 6, 8]]
print("Doubled list:", doubled)

# 3.Use filter() to extract odd numbers from a list [1, 2, 3, 4, 5, 6].
odd_numbers = [x for x in [1, 2, 3, 4, 5, 6] if x % 2 != 0]
print("Odd numbers:", odd_numbers)

# 4.Use reduce() to find the sum of numbers [10, 20, 30, 40, 50].
num_list = [10, 20, 30, 40, 50]
sum_of_nums = reduce(lambda x, y: x + y, num_list)
print("Sum of numbers:", sum_of_nums)