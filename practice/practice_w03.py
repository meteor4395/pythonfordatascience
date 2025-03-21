#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 
os.chdir("C:\\uhh\\nptel\\python for datascience\\practice")
#%%
df = pd.read_csv("mtcars.csv") #1
df.head()
sns.scatterplot(x='mpg',y = 'wt',data=df)
# %%
df2 = pd.read_csv("diamond.csv") #2
sns.boxplot(x='cut',y='price',data=df2)
highest_median_cut = df2.groupby('cut')['price'].median().index[0]
print(df2.groupby('cut')['price'].median())
print(f"The category under 'cut' with the highest median price is: {highest_median_cut}")
# %%
df3 = pd.read_csv("churn.csv") #3
df3['TotalCharges'].isnull().sum()
# %%
