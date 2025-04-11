# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sns

# Load the Iris dataset from sklearn
data = load_iris()

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data=data.data, columns=data.feature_names)

# Add target labels (species)
df['species'] = data.target

# Display the first few rows of the dataset
df.head()

# Check the data types and missing values
print(df.info())

# Check for any missing values
print(df.isnull().sum())

# Drop rows with missing values (if any)
df.dropna(inplace=True)

# Or, fill missing values (if any)
df.fillna(df.mean(), inplace=True)

# Compute basic statistics for numerical columns
print(df.describe())

# Group by 'species' and compute the mean of numerical columns
grouped = df.groupby('species').mean()

print(grouped)

# Example line chart (we can use the Sepal Length for illustration)
plt.plot(df['sepal length (cm)'])
plt.title('Sepal Length Trend')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.show()

# Bar chart showing the average sepal length per species
species_avg = df.groupby('species')['sepal length (cm)'].mean()
species_avg.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.xticks(rotation=0)
plt.show()

# Histogram for the Sepal Length
df['sepal length (cm)'].plot(kind='hist', bins=10, color='purple', alpha=0.7)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot between Sepal Length and Petal Length
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], alpha=0.7)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()

# Optional: set a theme for cleaner plots
sns.set(style="whitegrid")

# Example: scatter plot of sepal length vs petal length
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()