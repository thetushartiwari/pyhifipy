# DAY 3 – FUNCTIONS, SCOPE & MODULES

# Functions → Reusable blocks of logic
# Scope → Which variables can be accessed where
# Modules → Reuse of prebuilt or user-defined code
# ==================================================


# --------------------------------------------------
# 🔹 FUNCTIONS – BASICS
# --------------------------------------------------
# Functions let you write logic once and reuse it anywhere.

def add(a, b):
    """Simple function: returns sum of two numbers"""
    return a + b

print(add(5, 10))  # Output: 15


# ✅ PRACTICAL VERSION: taking user input
def add_input():
    """Takes input from user, returns sum"""
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a + b

# Example usage (dynamic): uncomment to run
# If you input 3 and 4, output will be:
# print("Sum:", add_input())   # Output (example): Sum: 7


# --------------------------------------------------
# 🔸 FUNCTION PARAMETERS – TYPES & USE
# --------------------------------------------------

# 1️⃣ Positional Arguments → Order matters
def multiply(a, b):
    """Multiplying two numbers (order matters)"""
    return a * b

print(multiply(3, 4))  # Output: 12


# 2️⃣ Keyword Arguments → Order doesn’t matter
def create_user(name, age, city):
    """Readable code using keyword args"""
    print(f"User: {name}, {age} yrs, from {city}")

create_user(age=22, name="Tushar", city="Delhi")
# Output: User: Tushar, 22 yrs, from Delhi


# 3️⃣ Default Arguments → Optional parameters
def greet(name="User"):
    """Greets user; uses default if not provided"""
    print(f"Hello, {name}!")

greet()          # Output: Hello, User!
greet("Tushar")  # Output: Hello, Tushar


# 4️⃣ *args → Variable number of positional arguments
def total(*numbers):
    """Accepts many inputs, returns their sum"""
    print("Numbers:", numbers)
    return sum(numbers)

print("Total:", total(10, 20, 30, 40))  # Output:
# Numbers: (10, 20, 30, 40)
# Total: 100


# 5️⃣ **kwargs → Variable number of keyword arguments
def display_info(**details):
    """Accepts flexible named data"""
    for key, val in details.items():
        print(f"{key}: {val}")

display_info(name="Tushar", age=22, course="CSDA")
# Output:
# name: Tushar
# age: 22
# course: CSDA


# ✅ PRACTICAL EXAMPLE combining all types
def calculate_bill(customer_name, *items, discount=0, **details):
    """
    Calculates total bill for a customer
    *items → list of prices
    discount → optional percentage
    **details → optional info like city, membership, etc.
    """
    total_amount = sum(items)
    final_amount = total_amount - (total_amount * discount / 100)
    
    print(f"\nCustomer: {customer_name}")
    print(f"Items total: ₹{total_amount}")
    print(f"After discount: ₹{final_amount}")
    for k, v in details.items():
        print(f"{k}: {v}")

calculate_bill("Tushar", 120, 250, 330, discount=10, city="Delhi", member="Gold")
# Output:
# Customer: Tushar
# Items total: ₹700
# After discount: ₹630.0
# city: Delhi
# member: Gold


# --------------------------------------------------
# 🔹 RETURN STATEMENT – When to Use
# --------------------------------------------------
# return → sends a result back; print → only displays output.

def square(num):
    return num ** 2  # reusable result

result = square(6)
print("Square:", result)  # Output: Square: 36

# ❌ Without return, result can't be reused
def square_print(num):
    print(num ** 2)  # only prints

# Output vs behavior:
square_print(5)         # Output: 25
print(square_print(5))  # Output: 25 then None


# --------------------------------------------------
# 🔹 RECURSION – Function Calling Itself
# --------------------------------------------------
# Used for repeating tasks that can be broken into smaller ones
# Always include a BASE CONDITION to stop recursion

def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))  # Output: Factorial of 5: 120

# Visual trace (conceptual):
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# ...
# factorial(1) = 1 (base), so recursion unwinds


# ✅ Tip:
# Recursion is great for factorial, Fibonacci, and tree/graph traversals.


# --------------------------------------------------
# 🔹 VARIABLE SCOPE – Local vs Global
# --------------------------------------------------
# Scope = where a variable is accessible from.

# Global scope → accessible everywhere
greeting = "Hi"

def say_hello():
    print(greeting + " from inside function")  # Output depends on global 'greeting'

say_hello()  # Output: Hi from inside function
print(greeting + " from outside function")  # Output: Hi from outside function

# Local scope → exists only inside a function
def local_example():
    msg = "Hello World"
    print(msg)  # Output: Hello World

local_example()  # Output: Hello World
# print(msg)  # ❌ Error if uncommented: msg not defined outside

# Modifying global variables
x = 5
def modify_global():
    global x
    x = 10

modify_global()
print("Updated x:", x)  # Output: Updated x: 10

# ✅ Tips:
# - Prefer local variables for safety.
# - Use 'global' only when truly needed.


# --------------------------------------------------
# 🔹 MODULES – Reusing External Code
# --------------------------------------------------
# A module = Python file or library containing prewritten functions.

import math as m

print("\nSquare root of 16:", m.sqrt(16))  # Output: Square root of 16: 4.0
print("Pi value:", m.pi)                   # Output: Pi value: 3.141592653589793
print("Factorial of 6:", m.factorial(6))   # Output: Factorial of 6: 720

# Importing specific functions:
from math import sqrt, pi
print("\nUsing direct import:", sqrt(25), pi)
# Output: Using direct import: 5.0 3.141592653589793

# ✅ Significance:
# - Use modules to avoid rewriting common utilities.


# --------------------------------------------------
# 🧠 QUICK SUMMARY
# --------------------------------------------------
# | Type/Concept  | When to Use | Example / Note |
# |----------------|-------------|----------------|
# | Positional     | Fixed order inputs | add(a, b) |
# | Keyword        | Clear, flexible order | create_user(age=22, name="Tushar") |
# | Default        | Optional inputs | greet(name="User") |
# | *args          | Unknown # of values | total(1,2,3) |
# | **kwargs       | Unknown named inputs | display_info(name="A", age=20) |
# | return         | Reuse value later | return result |
# | recursion      | Repeating pattern | factorial, Fibonacci |
# | global scope   | Use rarely | define outside function |
# | local scope    | Preferred | define inside function |
# | module import  | Reuse existing logic | import math, random |

# --------------------------------------------------
# 💡 PRACTICAL TIPS
# --------------------------------------------------
# ✅ Use functions to modularize your logic (like small building blocks)
# ✅ Use return when result needs to be reused in another part of program
# ✅ Use *args and **kwargs for flexible, reusable code
# ✅ Keep global usage minimal for cleaner debugging
# ✅ Import modules for prebuilt utilities instead of rewriting logic
# ✅ Always think: “Can I reuse this logic?” → If yes → make it a function
