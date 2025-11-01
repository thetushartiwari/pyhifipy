# ============================================================
# Day 6 – File Handling & Exceptions 
# ============================================================

# ------------------------------------------------------------
# 🌟 1. FILE HANDLING – Reading, Writing, Appending
# ------------------------------------------------------------

# In Python, files are opened using the built-in `open()` function.
# Syntax: open("filename", "mode")
# Modes:
# 'r' – read only     | 'w' – write (overwrites)
# 'a' – append        | 'x' – create new file
# 'r+' – read & write | 'w+' – write & read (overwrites)

# Example 1: Writing to a file
with open("notes.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is my first file write operation.")
print("✅ File created and text written successfully.")

# Example 2: Reading from a file
with open("notes.txt", "r") as file:
    content = file.read()
    print("\n📄 File content:\n", content)

# Example 3: Appending to an existing file
with open("notes.txt", "a") as file:
    file.write("\nAdding a new line at the end.")
print("✅ Line appended successfully!")

# Example 4: Reading line by line
with open("notes.txt", "r") as file:
    for line in file:
        print("🔹", line.strip())  # .strip() removes spaces & newline


# ------------------------------------------------------------
# 📁 2. OS & SYS MODULES (Basic Understanding)
# ------------------------------------------------------------

# `os` = gives access to system operations (create, delete, check files)
# `sys` = gives information about the Python runtime environment

import os
import sys

# Check if a file exists before reading it
print("\nChecking file existence:")
if os.path.exists("notes.txt"):
    print("✅ File exists.")
else:
    print("❌ File does not exist.")

# Get current working directory
print("📂 Current Directory:", os.getcwd())

# Show Python version
print("🐍 Python version:", sys.version)


# ------------------------------------------------------------
# ⚠️ 3. EXCEPTION HANDLING (try, except, else, finally)
# ------------------------------------------------------------

# Errors cause program crashes if not handled.
# We use `try-except` to handle them safely.

# Example 1: Basic try-except
try:
    num = int(input("\nEnter a number: "))
    print("You entered:", num)
except ValueError:
    print("❌ Invalid input! Please enter a number.")

# Example 2: Handling missing file
try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("⚠️ The file does not exist!")

# Example 3: Multiple Exceptions
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("❌ Please enter a valid number.")
except ZeroDivisionError:
    print("🚫 Division by zero not allowed.")
else:
    print("✅ No errors! Result =", y)
finally:
    print("🔚 This block always runs (cleanup code here).")

# `finally` is used for code that must run no matter what (like closing files or connections).


# ------------------------------------------------------------
# 📊 4. SMALL UTILITY FUNCTIONS (with Exception Handling)
# ------------------------------------------------------------

def count_words_and_lines(filename):
    """Counts lines and words in a file safely."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            return len(lines), word_count
    except FileNotFoundError:
        print("⚠️ File not found!")
        return 0, 0

lines, words = count_words_and_lines("notes.txt")
print(f"\n📘 Lines = {lines}, Words = {words}")


# ------------------------------------------------------------
# 🧠 5. WHAT IS __name__ == "__main__" ?
# ------------------------------------------------------------

# Every Python file can act as:
# (a) a script to run directly, or
# (b) a module to import elsewhere.

# When you run a file directly → __name__ becomes "__main__"
# When imported → __name__ becomes the file name.

def greet():
    print("👋 Hello from main program!")

if __name__ == "__main__":
    greet()

# ✅ This ensures that certain code only runs when the file is executed,
# not when imported into another program.



# ------------------------------------------------------------
# ✨ Quick Revision Summary
# ------------------------------------------------------------
# ✅ File Modes: r, w, a, x, r+, w+
# ✅ with open() handles file closing automatically
# ✅ os – interact with system (check files, directories)
# ✅ sys – access runtime details (Python version, args)
# ✅ try, except, else, finally → for safe error handling
# ✅ __main__ → ensures code runs only when executed directly
# ------------------------------------------------------------
