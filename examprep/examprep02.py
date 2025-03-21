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
aut = df[df['Season']=='Autumn']
crop = aut['Crop'].unique()
print(crop)
# %%
ut= df[df['State_Name']=='Uttar Pradesh']
ut_prd = ut.groupby('Crop_Year')['Production'].sum().sort_values(ascending=False)
print(ut_prd)
# %%
df.groupby('Crop_Year')['Area'].sum().sort_values(ascending = False)
# %%
df.groupby('State_Name')['Production'].sum().sort_values(ascending = True)
# %%
yr_15 = df[df['Crop_Year']==2015]
crop = yr_15.groupby("Crop")["Production"].sum().sort_values(ascending = False)
print(crop)
# %%
std = df['Area'].std()
print(std)
# %%
mp= df[df['State_Name']=='Madhya Pradesh']
mp_prd = mp.groupby('Crop')['Production'].sum().sort_values(ascending=False)
print(mp_prd)
# %%

sesn = df.groupby('Season')['Production'].sum().sort_values(ascending=False)
print(sesn)
# %%
ar_prd = df.groupby('State_Name')['Area'].sum().sort_values(ascending=False)
print(ar_prd)
# %%
ar_mean = df['Area'].mean()
print(ar_mean)
# %%
corelation = df['Area'].corr(df['Production'])
print(corelation)
# %%
crp_prd = df.groupby('Crop')['Production'].sum().sort_values(ascending=False)
print(crp_prd)
# %%
three_ssn = df[df['Season'].isin(['Autumn', 'Summer', 'Winter'])]
high_crp = three_ssn.groupby('Crop')['Production'].sum().sort_values(ascending=False)
print(high_crp)
# %%
from sklearn.metrics import root_mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("apy.csv")
data.dropna(inplace=True, axis=0)
data = data[['Area', 'Production']]
x = data['Area']
y = data['Production']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=42)
# %%
model = LinearRegression()
model.fit(x_train.values.reshape(-1,1), y_train)
y_pred = model.predict(x_test.values.reshape(-1,1))
rmse = root_mean_squared_error(y_test, y_pred)
print(rmse)
mae = mean_absolute_error(y_test, y_pred)
print(mae)
# %%
