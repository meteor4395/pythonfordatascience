#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# from sklearn.metrics import accuracy_score, confusion_matrix, mean_square_error
# from sklearn.linear_model import LinearRegression

os.chdir("C:\\uhh\\nptel\\python for datascience\\examprep")


# %%
df = pd.read_csv("apy.csv",)
df.info()
print(df.columns)
print(df['Season'].unique())

# Remove extra spaces from the 'Name' column
df['Season'] = df['Season'].str.strip()
print(df['Season'].unique())


# %%

sp=df.groupby("Season")['Production'].sum()
print(sp)
# %%
season = df.groupby("Season")
kharif = season.get_group('Kharif')
print(np.unique(kharif['Crop']))
# Search for a specific crop in Kharif season
crop_name = 'Apple'  # Replace with the crop you want to search for
specific_crop = kharif[kharif['Crop'] == crop_name]
print(specific_crop)
# %%
shcp = df.groupby('District_Name')['Production'].sum().sort_values(ascending=False).index[0]
print(shcp)
# highest production by district

# %%
tamil = df[df['State_Name']== 'Tamil Nadu']
year_prd = tamil.groupby('Crop_Year')['Production'].sum().sort_values(ascending=False)
print(year_prd)
# %%
state_prd = df.groupby('State_Name')["Production"].sum().sort_values(ascending=False)
print(state_prd)
# %%
sns.scatterplot(x='Area',y='Production',data=df)
# %%
avg = (df['Production'].aggregate(np.mean))
print(avg)
# %%
# Format describe() to show whole integer values
pd.options.display.float_format = '{:.0f}'.format
print(df['Production'].describe())
# Calculate and print the standard deviation of the 'Production' column
std_dev = df['Production'].std()
print(std_dev)
# %%
y_15 = df[df['Crop_Year']==2015]
print(y_15['State_Name'].unique())
# %%
y_97 = df[df['Crop_Year']==1997]
crop_top =y_97.groupby('Crop')['Production'].sum().sort_values(ascending=False)
print(crop_top)
# %%
sns.regplot(x='Crop_Year',y='Area',data=df)
plt.show()
sns.regplot(x='Crop_Year',y='Production',data=df)
plt.show()
# Check linear correlation between Crop_Year vs Area and Production
correlation_area = df[['Crop_Year', 'Area']].corr().iloc[0, 1]
correlation_production = df[['Crop_Year', 'Production']].corr().iloc[0, 1]

print(f"Correlation between Crop_Year and Area: {correlation_area}")
print(f"Correlation between Crop_Year and Production: {correlation_production}")

# Output boolean values
is_correlated_area = abs(correlation_area) > 0.5
is_correlated_production = abs(correlation_production) > 0.5

print(f"Is Crop_Year and Area correlated? {is_correlated_area}")
print(f"Is Crop_Year and Production correlated? {is_correlated_production}")

# %%
yr_prd = df.groupby('Crop_Year')['Production'].sum().sort_values(ascending=False)
print(yr_prd)
# %%
tamiln = df[df['State_Name']== 'Tamil Nadu']
year_pro = tamiln.groupby('Crop')['Production'].sum().sort_values(ascending=False)
print(year_pro)

# %%
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error

data= pd.read_csv("apy.csv")
data.info()
data.columns
data.dropna(inplace=True,axis=0)
data= data.drop(['State_Name', 'District_Name', 'Crop_Year', 'Season', 'Crop'],axis=1)
# %%
x=data['Area']
y=data['Production']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=11)
# %%
model = LinearRegression()

model.fit(x_train.values.reshape(-1,1),y_train)
prediction=model.predict(x_test.values.reshape(-1,1))
r2 = r2_score(y_test,prediction)
rmse= root_mean_squared_error(y_test,prediction)
print(r2,rmse)
# %%
