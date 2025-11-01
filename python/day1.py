# ==================================================
# DAY 1 – INTRODUCTION & DATA TYPES
# ==================================================
# Python basics: understanding variables, data types,
# and how to use them in real code.
# Everything in Python is an OBJECT.
# ==================================================


# --------------------------------------------------
# 🔹 VARIABLES & DATA TYPES
# --------------------------------------------------
# A variable stores data in memory.
# You don’t need to declare the type — Python figures it out automatically.
# Syntax: variable_name = value

integer_var = 10                              # int → Whole numbers
float_var = 3.14                              # float → Decimal numbers
string_var = "AI"                             # str → Text data
list_var = [1, 2, 3]                          # list → Ordered, changeable
tuple_var = (4, 5, 6)                         # tuple → Ordered, unchangeable
dict_var = {"name": "Alice", "role": "Engineer"}  # dict → Key-value pairs
bool_var = True                               # bool → True or False


# --------------------------------------------------
# 🔸 PRINTING & MANIPULATING VARIABLES
# --------------------------------------------------

print("Integer:", integer_var)                      # Output: Integer: 10
print("Float:", float_var)                          # Output: Float: 3.14
print("String:", string_var + " Bootcamp")          # Output: String: AI Bootcamp

# Working with Lists
list_var.append(4)                                  # Add new element
print("List:", list_var)                            # Output: List: [1, 2, 3, 4]

# Tuples are immutable (cannot be changed)
print("Tuple:", tuple_var)                          # Output: Tuple: (4, 5, 6)

# Accessing Dictionary values
print("Dictionary Value:", dict_var["role"])        # Output: Dictionary Value: Engineer

# Booleans represent logical states
print("Boolean:", bool_var)                         # Output: Boolean: True


# --------------------------------------------------
# 🔹 TYPE CHECKING & CONVERSION
# --------------------------------------------------
# You can check and convert between data types using:
# type(), int(), float(), str(), list(), tuple(), dict(), bool()

print(type(integer_var))        # Output: <class 'int'>
print(type(float_var))          # Output: <class 'float'>
print(type(string_var))         # Output: <class 'str'>

# Type Conversion Examples
num_str = "100"
print(int(num_str) + 50)        # Output: 150  (string → int conversion)

# Convert int → string
x = 42
print("Number: " + str(x))      # Output: Number: 42

# Convert list → tuple
print(tuple(list_var))          # Output: (1, 2, 3, 4)


# --------------------------------------------------
# 🔹 PYTHON IS DYNAMICALLY TYPED
# --------------------------------------------------
# You can assign different types to the same variable anytime.

data = 5
print(data, type(data))         # Output: 5 <class 'int'>
data = "Python"
print(data, type(data))         # Output: Python <class 'str'>


# --------------------------------------------------
# 🔹 IMMUTABLE vs MUTABLE TYPES
# --------------------------------------------------
# Mutable → Can be changed after creation (list, dict, set)
# Immutable → Cannot be changed (int, float, str, tuple)

# Mutable Example
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]

# Immutable Example
word = "Hi"
# word[0] = "P"   ❌ Error: strings are immutable
word = "Pi"       # ✅ Reassigning creates a new string
print(word)       # Output: Pi


# --------------------------------------------------
# 🔹 PRACTICAL USE IN PROJECTS
# --------------------------------------------------
# - int/float → calculations, scores, stats
# - str → names, messages, logs
# - list → storing multiple values (students, products)
# - tuple → fixed data like coordinates (x, y)
# - dict → structured data like user profiles
# - bool → decision making in conditions

# Example:
student = {
    "name": "Tushar",
    "age": 22,
    "enrolled": True,
    "skills": ["Python", "Data Analysis"]
}
print(student)
# Output: {'name': 'Tushar', 'age': 22, 'enrolled': True, 'skills': ['Python', 'Data Analysis']}


# --------------------------------------------------
# 🧩 PRACTICE EXERCISES
# --------------------------------------------------
# 1️⃣ Create variables for your name, age, and course. Print them nicely.
# 2️⃣ Convert a string number "25" into an integer and add 10.
# 3️⃣ Add an item to a list and remove another.
# 4️⃣ Create a dictionary for a book (title, author, pages) and print the author.
# 5️⃣ Explain the difference between mutable and immutable with examples.

# ✅ Tip:
# Practice printing and modifying each type until you can visualize how data flows.
# It helps you think like Python — everything is an object with properties and behaviors.
# --------------------------------------------------
