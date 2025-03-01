# 1. What is Inheritance?
# Inheritance helps you reuse code by creating a child class from a parent class.

# Parent Class: The base class whose methods and properties are inherited.

# Child Class: The class that inherits from the parent.

# Parent Class
import math


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")

# Child Class


class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Creating Objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")

animal.sound()
dog.sound()

# 2. Method Overriding
# If the child class defines the same method as the parent class, then the child’s method overrides the parent’s method.

# Parent Class


class Vehicle:
    def start(self):
        print("Vehicle is starting...")


class Car(Vehicle):
    def start(self):
        print("Car is starting...")


# Creating Objects
vehicle = Vehicle()
car = Car()

vehicle.start()
car.start()


# Practice Tasks:
# Create a Shape class with a method area().
# Create Rectangle and Circle classes that inherit from Shape.
# Override the area() method to calculate the area of each shape.

# Parent Class
class Shape:
    def area(self):
        print("Area method not implemented")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


rect = Rectangle(10, 20)
circle = Circle(5)

rectangle_area = rect.area()
circle_area = circle.area()

print("Rectangle Area: ", rectangle_area)
print("Circle Area: ", round(circle_area, 2))