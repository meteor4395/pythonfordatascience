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

# One-hot encoding for Genre
genre_encoded = pd.get_dummies(data['Genre'], prefix='Genre')

# Concatenate the one-hot encoded columns with the original DataFrame
data = pd.concat([data, genre_encoded], axis=1)

# Encode Verdict as numerical values
verdict_mapping = {'Flop': 0, 'Average': 1, 'Hit': 2, 'Blockbuster': 3}
data['Verdict'] = data['Verdict'].map(verdict_mapping)

# Exclude non-numeric columns for correlation analysis
numeric_data = data.select_dtypes(include=[np.number])

# Ensure genre columns are included in numeric_data
numeric_data = numeric_data.join(genre_encoded)

# Correlation Analysis
correlation_matrix = numeric_data.corr()
genre_columns = genre_encoded.columns
genre_verdict_correlation = correlation_matrix.loc[genre_columns, 'Verdict']
print(genre_verdict_correlation)

# Visualization of the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(genre_verdict_correlation.to_frame(), annot=True, cmap='coolwarm')
plt.title('Correlation between Genre and Verdict')
plt.show()

# scatter plot of number of screens vs verdict
sns.histplot(x='Number of Screens', y='Verdict', data=data)
plt.title('Number of Screens vs Verdict')
plt.show()

# Encode Release Period as numerical values
release_period_mapping = {'Holiday': 1, 'Normal Day': 0}
data['Release Period'] = data['Release Period'].map(release_period_mapping)

# Update numeric_data to include Release Period
numeric_data['Release Period'] = data['Release Period']

# Correlation between Release Period and Verdict
release_period_verdict_correlation = numeric_data['Release Period'].corr(numeric_data['Verdict'])
print(f'Correlation between Release Period and Verdict: {release_period_verdict_correlation}')

# Visualization of the correlation
plt.figure(figsize=(6, 4))
sns.heatmap(pd.DataFrame(release_period_verdict_correlation, index=['Release Period'], columns=['Verdict']), annot=True, cmap='coolwarm')
plt.title('Correlation between Release Period and Verdict')
plt.show()

# Create a correlation matrix for all numeric features including the mapped Verdict
full_correlation_matrix = numeric_data.corr()

# Print the full correlation matrix
print(full_correlation_matrix)

# Visualization of the full correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(full_correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Full Correlation Matrix')
plt.show()