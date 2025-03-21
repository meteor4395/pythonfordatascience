#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os


os.chdir("C:\\uhh\\nptel\\python for datascience\\examprep")
df = pd.read_csv("apy.csv")
df['Season'] = df['Season'].str.strip()
# %%
sum = df[df['Season']=='Summer']
sum_cr = sum['Crop'].unique()
print(sum_cr)
# %%
hr= df[df['State_Name']=='Haryana']
hr_prd = hr.groupby('Crop_Year')['Production'].sum().sort_values(ascending=False)
print(hr_prd)
# %%
ar_prd = df.groupby('Crop_Year')['Area'].sum().sort_values(ascending = False)
print(ar_prd)
# %%
low = df.groupby('State_Name')['Production'].sum().sort_values(ascending=True)
print(low)
# %%
yr_12 = df[df['Crop_Year']==2012]
crop = yr_12.groupby("Crop")["Production"].sum().sort_values(ascending = False)
print(crop)
# %%
arr = df['Area'].std()
print(arr)
# %%
andhr = df[df['State_Name']=='Andhra Pradesh']
andhr_prd = andhr.groupby('Crop')['Production'].sum().sort_values(ascending=False)
print(andhr_prd)
# %%
ssn = df.groupby('Season')['Production'].sum().sort_values(ascending=False)
print(ssn)
# %%
state = df.groupby('State_Name')['Production'].sum().sort_values(ascending=True)
print(state)
# %%
arr_mean = df['Area'].aggregate(np.mean)
print(arr_mean)
# %%
corl = df['Area'].corr(df['Production'])
print(corl)
# %%
crp = df.groupby('Crop')['Production'].sum().sort_values(ascending=False)
print(crp)
# %%
