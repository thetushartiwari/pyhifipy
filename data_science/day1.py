# ==================================================

# DAY 1 – NUMPY FOR NUMERICAL COMPUTING

# ==================================================

# NumPy (Numerical Python) is a core library for numerical and matrix operations.

# It's faster and more efficient than Python lists.

# Foundation for data science & machine learning libraries (pandas, TensorFlow, etc.)

# --------------------------------------------------

import numpy as np

# ==================================================

# 1️⃣ INTRODUCTION & ARRAY CREATION

# ==================================================

# Arrays are containers for data of the same type.

# They are more memory-efficient and faster than lists.

# Create a simple 1D array

arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Output: [1 2 3 4 5]

# Create a 2D array (Matrix)

arr2 = np.array([[1, 2, 3],
[4, 5, 6]])
print("2D Array:\n", arr2)

# Output:

# [[1 2 3]

# [4 5 6]]

# ==================================================

# Common Built-in Functions for Array Creation

# ==================================================

print("Zeros:\n", np.zeros((2, 3)))

# Creates 2x3 array of zeros

# Output:

# [[0. 0. 0.]

# [0. 0. 0.]]

print("Ones:\n", np.ones((2, 3)))

# Creates 2x3 array of ones

print("Arange (start, stop, step):", np.arange(1, 10, 2))

# Similar to range() in Python

# Output: [1 3 5 7 9]

print("Linspace (start, stop, num):", np.linspace(0, 1, 5))

# Creates evenly spaced values between start and stop

# Output: [0.   0.25 0.5  0.75 1.  ]

# 💡 Tip:

# - Use np.arange() for integer sequences.

# - Use np.linspace() when you want fixed number of points in an interval.

# ==================================================

# 2️⃣ BASIC ARRAY OPERATIONS

# ==================================================

a = np.arange(1, 6)
b = np.arange(6, 11)

print("a =", a)   # [1 2 3 4 5]
print("b =", b)   # [ 6  7  8  9 10]

# Element-wise operations

print("Add:", a + b)        # [ 7  9 11 13 15]
print("Subtract:", a - b)   # [-5 -5 -5 -5 -5]
print("Multiply:", a * b)   # [ 6 14 24 36 50]
print("Divide:", a / b)     # [0.1667 0.2857 0.375  0.444  0.5  ]

# 💡 Tip:

# NumPy operations apply element-wise — no loops required!

# Much faster than iterating through lists.

# ==================================================

# 3️⃣ INDEXING, SLICING, & RESHAPING

# ==================================================

arr = np.array([10, 20, 30, 40, 50, 60])

print("Element at index 2:", arr[2])     # 30
print("Last element:", arr[-1])          # 60
print("Slice [1:4]:", arr[1:4])          # [20 30 40]
print("Slice [3:]:", arr[3:])            # [40 50 60]

reshaped = arr.reshape(2, 3)
print("Reshaped (2x3):\n", reshaped)

# Output:

# [[10 20 30]

# [40 50 60]]

# 💡 Tip:

# reshape() changes the structure without changing data.

# Total number of elements must remain same.

# ==================================================

# 4️⃣ MATRIX OPERATIONS

# ==================================================

matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])

print("Original Matrix:\n", matrix)

# Transpose

print("Transpose:\n", matrix.T)

# Output:

# [[1 4 7]

# [2 5 8]

# [3 6 9]]

another_matrix = np.array([[9, 8, 7],
[6, 5, 4],
[3, 2, 1]])

print("Addition:\n", matrix + another_matrix)

# Output:

# [[10 10 10]

# [10 10 10]

# [10 10 10]]

print("Element-wise Multiplication:\n", matrix * another_matrix)

# Output:

# [[ 9 16 21]

# [24 25 24]

# [21 16  9]]

# 💡 Tip:

# For matrix multiplication (dot product), use np.dot(A, B) or A @ B

# ==================================================

# 5️⃣ BROADCASTING

# ==================================================

# Broadcasting allows arithmetic operations between arrays of different shapes.

# The smaller array is "stretched" to match the shape of the larger one.

matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
vector = np.array([1, 0, -1])

print("Matrix:\n", matrix)
print("Vector:", vector)

# Add vector to each row

print("Matrix + Vector:\n", matrix + vector)

# Output:

# [[2 2 2]

# [5 5 5]

# [8 8 8]]

print("Matrix * 2:\n", matrix * 2)

# Output:

# [[ 2  4  6]

# [ 8 10 12]

# [14 16 18]]

# 💡 Tip:

# Broadcasting reduces need for loops & increases speed.

# Often used in feature scaling or normalization in ML.

# ==================================================

# 6️⃣ AGGREGATION FUNCTIONS

# ==================================================

# Used for summarizing and analyzing data quickly.

dataset = np.random.randint(1, 51, size=(5, 5))
print("Original Dataset:\n", dataset)

# Output: Random 5x5 matrix

# Filter and replace

dataset[dataset > 25] = 0
print("Modified Dataset (values >25 → 0):\n", dataset)

# Aggregations

print("Sum:", np.sum(dataset))
print("Mean:", np.mean(dataset))
print("Std Deviation:", np.std(dataset))
print("Max:", np.max(dataset))
print("Min:", np.min(dataset))

# 💡 Tip:

# These are vectorized operations — extremely fast.

# Used for analytics, data summaries, feature scaling, etc.

# ==================================================

# 7️⃣ RANDOM NUMBERS & SEEDING

# ==================================================

# Random numbers are used in simulations, ML data splits, etc.

np.random.seed(42)  # Seed ensures reproducibility

random_array = np.random.rand(3, 3)
print("Random Float Array:\n", random_array)

# Output (same each time due to seed):

# [[0.3745 0.9507 0.7319]

# [0.5986 0.1560 0.1559]

# [0.0581 0.8661 0.6011]]

random_integers = np.random.randint(0, 10, size=(2, 3))
print("Random Integer Array:\n", random_integers)

# Output:

# [[7 4 3]

# [7 2 5]]

# 💡 Tip:

# np.random.rand → random floats [0,1)

# np.random.randint → random integers

# Always use np.random.seed() for reproducible results in experiments

# ==================================================

# 🧩 QUICK RECAP

# ==================================================

# ✅ np.array() → Create arrays

# ✅ np.zeros(), np.ones(), np.arange(), np.linspace() → Generate arrays

# ✅ arr.reshape() → Change shape

# ✅ arr.T → Transpose

# ✅ Broadcasting → Operate on different shaped arrays

# ✅ np.sum(), np.mean(), np.std() → Aggregate functions

# ✅ np.random → Generate random numbers

# ✅ np.random.seed() → For reproducibility