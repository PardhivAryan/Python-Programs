import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None, 'Eve', 'Frank', 'Eve'],
    'Age': [25, 30, None, 22, 29, 25, None, 25],
    'Salary': [50000, 60000, 55000, None, 52000, 50000, 52000, 50000]
}
df = pd.DataFrame(data)

print("Original Data: ")
print(df)

# Data Cleaning
# 1. Checking missing values
print("\nMissing values in each column")
print(df.isnull()) # isnull() finds missing values → returns True
print(df.isnull().sum()) # .sum() Counts total True values (i.e., missing data) per column
print()

# 2. Fill missing Age with mean age
print("Fill missing Age with mean age: ")
df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)
print()

# 3. Fill missing Salary with median
print("Fill missing Salary with median: ")
df['Salary'].fillna(df['Salary'].median(), inplace=True)
print(df)
print()

# 4. Drop rows where Name is missing
print("Drop rows where Name is missing: ")
df.dropna(subset=['Name'], inplace=True)
print(df)
print()

# 5. Remove duplicate rows
print("Remove duplicate rows: ")
df.drop_duplicates(inplace=True)
print(df)
print()

print("Cleaned Data: ")
print(df)

# Data Visualizing
# 1. Bar plot of average Salary by Name
plt.figure(figsize=(8,5))
sns.barplot(x='Name', y='Salary', data=df)
plt.title('Salary by Name')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()

# 2. Histogram of Age distribution
plt.figure(figsize=(8,5))
plt.hist(df['Age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 3. Scatter plot: Age vs Salary
plt.figure(figsize=(8,5))
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()
