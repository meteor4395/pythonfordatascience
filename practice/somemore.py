import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Load the data
data = pd.read_csv('data.csv')

# Data Cleaning
# Drop rows with missing values
data = data.dropna()

# Remove unnecessary columns
columns_to_drop = ['Release Period2', 'Release Period3', 'Whether Remake', 'Whether Franchise', 'New Actor2', 'New Director2', 'New Music Director']
data = data.drop(columns=columns_to_drop)

# Convert Budget(INR) and Revenue(INR) to numeric values
data['Budget(INR)'] = data['Budget(INR)'].replace('[\₹,]', '', regex=True).replace(',', '', regex=True).astype(float)
data['Revenue(INR)'] = data['Revenue(INR)'].replace('[\₹,]', '', regex=True).replace(',', '', regex=True).astype(float)

# Encode categorical columns
verdict_mapping = {'Flop': 0, 'Average': 1, 'Hit': 2, 'Blockbuster': 3}
data['Verdict'] = data['Verdict'].map(verdict_mapping)

# Display cleaned data
print(data.head())

# Save cleaned data to a new CSV file
data.to_csv('cleaned_data.csv', index=False)

data.describe()

# Remove outliers in Budget(INR) using IQR method
Q1 = data['Budget(INR)'].quantile(0.25)
Q3 = data['Budget(INR)'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

data = data[(data['Budget(INR)'] >= lower_bound) & (data['Budget(INR)'] <= upper_bound)]

# Display data after removing outliers
print(data.head())

# Create 10 bins for Budget(INR)
data['Budget_Bins'] = pd.cut(data['Budget(INR)'], bins=10, labels=False)

# Display data with budget bins
print(data.head())

# Exclude budget bins 1
data = data[data['Budget_Bins'] != 0]
data = data[data['Budget_Bins'] != 1]

# Plot Budget Bins against Verdict
plt.figure(figsize=(12, 6))
sns.countplot(x='Budget_Bins', hue='Verdict', data=data)
sns.set_theme(style="whitegrid")
plt.title('Budget Bins vs Verdict')
plt.xlabel('Budget Range (in Millions)')
plt.ylabel('Count')
plt.legend(title='Verdict', loc='upper right')

# Show the range of the bins in the plot with proper formatting
bin_edges = pd.cut(data['Budget(INR)'], bins=10).categories
bin_ranges = [f'{int(edge.left/1000000):,}M - {int(edge.right/1000000):,}M' for edge in bin_edges]
plt.xticks(ticks=range(len(bin_ranges)), labels=bin_ranges, rotation=45, ha='right')

# Adjust layout to prevent label cutoff
plt.tight_layout()
plt.show()