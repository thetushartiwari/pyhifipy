# ==============================================================
# DAY 2 - PANDAS FOR DATA MANIPULATION & ANALYSIS
# ==============================================================

# 🧠 What is Pandas?
# Pandas is a powerful Python library for data manipulation, cleaning,
# transformation, and analysis.
# It provides two main data structures:
#   1️⃣ Series → 1D labeled array (like one column in Excel)
#   2️⃣ DataFrame → 2D labeled table (like an Excel sheet)
# Pandas is built on top of NumPy and integrates well with libraries
# like Matplotlib, Seaborn, and Scikit-learn.

import pandas as pd
import numpy as np

# ==============================================================
# 🧩 1. SERIES (ONE-DIMENSIONAL DATA)
# ==============================================================

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("Series:\n", s)
# Output:
# a    10
# b    20
# c    30
# dtype: int64

# Accessing elements
print("\nAccess element by index label:", s["b"])  # 20
print("Access element by position:", s.iloc[1])    # 20

# 📝 Tip:
# Series are great for representing simple 1D data like temperatures,
# daily sales, or one column extracted from a DataFrame.

# ==============================================================
# 🧱 2. DATAFRAME (TWO-DIMENSIONAL DATA)
# ==============================================================

data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)
# Output:
#       Name  Age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35

# ==============================================================
# 📋 3. VIEWING DATA
# ==============================================================

print("\nFirst 2 rows:\n", df.head(2))
# Output:
#     Name  Age
# 0  Alice   25
# 1    Bob   30

print("\nLast row:\n", df.tail(1))
# Output:
#       Name  Age
# 2  Charlie   35

print("\nInfo:")
print(df.info())
# Output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    3 non-null      object
#  1   Age     3 non-null      int64
# dtypes: int64(1), object(1)

print("\nStatistical Summary:\n", df.describe())
# Output:
#              Age
# count   3.000000
# mean   30.000000
# std     5.000000
# min    25.000000
# 25%    27.500000
# 50%    30.000000
# 75%    32.500000
# max    35.000000

# Selecting columns
print("\nSelecting 'Name' column:\n", df["Name"])
# Output:
# 0      Alice
# 1        Bob
# 2    Charlie
# Name: Name, dtype: object

# Filtering rows
print("\nPeople older than 25:\n", df[df["Age"] > 25])
# Output:
#       Name  Age
# 1      Bob   30
# 2  Charlie   35

# ==============================================================
# 🎯 4. INDEXING AND SELECTION
# ==============================================================

print("\nUsing iloc (by position):\n", df.iloc[0])
# Output:
# Name    Alice
# Age        25
# Name: 0, dtype: object

print("\nUsing loc (by label):\n", df.loc[1, "Name"])
# Output: Bob

# ==============================================================
# 📂 5. READING & WRITING DATA
# ==============================================================
# df = pd.read_csv("data.csv")         # Load CSV
# df.to_csv("output.csv", index=False) # Save CSV
# df = pd.read_excel("data.xlsx")      # Load Excel
# df.to_excel("data.xlsx", index=False)

# ✅ Tip:
# Use `pd.read_csv(URL)` to directly load online datasets.

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print("\nLoaded Dataset (Iris):\n", df.head())
# Output shows first 5 rows of the iris dataset

print("\nColumns:", df.columns.tolist())
# Output:
# ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Filter data
filtered = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("\nFiltered Rows (setosa with sepal_length > 5):\n", filtered.head())
# Output: rows of setosa with sepal_length > 5

# ==============================================================
# 🧹 6. DATA CLEANING (MISSING VALUES)
# ==============================================================

data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, np.nan, 30, 35],
    "Score": [85, 90, np.nan, 88],
}
df = pd.DataFrame(data)
print("\nOriginal Dataset:\n", df)
# Output:
#     Name   Age  Score
# 0  Alice  25.0   85.0
# 1    Bob   NaN   90.0
# 2    NaN  30.0    NaN
# 3  David  35.0   88.0

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()  # Linear fill for numeric values
print("\nAfter Handling Missing Values:\n", df)
# Output:
#     Name   Age  Score
# 0  Alice  25.0   85.0
# 1    Bob  30.0   90.0
# 2    NaN  30.0   89.0
# 3  David  35.0   88.0

# Rename columns
df = df.rename(columns={"Name": "Student_Name", "Score": "Exam_Score"})
print("\nAfter Renaming Columns:\n", df)

# ==============================================================
# 🔗 7. MERGING, JOINING & CONCATENATION
# ==============================================================

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
})
df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Score": [85, 90, 88],
})

print("\nDataset 1:\n", df1)
print("\nDataset 2:\n", df2)

# Merge on common column
merged = pd.merge(df1, df2, how="inner", on="ID")
print("\nMerged Dataset:\n", merged)
# Output:
#    ID     Name  Age  Score
# 0   1    Alice   25     85
# 1   2      Bob   30     90
# 2   3  Charlie   35     88

# Add derived column
merged["Score_Percentage"] = (merged["Score"] / 200) * 100
print("\nAfter Transformation:\n", merged)
# Output includes a new Score_Percentage column

# Concatenation Example
concat_rows = pd.concat([df1, df1], axis=0)
print("\nConcatenated Rows:\n", concat_rows.head())

concat_cols = pd.concat([df1, df2], axis=1)
print("\nConcatenated Columns:\n", concat_cols.head())

# ==============================================================
# 📊 8. GROUPING & AGGREGATION
# ==============================================================

grouped = merged.groupby("Age")["Score"].mean()
print("\nAverage Score by Age:\n", grouped)
# Output: mean score for each Age

agg_stats = merged.groupby("Age").agg({"Score": ["mean", "max", "min"]})
print("\nAggregated Statistics:\n", agg_stats)

# Custom function example
def score_range(x):
    return x.max() - x.min()

print("\nScore Range by Age:\n", merged.groupby("Age")["Score"].agg(score_range))

# ==============================================================
# 🧮 9. PIVOT TABLES
# ==============================================================
pivot = merged.pivot_table(values="Score", index="Age", aggfunc="mean")
print("\nPivot Table (Average Score by Age):\n", pivot)
# Output: pivot table showing average Score by Age

# ==============================================================
# 💡 INTERVIEW & PRACTICAL TIPS
# ==============================================================
# ✅ loc vs iloc
#   - loc → label-based
#   - iloc → index-based
#
# ✅ Missing Values:
#   - df.dropna()  → remove missing rows
#   - df.fillna(value) → replace with custom value
#   - df.interpolate() → fill using linear interpolation
#
# ✅ Combining Data:
#   - merge() → joins like SQL
#   - concat() → stacks data vertically/horizontally
#   - join() → joins on index
#
# ✅ Grouping & Aggregation:
#   - df.groupby("col").mean(), sum(), agg()
#   - df.pivot_table() → Excel-style summary table
#
# 🧠 Real-world Tip:
# Always inspect data first:
#   df.info(), df.describe(), df.isnull().sum()
#
# Most data preprocessing in ML pipelines happens with Pandas
# before modeling.
