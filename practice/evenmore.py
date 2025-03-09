import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV data
df = pd.read_csv('data.csv')

# Clean up the currency values
df['Budget(INR)'] = df['Budget(INR)'].str.replace('₹', '').str.replace(',', '').astype(float)
df['Revenue(INR)'] = df['Revenue(INR)'].str.replace('₹', '').str.replace(',', '').astype(float)

# Calculate ROI (Return on Investment)
df['ROI'] = (df['Revenue(INR)'] - df['Budget(INR)']) / df['Budget(INR)']

# Create various visualizations

# 1. Success Rate by Genre
plt.figure(figsize=(15, 6))
success_by_genre = df.groupby('Genre')['Verdict'].value_counts().unstack()
success_by_genre.plot(kind='bar', stacked=True)
plt.title('Movie Success Rate by Genre')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Budget vs Revenue by Verdict
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='Budget(INR)', y='Revenue(INR)', hue='Verdict', alpha=0.6)
plt.title('Budget vs Revenue by Verdict')
plt.xlabel('Budget (INR)')
plt.ylabel('Revenue (INR)')
plt.tight_layout()
plt.show()

# 3. Success Rate by Release Period
plt.figure(figsize=(10, 6))
success_by_period = df.groupby('Release Period')['Verdict'].value_counts().unstack()
success_by_period.plot(kind='bar', stacked=True)
plt.title('Movie Success Rate by Release Period')
plt.xlabel('Release Period')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.show()

# 4. Average ROI by Genre
plt.figure(figsize=(15, 6))
avg_roi_by_genre = df.groupby('Genre')['ROI'].mean().sort_values(ascending=False)
avg_roi_by_genre.plot(kind='bar')
plt.title('Average ROI by Genre')
plt.xlabel('Genre')
plt.ylabel('Average ROI')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Success Rate for New vs Established Actors
plt.figure(figsize=(10, 6))
success_by_new_actor = df.groupby('new actor')['Verdict'].value_counts().unstack()
success_by_new_actor.plot(kind='bar', stacked=True)
plt.title('Success Rate: New vs Established Actors')
plt.xlabel('New Actor (1=Yes, 0=No)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.show()

# 6. Distribution of Number of Screens by Verdict
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Verdict', y='Number of Screens')
plt.title('Distribution of Number of Screens by Verdict')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Monthly Distribution of Successful Movies
plt.figure(figsize=(12, 6))
df['Month'] = pd.to_datetime(df['Release Date']).dt.month
success_by_month = df[df['Verdict'].isin(['Hit', 'Blockbuster'])].groupby('Month').size()
success_by_month.plot(kind='bar')
plt.title('Distribution of Successful Movies by Month')
plt.xlabel('Month')
plt.ylabel('Number of Successful Movies')
plt.xticks(range(12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.tight_layout()
plt.show()

# 8. ROI Distribution by Verdict
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='Verdict', y='ROI')
plt.title('ROI Distribution by Verdict')
plt.xticks(rotation=45)
plt.ylabel('Return on Investment (ROI)')
plt.tight_layout()
plt.show()

# 9. Budget Distribution by Genre
plt.figure(figsize=(15, 6))
sns.boxplot(data=df, x='Genre', y='Budget(INR)')
plt.title('Budget Distribution by Genre')
plt.xticks(rotation=45)
plt.ylabel('Budget (INR)')
plt.tight_layout()
plt.show()

# 10. Correlation Heatmap
numeric_columns = ['Budget(INR)', 'Revenue(INR)', 'Number of Screens', 'ROI']
plt.figure(figsize=(10, 8))
sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Numeric Variables')
plt.tight_layout()
plt.show()

# 11. Success Rate by Budget Range
df['Budget_Range'] = pd.qcut(df['Budget(INR)'], q=5, labels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])
plt.figure(figsize=(12, 6))
success_by_budget = df.groupby('Budget_Range')['Verdict'].value_counts().unstack()
success_by_budget.plot(kind='bar', stacked=True)
plt.title('Success Rate by Budget Range')
plt.xlabel('Budget Range')
plt.ylabel('Number of Movies')
plt.legend(title='Verdict')
plt.tight_layout()
plt.show()

# 12. Revenue to Budget Ratio by Genre
df['Revenue_to_Budget_Ratio'] = df['Revenue(INR)'] / df['Budget(INR)']
plt.figure(figsize=(15, 6))
sns.boxplot(data=df, x='Genre', y='Revenue_to_Budget_Ratio')
plt.title('Revenue to Budget Ratio by Genre')
plt.xticks(rotation=45)
plt.ylabel('Revenue to Budget Ratio')
plt.tight_layout()
plt.show()

# Key findings analysis
print("\nKey Findings:")
print("\n1. Genre Success Rates:")
genre_success = df.groupby('Genre')['Verdict'].apply(lambda x: (x == 'Hit').mean() + (x == 'Blockbuster').mean())
print(genre_success.sort_values(ascending=False).head())

print("\n2. Average Budget by Verdict:")
print(df.groupby('Verdict')['Budget(INR)'].mean().sort_values(ascending=False))

print("\n3. Success Rate by Release Period:")
release_success = df.groupby('Release Period')['Verdict'].apply(lambda x: (x == 'Hit').mean() + (x == 'Blockbuster').mean())
print(release_success)

print("\n4. New Actor Success Rate:")
new_actor_success = df.groupby('new actor')['Verdict'].apply(lambda x: (x == 'Hit').mean() + (x == 'Blockbuster').mean())
print(new_actor_success)

# Additional Key Findings Analysis
print("\n5. Monthly Success Distribution:")
monthly_success_rate = df[df['Verdict'].isin(['Hit', 'Blockbuster'])].groupby('Month').size()
print(monthly_success_rate.sort_values(ascending=False).head())

print("\n6. Average Revenue to Budget Ratio by Genre:")
avg_ratio_by_genre = df.groupby('Genre')['Revenue_to_Budget_Ratio'].mean().sort_values(ascending=False)
print(avg_ratio_by_genre.head())

print("\n7. Success Rate by Budget Range:")
budget_success = df.groupby('Budget_Range')['Verdict'].apply(
    lambda x: (x == 'Hit').mean() + (x == 'Blockbuster').mean()
)
print(budget_success)