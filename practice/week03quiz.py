#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#%%
df = pd.read_csv("C:\\uhh\\nptel\\python for datascience\\practice\\flavors_of_cocoa.csv")
print(df.isnull().sum())  #  6

print(df['Company Location'].value_counts()) #7

print(df.info()) #8
df=df['Review Date'].astype('datetime64[ns]')
print(df.info())

#%%
df = pd.read_csv("C:\\uhh\\nptel\\python for datascience\\practice\\flavors_of_cocoa.csv")
print(df['Rating'].max()) #9


# %%
