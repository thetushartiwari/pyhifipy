# ============================================================
# 🗓️ Day 8 – Advanced Python & Software Engineering Concepts
# ============================================================

# - Decorators
# - Iterators & Generators
# - Asyncio (Asynchronous programming)
# - Testing & Mocking basics
# - Bytecode, Garbage Collection, and Final Tips
# Everything is simplified for learning + interview prep.

# ------------------------------------------------------------
# 🔹 1. DECORATORS – “Functions that modify other functions”
# ------------------------------------------------------------
# Used to add extra functionality (like logging, auth, timing)
# without modifying the original function code.

def logger(func):
    """Decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        print(f"📜 Running {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} finished.\n")
        return result
    return wrapper

@logger
def greet(name):
    print(f"Hello, {name}!")

@logger
def add(a, b):
    return a + b

greet("Tushar")
print(add(5, 7))

# ✅ When to use:
# - Logging
# - Performance measurement
# - Authorization checks
# - Reusing pre/post logic easily


# ------------------------------------------------------------
# 🔹 2. ITERATORS & GENERATORS
# ------------------------------------------------------------
# Iterator = object that can be iterated (using next()).
# Generator = simpler way to create iterators using 'yield'.

# Example of iterator manually:
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2

# Example of generator:
def countdown(n):
    """Counts down from n to 1."""
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)

# ✅ When to use:
# - For large data / memory efficiency
# - Streaming APIs, log reading, etc.


# ------------------------------------------------------------
# 🔹 3. ASYNCIO – Asynchronous Programming
# ------------------------------------------------------------
# Lets you run tasks concurrently (not parallel).
# Best for I/O tasks (API calls, database, file operations).

import asyncio

async def fetch_data():
    print("📡 Fetching data...")
    await asyncio.sleep(2)  # simulate network delay
    print("✅ Data fetched!")
    return {"data": 123}

async def process_data():
    print("⚙️ Processing data...")
    await asyncio.sleep(1)
    print("✅ Processing done!")

async def main():
    # Run tasks concurrently
    await asyncio.gather(fetch_data(), process_data())

asyncio.run(main())

# ✅ When to use:
# - API requests
# - Web scraping
# - Async web frameworks (FastAPI, aiohttp)
# 🔹 Think: "async = non-blocking code execution"


# ------------------------------------------------------------
# 🔹 4. UNIT TESTING & MOCKING (Software Engineering Basics)
# ------------------------------------------------------------
# Helps test individual functions or modules automatically.

import unittest
from unittest.mock import patch

def get_discounted_price(price, discount):
    return price - (price * discount / 100)

class TestDiscount(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(get_discounted_price(100, 10), 90)

    @patch("__main__.get_discounted_price", return_value=80)
    def test_mocked_discount(self, mock_func):
        self.assertEqual(get_discounted_price(100, 10), 80)
        mock_func.assert_called_once()

if __name__ == "__main__":
    unittest.main(exit=False)

# ✅ When to use:
# - Writing maintainable, bug-free code
# - Simulate APIs or user inputs with mocking
# - Required in professional software testing


# ------------------------------------------------------------
# 🔹 5. BYTECODE, MEMORY & GARBAGE COLLECTION
# ------------------------------------------------------------
# Python converts code → Bytecode → Executes via the Python Virtual Machine (PVM)
# Bytecode = low-level instructions (stored in .pyc files)

import dis
def square(x): return x * x
dis.dis(square)  # Shows Python bytecode

# 🔹 Memory Management
# - Stack (function calls, local vars)
# - Heap (objects, data)
# - Garbage Collector automatically frees unused memory
# - Use `del` to delete references manually (rarely needed)

import gc
gc.collect()  # manually trigger garbage collection (not usually required)

# ✅ Tip: Use memory efficiently → prefer generators, avoid unnecessary global objects


# ------------------------------------------------------------
# 🔹 6. PYTHONIC PRACTICES (Real-World Good Habits)
# ------------------------------------------------------------
# ✅ Use list comprehensions
squares = [x**2 for x in range(5)]     # [0, 1, 4, 9, 16]

# ✅ Use with-statement for file handling
with open("data.txt", "w") as f:
    f.write("Clean and safe file handling!")

# ✅ Use enumerate() and zip()
for i, fruit in enumerate(["apple", "banana", "cherry"]):
    print(i, fruit)

names = ["Tushar", "Ananya"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ✅ Use f-strings for readability
name = "Python"
print(f"{name} is awesome!")


# ------------------------------------------------------------
# 🧠 7. INTERVIEW QUICK RECAP
# ------------------------------------------------------------
# ✅ Decorators → Add extra behavior to functions
# ✅ Generators → Yield values one at a time (save memory)
# ✅ Asyncio → Run I/O tasks concurrently (non-blocking)
# ✅ Testing & Mocking → Ensure correctness + simulate real cases
# ✅ Bytecode → Internal Python translation of your code
# ✅ Garbage Collection → Automatic memory cleanup
# ✅ Pythonic Tips → Clean, readable, efficient code

# ------------------------------------------------------------
# 🧩 8. FINAL SOFTWARE ENGINEERING TIPS
# ------------------------------------------------------------
# - Follow PEP-8 (Python style guide)
# - Write modular, testable code
# - Use virtual environments for isolation
# - Use logging instead of print()
# - Always handle exceptions properly