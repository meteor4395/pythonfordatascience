import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('data.csv')

# Data Cleaning
data = data.dropna()
data['Budget(INR)'] = data['Budget(INR)'].replace('[\₹,]', '', regex=True).astype(float)
data['Revenue(INR)'] = data['Revenue(INR)'].replace('[\₹,]', '', regex=True).astype(float)

# Exploratory Data Analysis
print(data.describe())
print(data.info())

# Feature Engineering
data['Profit'] = data['Revenue(INR)'] - data['Budget(INR)']
data['Profit Margin'] = data['Profit'] / data['Budget(INR)']

# Correlation Analysis
# correlation_matrix = data[['Budget(INR)', 'Revenue(INR)', 'Profit', 'Profit Margin', 'Verdict']].corr()
# print(correlation_matrix['Profit'].sort_values(ascending=False))

# # Visualization
# plt.figure(figsize=(10, 6))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.show()

# Scatter plot of Budget vs Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Budget(INR)', y='Revenue(INR)', hue='Verdict', data=data)
plt.title('Budget vs Revenue')
plt.show()

# Box plot of Profit Margin by Verdict
plt.figure(figsize=(10, 6))
sns.boxplot(x='Verdict', y='Profit Margin', data=data)
plt.title('Profit Margin by Verdict')
plt.show()
 

# Correlation between Genre and Verdict
genre_verdict_crosstab = pd.crosstab(data['Genre'], data['Verdict'])
genre_verdict_correlation = genre_verdict_crosstab.corr()
print(genre_verdict_correlation)

# Visualization of the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(genre_verdict_correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix between Genre and Verdict')
plt.show()