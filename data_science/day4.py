# ============================================
# Day 4 – Exploratory Data Analysis (EDA)
# ============================================
# EDA = Understanding your dataset deeply before modeling
# Goal: Identify patterns, clean data, detect anomalies, & visualize relationships

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------
# 1️⃣ Load Dataset
# -----------------------------------------------------
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Quick Overview
print("🔹 Basic Info:")
print(df.info())
# ➤ Output shows number of non-null entries, data types, and column names.

print("\n🔹 Summary Statistics:")
print(df.describe())
# ➤ Helps check data ranges, missing values, and possible outliers.

# -----------------------------------------------------
# 2️⃣ Handle Missing Values
# -----------------------------------------------------
# Fill missing Age with median (less affected by outliers)
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked with mode (most common value)
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\n✅ Missing values handled successfully!")
print(df.isnull().sum())
# ➤ Output: All columns should now have 0 missing values.

# -----------------------------------------------------
# 3️⃣ Remove Duplicates
# -----------------------------------------------------
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print(f"\n🧹 Removed {before - after} duplicate rows.")
# ➤ Ensures clean data for unbiased analysis.

# -----------------------------------------------------
# 4️⃣ Filter Data Example
# -----------------------------------------------------
first_class = df[df["Pclass"] == 1]
print("\n🎩 First Class Passengers:")
print(first_class.head())
# ➤ Shows only passengers from Class 1.

# -----------------------------------------------------
# 5️⃣ Survival Rate by Class (Bar Chart)
# -----------------------------------------------------
survival_by_class = df.groupby("Pclass")["Survived"].mean()
print("\n🚢 Survival Rate by Class:")
print(survival_by_class)
# ➤ Output Example:
# Pclass
# 1    0.629630
# 2    0.472826
# 3    0.242363

survival_by_class.plot(kind="bar", color="skyblue")
plt.title("Survival Rate by Class")
plt.ylabel("Survival Rate")
plt.xlabel("Passenger Class")
plt.show()
# ➤ Visualization Tip:
#     - Class 1 passengers had higher survival chance.
#     - Indicates socioeconomic influence.

# -----------------------------------------------------
# 6️⃣ Age Distribution (Histogram)
# -----------------------------------------------------
sns.histplot(df["Age"], kde=True, bins=20, color="purple")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
# ➤ Interpretation:
#     - KDE curve shows density (probability).
#     - Helps spot if data is skewed or multimodal.

# -----------------------------------------------------
# 7️⃣ Age vs Fare Relationship (Scatter Plot)
# -----------------------------------------------------
plt.scatter(df["Age"], df["Fare"], alpha=0.6, color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
# ➤ Output:
#     - Each point = passenger
#     - Older passengers tend to have higher fares (maybe 1st class bias)

# -----------------------------------------------------
# 8️⃣ Correlation Heatmap
# -----------------------------------------------------
numeric_df = df.select_dtypes(include=["number"])
corr = numeric_df.corr()
print("\n📊 Correlation Matrix:")
print(corr)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Titanic Dataset")
plt.show()
# ➤ Insights:
#     - Check strong correlations (Fare ↔ Pclass, Age ↔ SibSp, etc.)
#     - Helps feature selection in ML.

# -----------------------------------------------------
# ✅ Summary Tip:
# -----------------------------------------------------
# ➤ EDA Steps to Remember (Interview Tip):
#     1. df.info() + df.describe() → quick scan
#     2. Handle NaN & Duplicates
#     3. Group, Filter, Aggregate
#     4. Visualize distributions (hist/box)
#     5. Find correlations (heatmap, pairplot)
#     6. Document insights before modeling
