# For Loops:

# Using Ranges in Loops
import psutil  # Requires installation of the psutil library
import time
for i in range(1, 11):
    print(i)

# Iterating Over Lists
fruits = ["apple", "banana", "mango"]
for fruits in fruits:
    print(f"I like {fruits} ")

# Calculating total revenue from daily sales
daily_sales = [120.50, 89.99, 45.00, 150.75, 210.00]
total_revenue = 0

for sale in daily_sales:
    total_revenue += sale
print("Total revenue for the day: $", total_revenue)

# While Loop Example
num = 1
while num <= 10:
    # print(num)
    num += 1

# Using break and continue:

# Using break
for num1 in range(1, 11):
    if num1 == 6:
        break
    # print(num1)

# Using continue
for num2 in range(1, 11):
    if num2 == 6:
        continue  # skip the number 6
    print(num2)

# User authentication
correct_username = "admin"
correct_password = "password123"

username = str(input("Enter your username: "))
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password. Please try again.")


# Monitoring system status
threshold = 80.0  # CPU usage percentage threshold

cpu_usage = psutil.cpu_percent(interval=1)
print(f"Current CPU usage: {cpu_usage}%")

if cpu_usage > threshold:
    print("Warning: High CPU usage detected!")
    
time.sleep(5)