# ============================================================
# Day 7 – Object-Oriented Programming (OOP) in Python
# ============================================================

# ------------------------------------------------------------
# 🔹 1. WHAT IS OOP?
# ------------------------------------------------------------
# OOP (Object-Oriented Programming) organizes code into reusable units (classes).
# A CLASS is a blueprint | An OBJECT is an instance of that blueprint.
# Key principles: Encapsulation, Inheritance, Polymorphism, Abstraction

# ------------------------------------------------------------
# 🧱 2. CLASSES AND OBJECTS (Basic Structure)
# ------------------------------------------------------------

class Student:
    """Represents a student with basic info."""
    
    def __init__(self, name, major, age):
        # instance attributes
        self.name = name
        self.major = major
        self._age = age  # convention: _ means "protected" (not private, but not for direct use)

    def introduce(self):
        print(f"Hi, I’m {self.name}, studying {self.major}, aged {self._age}.")

    # Encapsulation – controlling access to attributes
    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print("❌ Age must be positive.")

# Example:
s = Student("Tushar", "CSDA", 22)
s.introduce()
s.set_age(23)
print("Updated Age:", s.get_age())

# ------------------------------------------------------------
# 🧬 3. INHERITANCE – Reuse & Extend Functionality
# ------------------------------------------------------------
# Child classes can inherit properties & methods from parent classes.

class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, I’m {self.name}.")

class StudentChild(Person):  # inherits from Person
    def __init__(self, name, major):
        super().__init__(name)  # calls parent's constructor
        self.major = major
    def introduce(self):
        print(f"{self.name}, majoring in {self.major}.")

child = StudentChild("Alice", "Math")
child.greet()        # From parent
child.introduce()    # From child

# 🔹 Tip: super() is used to call the parent’s version of a method.


# ------------------------------------------------------------
# 🌀 4. POLYMORPHISM – Same Function, Different Behavior
# ------------------------------------------------------------
# Allows multiple classes to define methods with the same name but different implementations.

class Animal:
    def make_sound(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def make_sound(self):
        print("🐶 Woof!")

class Cat(Animal):
    def make_sound(self):
        print("🐱 Meow!")

animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.make_sound()  # Each class uses its own version

# 🔹 Tip: Polymorphism = “Many forms” (Same interface, different behavior)


# ------------------------------------------------------------
# 🔒 5. ENCAPSULATION – Data Hiding & Controlled Access
# ------------------------------------------------------------
# Using methods (getters/setters) to safely interact with data.
# Private vars use "__" prefix; protected vars use "_".

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance = ₹{self.__balance}.")
        else:
            print("Invalid deposit amount!")

    def get_balance(self):
        return self.__balance

acc = Account("Tushar", 1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

# 🔹 Tip: __balance is name-mangled (hidden) and can’t be accessed directly like acc.__balance.


# ------------------------------------------------------------
# 🎭 6. ABSTRACTION – Hiding Internal Details
# ------------------------------------------------------------
# Achieved using abstract classes & methods from the abc module.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class"""
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):  # must be implemented in child
        pass

    def describe(self):
        print(f"This is a {self.color} shape.")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height

c = Circle("red", 5)
r = Rectangle("blue", 4, 6)

c.describe(); print("Area:", round(c.area(), 2))
r.describe(); print("Area:", r.area())

# 🔹 Tip: You can’t create an object from an abstract class directly.


# ------------------------------------------------------------
# 🧠 7. INTERVIEW QUICK RECAP
# ------------------------------------------------------------
# ✅ CLASS – Blueprint for creating objects.
# ✅ OBJECT – Instance of a class.
# ✅ ENCAPSULATION – Hide data, use getters/setters.
# ✅ INHERITANCE – Reuse code across related classes.
# ✅ POLYMORPHISM – Same interface, different implementation.
# ✅ ABSTRACTION – Show essential, hide complex.


# ------------------------------------------------------------
# 🎯 FINAL TAKEAWAY
# ------------------------------------------------------------
# 🧩 OOP makes code:
# → Reusable (through inheritance)
# → Secure (through encapsulation)
# → Flexible (through polymorphism)
# → Maintainable (through abstraction)
