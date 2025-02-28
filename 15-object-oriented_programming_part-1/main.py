# Introduction to Object-Oriented Programming (OOP)

# Class: A blueprint for creating objects (like a template).
# Object: An instance of a class with its own unique data.

# 1.How to Define a Class
class Car:
    brand = "Ferrari"

    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")

# 2.Creating Objects
my_car = Car()
print(my_car.brand)

my_car.start()
my_car.stop()

# 3.__init__ Method (Constructor)
# The __init__ method automatically gets called when you create an object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an Object
person1 = Person("Talha", 18)
person1.display()

# Practice Tasks:

# 1.Create a Book class with attributes like title and author.
# 2.Define a method show_info() to print the book details.
# 3.Create an object and call the method.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Creating an Object
book1 = Book("Atomic Habits", "James Clear")
book1.show_info()

# 4.Write a class Student with name and marks attributes, and a method to display them.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Creating an Object
student1 = Student("Talha", 87)
student1.display()