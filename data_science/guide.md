# 🧠 Data Science Practical Guide – From Data to Insights

*A complete hands-on workbook for learning, practicing, and revising data analysis in Python.*

---

## 🌍 1. Foundations of Data Science

### 🔹 What Is Data Science?

Data Science is the process of extracting **insights and knowledge** from data using:

* **Math & Statistics**
* **Programming (mainly Python)**
* **Domain Understanding**
* **Data Visualization & Communication**

**Goal:** Convert raw data → information → insights → decisions.

### 🔹 Typical Workflow

1. **Define Problem** → What question are we solving?
2. **Collect Data** → CSVs, APIs, databases, sensors.
3. **Clean Data** → Handle missing, duplicates, outliers.
4. **Explore (EDA)** → Summaries, visualizations, relationships.
5. **Model** → Regression, classification, clustering, etc.
6. **Interpret & Communicate** → Insights, visuals, reports.

> 💡 Tip: In most real-world cases, **80% of your time** goes into data cleaning and EDA, not modeling!

---

## ⚙️ 2. NumPy – Numerical Computing

### 🔹 Why NumPy?

NumPy provides high-speed mathematical operations and memory-efficient arrays.

```python
import numpy as np

# Creating arrays
a = np.array([1, 2, 3])
b = np.arange(4, 7)

print(a + b)  # Output: [5 7 9]
print(a * 2)  # Output: [2 4 6]
```

### 🔹 Key Operations

```python
matrix = np.array([[1, 2], [3, 4]])
print(matrix.T)         # Transpose
print(np.mean(matrix))  # Average value
print(np.std(matrix))   # Standard deviation
```

### 🔹 Broadcasting

Allows operations between arrays of **different shapes**.

```python
m = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([1, 0, -1])
print(m + v)
# Output:
# [[2 2 2]
#  [5 5 5]]
```

> 🧩 **Use Tip:** NumPy is ideal for mathematical computing before data enters Pandas.

---

## 🧾 3. Pandas – Data Manipulation & Cleaning

### 🔹 Data Structures

* **Series:** 1D labeled array
* **DataFrame:** 2D labeled table (rows & columns)

```python
import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)
# Output:
#     Name  Age
# 0  Alice   25
# 1    Bob   30
```

### 🔹 Reading / Writing Data

```python
df = pd.read_csv("data.csv")   # Read
df.to_csv("output.csv", index=False)  # Write
```

### 🔹 Cleaning & Handling Missing Data

```python
df["Age"].fillna(df["Age"].mean(), inplace=True)
df.drop_duplicates(inplace=True)
```

### 🔹 Filtering, Sorting, Aggregating

```python
print(df[df["Age"] > 25])
df.sort_values(by="Age", inplace=True)
df.groupby("Department")["Salary"].mean()
```

> 💡 **Use Tip:**
>
> * Pandas = Data wrangling powerhouse.
> * Combine with NumPy for numerical operations.

---

## 📊 4. Data Visualization – Matplotlib & Seaborn

### 🔹 Matplotlib Basics

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, color="blue", marker="o")
plt.title("Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()
```

### 🔹 Seaborn – High-level Visualization

```python
import seaborn as sns
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

sns.histplot(df["sepal_length"], kde=True, color="purple")
plt.title("Sepal Length Distribution")
plt.show()
```

### 🔹 Correlation Heatmap

```python
corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Feature Correlations")
plt.show()
```

> 🎨 **Use Tip:**
>
> * **Matplotlib** → Full control & customization
> * **Seaborn** → Cleaner, faster, statistical plots

---

## 🔍 5. EDA (Exploratory Data Analysis)

### 🔹 Step-by-Step EDA Process

1. **Understand the dataset**

   ```python
   print(df.info())
   print(df.describe())
   print(df.isnull().sum())
   ```

2. **Handle missing/outliers**

   ```python
   df["Age"].fillna(df["Age"].median(), inplace=True)
   df = df[df["Fare"] < 500]  # remove outliers
   ```

3. **Explore relationships**

   ```python
   sns.boxplot(x="Pclass", y="Age", data=df)
   sns.countplot(x="Survived", data=df)
   ```

4. **Visual Summary**

   ```python
   sns.pairplot(df, hue="Survived")
   plt.show()
   ```

> 🧠 **Goal:** Reveal trends, correlations, and anomalies before modeling.

---

## 📈 6. From EDA to Insights

### 🔹 Aggregation

```python
summary = df.groupby("Pclass")["Fare"].agg(["mean", "max", "min"])
print(summary)
```

### 🔹 Feature Relationships

* Use **pairplot** for numeric relations
* Use **barplot** or **countplot** for categorical relations

### 🔹 Communication

End every analysis with:

* Key findings (insights)
* Supporting visual evidence
* Business interpretation


