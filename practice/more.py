import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data.csv')


bins = list(range(0, data['Number of Screens'].max() + 300, 300))
data['screens_binned'] = pd.cut(data['Number of Screens'], bins=bins)

#  bin
screen_counts = data['screens_binned'].value_counts().sort_index()

# bar plot to  between binned number of screens and verdicts
plt.figure(figsize=(12, 6))
sns.barplot(x=screen_counts.index.astype(str), y=screen_counts.values)
plt.xticks(rotation=90)
plt.xlabel('Number of Screens (binned)')
plt.ylabel('Count')
plt.title('Distribution of Number of Screens')
plt.show()

# box plot to binned number of screens and verdicts
plt.figure(figsize=(12, 6))
sns.boxplot(x='screens_binned', y='Verdict', data=data)
plt.xticks(rotation=90)
plt.xlabel('Number of Screens (binned)')
plt.ylabel('Verdict')
plt.title('Relation between Number of Screens and Verdicts')
plt.show()

