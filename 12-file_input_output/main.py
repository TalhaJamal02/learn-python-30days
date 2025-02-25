# File Input/Output
from datetime import datetime

# Writing to a File
file = open("example.txt", "w")
file.write("Hello, This is Day 12 of Python learning")
file.close()  # Always close the file after writing

# Reading from a File
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Appending to a File
file = open("example.txt", "a")
file.write("\nThis is a new line added to the file")
file.close()

# Using with open() (Best Practice)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # No need to manually close the file!

# Writing & Reading a List of Data
lines = ["Python is fun!\n", "Python is easy!\n",
         "File handling is easy!\n", "Let's practice!\n"]

# Writing multiple lines
with open("multiple_lines_data.txt", "w") as file:
    file.writelines(lines)

# Reading the file
with open("multiple_lines_data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character

# Practice Tasks:

# 1.Create a program that writes user input to a file and then reads it back.
user_input = str(input("Enter you text: "))
with open("user_input.txt", "w") as file:
    file.write(user_input)
    print("Data written to file!")

with open("user_input.txt", "r") as file:
    content = file.read()
    print("Your text: ", content.strip())

# 2.Write a script that logs the current date & time in a file whenever it is run.

with open("log.txt", "w") as file:
    now = datetime.now()
    file.write(f"Log entry: {now.strftime('%d/%m/%Y, %H:%M:%S')}\n")

with open("log.txt", "r") as file:
    content = file.read()
    print(content)

# 3.Read a file and count the number of words in it.

with open("example.txt", "r") as file:
    content = file.read()
    words = content.split()
    print(f"'example.txt' has {len(words)} number of words")