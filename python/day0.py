# ==================================================
# DAY 0 – GETTING STARTED WITH PYTHON
# Foundations every programmer should know before writing code.
# ==================================================


# --------------------------------------------------
# 🔹 1. WHAT HAPPENS WHEN YOU RUN A PYTHON PROGRAM
# --------------------------------------------------
# Step-by-step (behind the scenes):
# 1️⃣ You write Python code (human-readable).
# 2️⃣ The Python Interpreter converts it to *bytecode* (.pyc internally).
# 3️⃣ The Python Virtual Machine (PVM) executes that bytecode line by line.
# 4️⃣ During execution, Python automatically manages memory for variables, data, etc.

# Simple example:
x = 10
y = 20
z = x + y
print(z)   # Output: 30

# When executed:
# - Variables (x, y, z) are created in memory.
# - Objects (10, 20, 30) are stored on the HEAP.
# - The variable names (x, y, z) are references stored in the STACK.
# In short → Names live on stack, data lives on heap.


# --------------------------------------------------
# 🔹 2. STACK vs HEAP (Simple and Important!)
# --------------------------------------------------
# 🧩 STACK:
# - Stores *function calls* and *local variable references*.
# - Works like a plate stack (LIFO – Last In, First Out).
# - When a function ends, its stack frame is deleted.

# 🧱 HEAP:
# - Stores *actual objects* (lists, dicts, strings, etc).
# - Managed automatically by Python’s *Garbage Collector (GC)*.
# - Slower but flexible — data can live beyond one function call.

# Example:
def add_numbers(a, b):
    result = a + b  # 'result' in stack; (a+b) object on heap
    return result

sum_result = add_numbers(5, 10)
print(sum_result)  # Output: 15

# 🧠 Memory flow:
# 1. When add_numbers() is called → new *stack frame* created.
# 2. Variables (a, b, result) go into that stack frame.
# 3. Values (5, 10, 15) live on heap.
# 4. After return → stack frame removed, but result (15) still lives on heap because main code references it.


# --------------------------------------------------
# 🔹 3. VARIABLES & REFERENCES
# --------------------------------------------------
# Python variables are *references*, not boxes like in C.
# They point to objects stored on the heap.

x = [1, 2, 3]
y = x   # y points to the same object as x
y.append(4)
print(x)  # Output: [1, 2, 3, 4]
# Both x and y reference the same list (heap object).


# --------------------------------------------------
# 🔹 4. IMMUTABLE vs MUTABLE OBJECTS
# --------------------------------------------------
# Mutable objects → Can be changed in place (list, dict, set)
# Immutable objects → Cannot be changed (int, str, tuple)

# Example:
a = 10
b = a
b += 5
print(a, b)   # Output: 10, 15 (new object created for b → immutability)

lst1 = [1, 2]
lst2 = lst1
lst2.append(3)
print(lst1, lst2)  # Output: [1, 2, 3], [1, 2, 3] (same object → mutable)

# ✅ Tip:
# - Use mutable types when you want to modify data.
# - Use immutable when you need safety and consistency (e.g. keys in dicts).


# --------------------------------------------------
# 🔹 5. GARBAGE COLLECTION (Simplified)
# --------------------------------------------------
# Python uses *reference counting* + *cyclic garbage collection*.
# When no variable refers to an object → memory is freed automatically.

x = [1, 2, 3]
x = None   # Old list [1,2,3] becomes unreferenced → GC cleans it.

# You rarely need to worry about freeing memory manually.
# But in large apps, keep an eye on object references to avoid memory leaks.


# --------------------------------------------------
# 🔹 6. PYTHON EXECUTION MODEL (Simple Diagram)
# --------------------------------------------------
# 🧩 How Python organizes memory during execution:
#
#   ┌──────────────────────────────┐
#   │        STACK (function calls)│
#   │  ┌────────────────────────┐  │
#   │  │ main()                │  │
#   │  │ ├─ x ─┐               │  │
#   │  │ ├─ y ─┐               │  │
#   │  │ └─ z ─┘               │  │
#   │  └────────────────────────┘  │
#   │                              │
#   │   Each function → new frame  │
#   └──────────────┬───────────────┘
#                  │
#   ┌──────────────▼───────────────┐
#   │         HEAP (objects)       │
#   │  [10], [20], [30], [list]   │
#   │  {'key': 'value'}           │
#   └──────────────────────────────┘
#
# Stack stores variable names, heap stores actual objects.


# --------------------------------------------------
# 🔹 7. BUILT-IN MEMORY INSPECTION TOOLS
# --------------------------------------------------
# To explore memory in real use:
import sys

num = 1000
print(sys.getsizeof(num))   # Shows memory (in bytes) used by object

text = "Python"
print(sys.getsizeof(text))  # Strings also take memory for metadata

# ✅ Tip:
# In interviews → mention sys.getsizeof() and id() to show understanding.


# --------------------------------------------------
# 🔹 8. WHY THIS MATTERS (REAL-WORLD USE)
# --------------------------------------------------
# - Explains why copies, memory leaks, and recursion behave the way they do.
# - Helps in writing memory-efficient code.
# - Crucial for understanding DSA (stack operations, recursion, pointers in lists, etc.).
# - Often asked in interviews: “Where are variables stored?”, “What’s stack vs heap?”, “What is immutability?”


# --------------------------------------------------
# ✅ SUMMARY – DAY 0 PYTHON FOUNDATIONS
# --------------------------------------------------
# 1️⃣ Code runs via Python interpreter → bytecode → PVM executes.
# 2️⃣ Names (variables) live on stack; data lives on heap.
# 3️⃣ Immutable = new object; Mutable = same object modified.
# 4️⃣ Garbage Collector automatically clears unused objects.
# 5️⃣ Memory concepts help you understand recursion, data structures, and performance.
# --------------------------------------------------
