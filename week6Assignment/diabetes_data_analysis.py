# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('diabetes_prediction_dataset.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
except pd.errors.EmptyDataError:
    print("No data in the file.")
except Exception as e:
    print(f"An error occurred: {e}")

df.info()

# get an overview of the data
print(df.describe())

# Display the first few rows of the dataset
print(df.head())

# Checks and counts all the genders in the dataset
print(df['gender'].value_counts())

# Checks and counts all the unique smoking history groups in the dataset
print(df['smoking_history'].value_counts())

print(df.isnull().sum())

plt.plot(df['diabetes'])
plt.title('Diabetes Trend')
plt.xlabel('Index')
plt.ylabel('Diabetes')
plt.show()

smoking_avg = df.groupby('smoking_history')['diabetes'].mean()
smoking_avg.plot(kind='bar', color=['green', 'blue', 'red', 'purple', 'orange', 'pink'])
plt.title('Average Diabetes per Smoking History')
plt.xlabel('Smoking History')
plt.ylabel('Average Diabetes')
plt.xticks(rotation=0)
plt.show()

df['heart_disease'].plot(kind='hist', bins=10, color='purple', alpha=0.7)
plt.title('Distribution of Heart Disease')
plt.xlabel('Heart Disease')
plt.ylabel('Frequency')
plt.show()

# Optional: set a theme for cleaner plots
sns.set(style="whitegrid")

# Example: scatter plot of sepal length vs petal length
sns.scatterplot(data=df, x='diabetes', y='HbA1c_level', hue='gender')
plt.title("Diabetes vs HbA1c_level by Gender")
plt.xlabel("Diabetes")
plt.ylabel("HbA1c_level")
plt.show()