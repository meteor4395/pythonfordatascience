#%%
# classifying personal income
import pandas as pd
import numpy as np
import os
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

os.chdir("C:\\uhh\\nptel\\python for datascience\\w04")
data_income= pd.read_csv("income.csv")
data = data_income.copy()

# print(data.info())

# print(data.isnull().sum())

summary_num = data.describe()
# print(summary_num)

summary_cat = data.describe(include = "O")
print(summary_cat)

data['JobType'].value_counts()
data['occupation'].value_counts()

print(np.unique(data['JobType']))
print(np.unique(data['occupation']))

data = pd.read_csv("income.csv",na_values=[' ?'])
data.isnull().sum()

missing = data[data.isnull().any(axis=1)]
data2 = data.dropna(axis=0)

correlation_matrix = data2[['age', 'capitalgain', 'capitalloss', 'hoursperweek']].corr()
print(correlation_matrix)

data2.columns

gender = pd.crosstab(index = data2['gender'],
                     columns= 'count',
                     normalize = True
                     )
print(gender)

gender_salstat = pd.crosstab(index=data2["gender"],
                             columns=data2["SalStat"],
                             margins=True,
                             normalize='index')
print(gender_salstat)

SalSat = sns.countplot(x='SalStat', data=data2)
sns.displot(data2['age'], bins=10, kde=False)

sns.boxplot(y='SalStat', x='age', data=data2)
data2.groupby('SalStat')['age'].median()

data2 = data2.dropna(subset=['JobType'])
sns.barplot(y='SalStat', x='JobType', data=data2)

# %%
