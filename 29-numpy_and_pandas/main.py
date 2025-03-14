import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("Shape:", arr.shape)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))

arr2 = np.array([10, 20, 30, 40, 50])
print("Element-wise Addition:", arr + arr2)
print("Element-wise Multiplication:", arr * arr2)

data = {
    "Name": ["Alice", "Bob", "John"],
    "Age": [25, 30, 27],
    "Salary": [40000, 60000, 70000]
}

df = pd.DataFrame(data)
print(df)

df = pd.read_csv("employees.csv")
print(df.head())  # Display first 5 rows

high_salary = df[df["Salary"] > 55000]
print(high_salary)

print("Average Age:", df["Age"].mean())
print("Total Salary", df["Salary"].sum())

# 1. Apply NumPy on a Real-World Dataset
# You can use NumPy to perform mathematical operations on large datasets. Try:
# Loading a CSV file into NumPy using np.loadtxt() or np.genfromtxt().
# Performing statistical operations like mean, median, standard deviation, etc.
# Normalizing or transforming numerical data.

data = np.loadtxt("numerical_data.csv", delimiter=",", skiprows=1)

mean_value = np.mean(data, axis=0)
std_dev = np.std(data, axis=0)
print("Mean:", mean_value)
print("Standard Deviation:", std_dev)


# 2. Perform Data Cleaning with Pandas
# Pandas is great for handling messy data. You can:
# Handle missing values (dropna(), fillna())
# Remove duplicates (drop_duplicates())
# Convert data types (astype())
# Filter and sort data

# Create sample data with some missing values
data = pd.read_csv("cleaning_data.csv")

# Check for missing values
print(df.isnull().sum())

# Fill missing values with the column mean
df['value'] = df['value'].fillna(df['value'].mean())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert a column to a different data type
df["date"] = pd.to_datetime(df["date"], errors='coerce')

print(df.head())

# 3. Visualize Data with Matplotlib or Seaborn
# Create sample data
data = {
    'category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'value': [10, 15, 8, 12, 14, 9]
}
df = pd.read_csv("sample_data.csv")

# Bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x="category", y="value", data=df)
plt.title("Category-wise Value Distribution")
plt.show()

# Histogram
plt.hist(df["value"], bins=10, color="skyblue", edgecolor="black")
plt.title("Value Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()