# ==============================================================
# DAY 3 – DATA VISUALIZATION WITH MATPLOTLIB & SEABORN
# ==============================================================

# 📘 Overview:
# Data visualization is a key step in Data Science. It helps in exploring,
# understanding, and communicating data patterns effectively.
# 
# 👉 Matplotlib → Low-level plotting library for static charts.
# 👉 Seaborn     → High-level library built on Matplotlib for
#                  statistical and beautiful visualizations.

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# ==============================================================
# 🧮 1. BASIC MATPLOTLIB VISUALS
# ==============================================================

# 🔹 Line Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, label="Trend", color="orange", linestyle="--", marker="x")
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Output: Orange dashed line with 'x' markers showing trend

# --------------------------------------------------------------
# 🔹 Scatter Plot – To show relationships between two numerical variables
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 85]

plt.scatter(hours_studied, exam_scores, color="red")
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.show()

# Output: Red points showing upward correlation (more hours → higher scores)

# --------------------------------------------------------------
# 🔹 Bar Chart – Compare categories
categories = ["Electronics", "Clothing", "Groceries"]
revenue = [250, 400, 150]

plt.bar(categories, revenue, color="green", edgecolor="black")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

# Output: Green bars for each category’s revenue

# --------------------------------------------------------------
# 🔹 Histogram – Show frequency distribution
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

plt.hist(data, bins=4, color="skyblue", edgecolor="black")
plt.title("Histogram Example")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# Output: Blue bars showing how often each number appears

# --------------------------------------------------------------
# 🔹 Multiple Lines – Compare trends
years = [2010, 2011, 2012, 2013]
sales = [100, 120, 140, 160]
profit = [20, 25, 30, 35]

plt.plot(years, sales, label="Sales", color="blue", marker="o")
plt.plot(years, profit, label="Profit", color="orange", marker="s")
plt.title("Sales & Profit over Years")
plt.xlabel("Years")
plt.ylabel("Value")
plt.legend()
plt.show()

# Output: Two line plots – Sales (blue circles) and Profit (orange squares)

# ==============================================================
# 🌈 2. ADVANCED VISUALIZATION WITH SEABORN
# ==============================================================

# Seaborn automatically styles plots beautifully and is
# best suited for statistical and exploratory data analysis.

# Load Iris Dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print("\nDataset Loaded:\n", df.head())

# --------------------------------------------------------------
# 🔹 Pairplot – Relationship between all numeric columns
sns.pairplot(df, hue="species", palette="husl")
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()

# Output: Scatter matrix showing pairwise relationships between features,
# colored by species.

# --------------------------------------------------------------
# 🔹 Heatmap – Show correlation between numeric variables
# Remove non-numeric column
df_numeric = df.drop(columns=["species"])

# Calculate correlation matrix
correlation_matrix = df_numeric.corr()

# Plot Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap (Iris Dataset)")
plt.show()

# Output: Square grid showing correlation values (-1 to +1).
# Strong correlations appear in dark red/blue.

# --------------------------------------------------------------
# 🔹 Boxplot – Detect outliers and view distributions
sns.boxplot(x="species", y="sepal_length", data=df, palette="Set2")
plt.title("Boxplot of Sepal Length by Species")
plt.show()

# Output: Three boxplots comparing sepal lengths across Iris species.

# --------------------------------------------------------------
# 🔹 Violin Plot – Combination of boxplot + KDE (distribution shape)
sns.violinplot(x="species", y="petal_length", data=df, palette="muted")
plt.title("Violin Plot of Petal Length by Species")
plt.show()

# Output: Smooth violin-shaped plots showing distribution + median line.

# --------------------------------------------------------------
# 🔹 Countplot – Frequency of categorical data
sns.countplot(x="species", data=df, palette="pastel")
plt.title("Count of Each Species")
plt.show()

# Output: Bar chart showing how many samples belong to each Iris species.

# --------------------------------------------------------------
# 🔹 Distplot / Histplot – Distribution of single variable
sns.histplot(df["sepal_length"], bins=10, kde=True, color="teal")
plt.title("Distribution of Sepal Length")
plt.show()

# Output: Histogram with KDE (bell curve) showing data distribution.

# ==============================================================
# ⚙️ 3. CUSTOMIZING PLOTS
# ==============================================================

# Seaborn style settings
sns.set_style("whitegrid")  # Other options: dark, ticks, white
sns.set_palette("husl")

# Example with custom style
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, s=80)
plt.title("Customized Scatter Plot")
plt.show()

# ==============================================================
# 🧠 INTERVIEW & REVISION NOTES
# ==============================================================

# ✅ Matplotlib Basics:
#   - plt.plot() → Line Plot
#   - plt.bar() → Bar Chart
#   - plt.hist() → Histogram
#   - plt.scatter() → Scatter Plot
#
# ✅ Seaborn Basics:
#   - sns.pairplot(), sns.heatmap(), sns.boxplot(), sns.countplot()
#
# ✅ Real-world Tip:
#   - Always visualize before modeling.
#   - Use Heatmap to identify correlated variables (avoid multicollinearity).
#   - Use Pairplot to detect relationships for feature engineering.
#
# ✅ Common Interview Qs:
#   1. Difference between Matplotlib and Seaborn?
#   2. What is a heatmap used for?
#   3. How do you detect outliers visually?
#   4. What is KDE in histograms?
#
# ✅ Quick Practice:
#   - Visualize your CSV data with histograms and scatter plots.
#   - Create boxplots for numeric columns by category.
#   - Build correlation heatmaps to understand relationships.
