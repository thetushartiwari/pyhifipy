# ==================================================
# Day 5 – Strings & Regular Expressions (Regex)
# ==================================================

# Strings are sequences of characters enclosed in single (' '), double (" "), or triple quotes (''' ''' or """ """).

# ==============================================
# 🔹 Basic String Operations
# ==============================================

sentence = "Python is fun"

# split() → breaks the string into a list based on spaces (default)
words = sentence.split()
print(words)  # Output: ['Python', 'is', 'fun']

# join() → joins list elements into a single string with a separator
new_sentence = "|".join(words)
print(new_sentence)  # Output: Python|is|fun

# replace() → replaces part of a string with another string
text = "I love Java"
updated_text = text.replace("Java", "Python")
print(updated_text)  # Output: I love Python

# strip() → removes leading and trailing whitespaces
messy = "     Hello, World     "
print(messy)  # Output: "     Hello, World     "
cleaned_text = messy.strip()
print(cleaned_text)  # Output: "Hello, World"


# ==============================================
# 🔹 Text Cleaning Example (Regex + String methods)
# ==============================================

import re

def clean_text(text):
    """Cleans text by removing punctuation, extra spaces, and converting to lowercase."""
    text = re.sub(r"[^\w\s]", "", text)   # Remove punctuation
    text = " ".join(text.split())         # Remove extra spaces
    return text.lower()                   # Convert to lowercase

input_text = "   Hello, World.!!! Welcome to Python, Programming....    "
cleaned_text = clean_text(input_text)
print("Cleaned Text:", cleaned_text)
# Output: Cleaned Text: hello world welcome to python programming


# ==============================================
# 🔹 Palindrome Checker (Logic Practice)
# ==============================================
# A palindrome reads the same backward and forward (e.g., "madam", "racecar")

def is_palindrome(text):
    """Checks whether a given text is a palindrome or not."""
    # Keep only alphanumeric characters and make them lowercase
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]  # Compare with its reverse

input_text = "Madam"
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:
    print(f'"{input_text}" is not a palindrome.')
# Output: "Madam" is a palindrome.


# ==============================================
# 🔹 Introduction to Regex (Regular Expressions)
# ==============================================
# Regex is used for pattern matching — searching, validating, or extracting text data.

# \d → matches digits
# \w → matches word characters (letters, digits, underscore)
# \s → matches whitespace
# +  → one or more occurrences
# *  → zero or more occurrences
# ^  → starts with
# $  → ends with
# [] → character set

text = "Contact me at 123-456-7890 or 9876543210"

# findall() → extracts all matches of a pattern
digits = re.findall(r"\d+", text)
print(digits)  
# Output: ['123', '456', '7890', '9876543210']

# sub() → replaces pattern matches with another string
updated_text = re.sub(r"\d", "X", text)
print(updated_text)
# Output: Contact me at XXX-XXX-XXXX or XXXXXXXXXX


# ==============================================
# 🔹 Practical Tips
# ==============================================
# ✅ Use .split() and .join() to clean and format strings.
# ✅ Use .replace() and .strip() for sanitizing user input.
# ✅ Use regex for searching, validating (emails, phone numbers, etc.).
# ✅ Practice writing regex patterns by testing on small examples.
# ✅ Reuse helper functions like clean_text() in projects (data cleaning, NLP, etc.).

