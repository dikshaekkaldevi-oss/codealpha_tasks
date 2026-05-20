# TASK 2 - Exploratory Data Analysis (EDA)
# Project: HR Analytics

#required libraries
import pandas as pd
import matplotlib.pyplot as plt

# loading the dataset
df = pd.read_csv("HR_Analytics.csv")

# Viewing first 5 records
print("First 5 rows of dataset:\n")
print(df.head())

# Checking basic information
print("\nDataset Information:\n")
print(df.info())

'''info() prints:
total rows and columns
data types of columns
non-null values'''

# Checking missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Checking duplicate rows
print("\nDuplicate Rows:\n")
print(df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:\n")
print(df.describe())
# describe() prints: mean,minimum value, maximum value and standard deviation

# Attrition analysis
print("\nAttrition Count:\n")
attrition = df['Attrition'].value_counts()

print(attrition)

# Department analysis
print("\nEmployees in each department:\n")
dept = df['Department'].value_counts()

print(dept)
# shows which department has more employees

# Job satisfaction vs income
print("\nAverage Monthly Income based on Job Satisfaction:\n")
satisfaction = df.groupby('JobSatisfaction')['MonthlyIncome'].mean()

print(satisfaction)
# checking whether higher satisfaction is related to better income

# Age distribution chart
df['Age'].plot(kind='hist')

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show() # histogram graph

# Attrition chart
attrition.plot(kind='bar')

plt.title("Attrition Count")
plt.xlabel("Attrition")
plt.ylabel("Employees")

plt.show() #bar chart

# Department chart
dept.plot(kind='bar')

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")

plt.show()

# Monthly income analysis
income = df.groupby('Department')['MonthlyIncome'].mean()

income.plot(kind='bar')

plt.title("Average Income by Department")
plt.xlabel("Department")
plt.ylabel("Average Income")

plt.show()
