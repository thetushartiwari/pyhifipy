# ==================================================
# DAY 4 – PYTHON DATA STRUCTURES (Collections)
# ==================================================
# Lists | Tuples | Sets | Dictionaries
# These are the main data-holding types in Python.
# ==================================================

# --------------------------------------------------
# 🔹 1. LISTS
# --------------------------------------------------
# ✅ Mutable (can be changed)
# ✅ Ordered (maintains order)
# ✅ Can hold mixed data types

numbers = [1, 2, 3, 4]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True]

print(numbers[2])   # Output: 3
print(fruits[-1])   # Output: cherry
print(mixed[1])     # Output: apple

# 🔸 Common List Operations
fruits.append("orange")       # Add at end
fruits.insert(1, "grape")     # Insert at index 1
print(fruits)                 # Output: ['apple', 'grape', 'banana', 'cherry', 'orange']

# Slicing
sliced_fruits = fruits[2:4]
print(sliced_fruits)          # Output: ['banana', 'cherry']

# Removing items
fruits.remove("banana")       # Remove specific value
print(fruits)                 # Output: ['apple', 'grape', 'cherry', 'orange']

del fruits[0]                 # Delete by index
print(fruits)                 # Output: ['grape', 'cherry', 'orange']

fruits.pop()                  # Removes last item
print(fruits)                 # Output: ['grape', 'cherry']

# ✅ When to use lists:
# - When you need a flexible, ordered collection that you can modify.
# - Commonly used for sequences, queues, dynamic data.


# --------------------------------------------------
# 🔹 2. TUPLES
# --------------------------------------------------
# ✅ Immutable (cannot be changed)
# ✅ Ordered
# ✅ Faster and memory efficient compared to lists

colors = ("red", "green", "blue")
single_item = ("glass",)  # NOTE: Must include a comma for single-element tuple

print(colors[0])   # Output: red
print(colors[-1])  # Output: blue

# ✅ When to use tuples:
# - When data should not change (coordinates, constants, fixed info)
# - Good for dictionary keys or safe data passing

# ⚡Tip:
# Tuples are immutable → less overhead → slightly faster than lists.


# --------------------------------------------------
# 🔹 3. SETS
# --------------------------------------------------
# ✅ Unordered (no index)
# ✅ No duplicates allowed
# ✅ Mutable (can add/remove)
# ✅ Useful for mathematical operations like union, intersection, etc.

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 - set2)        # Difference → {1, 2}
print(set1 | set2)        # Union → {1, 2, 3, 4, 5}
print(set1 & set2)        # Intersection → {3}
print(set1 ^ set2)        # Symmetric Difference → {1, 2, 4, 5}

# ✅ When to use sets:
# - When you need unique items only.
# - Great for removing duplicates, membership checks, or mathematical set logic.


# --------------------------------------------------
# 🔹 4. DICTIONARIES
# --------------------------------------------------
# ✅ Key-Value pairs
# ✅ Mutable and Unordered (in Python 3.7+, maintains insertion order)
# ✅ Fast lookups

student = {"name": "Alice", "age": 25, "grade": "A"}
print(student["name"])   # Output: Alice

# Loop through keys and values
for key, value in student.items():
    print(key, ":", value)
# Output:
# name : Alice
# age : 25
# grade : A

# Add / Update values
student["subject"] = "Math"
student["age"] = 32
print(student)
# Output: {'name': 'Alice', 'age': 32, 'grade': 'A', 'subject': 'Math'}

# Delete items
del student["grade"]
print(student)  # Output: {'name': 'Alice', 'age': 32, 'subject': 'Math'}

student.pop("subject")
print(student)  # Output: {'name': 'Alice', 'age': 32}

# ✅ When to use dicts:
# - When data has a “key:value” relation (name → score, id → info).
# - Excellent for fast lookups, JSON-style data, or structured info.


# --------------------------------------------------
# 🔹 5. MINI PROJECT EXAMPLE – WORD FREQUENCY COUNTER
# --------------------------------------------------
# Demonstrates practical dictionary use.
# Counts word frequency in a given sentence.

def word_frequency(sentence: str):
    """Counts how many times each word appears."""
    words = sentence.split()       # Split by spaces
    word_count = {}
    for word in words:
        word = word.lower()        # Ignore case
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(word_frequency("Hello hello world world"))
# Output: {'hello': 2, 'world': 2}

# ✅ When to use this logic:
# - Text analysis, NLP preprocessing, log analysis, etc.


# --------------------------------------------------
# 🔹 6. PRACTICAL EXAMPLE – UPDATE AND CLEAN A RECORD
# --------------------------------------------------
person = {"name": "Alice", "age": 25, "grade": "A"}
print(person)
# Output: {'name': 'Alice', 'age': 25, 'grade': 'A'}

# Add new data
person["address"] = "123 Main St"

# Update an existing value
person["age"] = 32

# Remove unwanted keys safely
if "grade" in person:
    del person["grade"]

print(person)
# Output: {'name': 'Alice', 'age': 32, 'address': '123 Main St'}


# --------------------------------------------------
# 🔹 7. OPTIONAL INTERACTIVE EXAMPLE
# --------------------------------------------------
# Uncomment to try this manually in a terminal.
"""
sentence = input("Enter a sentence: ")
word_count = {}
for word in sentence.split():
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
"""


# --------------------------------------------------
# ✅ SUMMARY (REVISION QUICK NOTES)
# --------------------------------------------------
# 🟢 LIST → Mutable, Ordered, Duplicates allowed
# 🔵 TUPLE → Immutable, Ordered, Faster
# 🟣 SET → Mutable, Unordered, No duplicates
# 🟠 DICT → Key:Value, Mutable, Fast lookups
# --------------------------------------------------
# 💡 Quick Use-Cases:
# - LIST → Dynamic data (shopping list, scores)
# - TUPLE → Fixed data (coordinates, constants)
# - SET → Unique data (remove duplicates, IDs)
# - DICT → Mapping data (user info, word count)
# --------------------------------------------------
