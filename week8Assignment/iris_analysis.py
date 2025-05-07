import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    print("First 5 rows of the dataset:")
    print(df.head())

    print("\nData types and missing values:")
    print(df.info())

    print("\nMissing values:\n", df.isnull().sum())
except Exception as e:
    print("Error loading the dataset:", e)

# Task 2: Basic Data Analysis
print("\nBasic statistics:")
print(df.describe())

print("\nAverage values per species:")
print(df.groupby('species').mean())

# Task 3: Data Visualization
sns.set(style="whitegrid")

# Line Chart (just as a trend example using cumulative sum)
df["row_index"] = range(len(df))
df["cumulative_petal_length"] = df["petal length (cm)"].cumsum()
plt.figure(figsize=(8, 5))
plt.plot(df["row_index"], df["cumulative_petal_length"])
plt.title("Cumulative Petal Length Over Observations")
plt.xlabel("Observation Index")
plt.ylabel("Cumulative Petal Length (cm)")
plt.grid(True)
plt.show()

# Bar Chart
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)', data=df, estimator='mean', ci=None)
plt.title("Average Petal Length by Species")
plt.ylabel("Petal Length (cm)")
plt.xlabel("Species")
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species")
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# Findings
print("\nFindings:")
print("- Iris-virginica tends to have longer petal lengths.")
print("- Sepal width has a relatively normal distribution.")
print("- Petal length and sepal length have a strong positive correlation.")
