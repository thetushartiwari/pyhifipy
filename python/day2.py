# ==================================================
# DAY 2 – CONTROL FLOW & LOOPS
# ==================================================
# Learn how Python makes decisions and repeats actions efficiently.
# Includes: if-elif-else, nested conditions, for & while loops,
# and loop control statements (break, continue, pass).
# ==================================================


# --------------------------------------------------
# 🔹 CONDITIONAL STATEMENTS – if, elif, else
# --------------------------------------------------
# Used to perform different actions based on conditions.
# Python checks top-to-bottom and executes the first True condition.

num = -50

if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")
# Output: Negative Number


# --------------------------------------------------
# 🔸 Nested Conditions
# --------------------------------------------------
# You can put one if inside another,
# but logical operators (and/or) are usually cleaner.

age = 3
if age > 18:
    if age < 30:
        print("Young Adult")
    else:
        print("Adult")

# ✅ Better way using logical operator:
if 18 < age < 30:
    print("Young Adult")
# Output (for age = 3): Nothing printed (condition False)

# ✅ When to use if/elif/else:
# - When you need to make decisions
# - Example: checking login, eligibility, ranges, grades, etc.


# ==================================================
# 🔹 LOOPS IN PYTHON
# ==================================================
# Loops repeat a code block multiple times.
# Two main loops: for and while.
# Use loops to automate repetitive logic.
# ==================================================


# --------------------------------------------------
# 🔸 FOR LOOP → Use when you KNOW how many times to repeat
# --------------------------------------------------
# Syntax:
# for variable in sequence:
#     <code block>

# Example 1: Using range()
for i in range(5):  # Loops from 0 to 4
    print(i)
# Output: 0, 1, 2, 3, 4

# Example 2: range(start, stop, step)
for i in range(2, 11, 2):
    print(i)
# Output: 2, 4, 6, 8, 10

# Example 3: Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry


# ✅ When to use for loop:
# - You know how many times to iterate
# - Iterating over lists, strings, tuples, sets, or ranges
# - Cleaner and safer than while for fixed loops


# --------------------------------------------------
# 🔸 WHILE LOOP → Use when you DON'T know how many times to repeat
# --------------------------------------------------
# Syntax:
# while condition:
#     <code block>

# Example 1: Countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Outside While Loop")
# Output:
# 5
# 4
# 3
# 2
# 1
# Outside While Loop


# Example 2: Keep asking input until user stops
# (uncomment to test)
# num = int(input("Enter a number (0 to stop): "))
# while num != 0:
#     print("You entered:", num)
#     num = int(input("Enter a number (0 to stop): "))
# print("Loop ended!")
# Example Output:
# Enter a number (0 to stop): 3
# You entered: 3
# Enter a number (0 to stop): 4
# You entered: 4
# Enter a number (0 to stop): 0
# Loop ended!

# ✅ When to use while loop:
# - You don’t know the exact count
# - Use when looping depends on a condition or user input


# --------------------------------------------------
# 🔹 LOOP CONTROL STATEMENTS
# --------------------------------------------------
# Control how your loop behaves:
# - break → Exit the loop completely.
# - continue → Skip current iteration, go to next.
# - pass → Placeholder; does nothing (used for future code).

for i in range(5):
    if i == 2:
        continue     # Skip printing 2
    if i == 4:
        break        # Stop loop completely when i == 4
    print(i)
# Output:
# 0
# 1
# 3



# --------------------------------------------------
# 🧩 PRACTICAL COMPARISON
# --------------------------------------------------
# for loop → known range or sequence
# while loop → unknown repetitions (based on condition)
# if → decision-making
# break → emergency exit
# continue → skip and move on
# pass → placeholder for future logic


# --------------------------------------------------
# 💡 MINI PRACTICE CHALLENGES
# --------------------------------------------------
# 1️⃣ Print all even numbers from 1 to 10 using for loop.
# 2️⃣ Print numbers 10 to 1 using while loop.
# 3️⃣ Ask user for 5 numbers; print only positive ones.
# 4️⃣ Skip 5 and stop loop if number is greater than 8 (use continue & break).
# 5️⃣ Use pass in a loop to handle invalid inputs later.

# ✅ Tip: Always trace your loops carefully — print variables inside loops
# to see how they change and help debug logic.
# --------------------------------------------------
