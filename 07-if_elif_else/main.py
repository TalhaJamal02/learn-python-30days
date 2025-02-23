# if else statements

# Check if a number is positive, negative or zero
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positve")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Check Even or Odd
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Grade Calculator
score = int(input("Enter your score: "))

if score > 100:
    print("Invalid score")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Find the Largest of Three Numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)

# Check Leap Year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Try years like 2024, 2000!
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Challenge: Nested If Statements:
# Task: Check if a person is eligible to vote (must be 18+ and a citizen).
age = int(input("Enter your age: "))
citizen = str(input("Are you a citizen? (y/n): "))

if age >= 18:
    if citizen == "y":
        print("You are eligible to vote")
    else:
        print("You must be a citizen to vote")
else:
    print("You must be at least 18 years old to vote")

# Check if a triangle is valid (Sum of two sides must be greater than the third).
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and (a + b > c and a + c > b and b + c > a):
    print("Triangle is valid")
else:
    print("Triangle is not valid")