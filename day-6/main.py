# 1. Arithmetic Operators
length = 10
width = 5
area = length * width
print("Area of rectangle:", area)

remainder = 25 % 4
print("Remainder:", remainder)

power = 5 ** 3
print("5^3:", power)

# 2. Comparison Operators
a = 10
b = 3
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)

x = 15 > 10
print(x)

y = 25 / 5 == 5
print(y)

z = 7 * 3 != 21
print(z)

# 3. Logical Operators
num = 24

# Check if num is between 10 and 50
is_between = 10 < num < 50 
print(is_between)

# Check if num is even or > 100
is_even = num % 2 == 0 or num > 100
print(is_even)

# Use 'not' to check if 20 is not greater than 50
is_greater = not 20 > 50
print(is_greater)

# 4. Membership Operators
fruits = ["apple","banana","mango"]

# Check if "banana" is in the list
is_in_list = "banana" in fruits
print(is_in_list)

# Check if "orange" is not in the list
is_not_in_list = "orange" not in fruits
print(is_not_in_list)

# 5. Identity Operators
x = 5
y = 5

# Check if x and y are the same object
is_same_object = x is y
print(is_same_object)

# Check if x and y are not the same object
is_not_same_object = x is not y
print(is_not_same_object)