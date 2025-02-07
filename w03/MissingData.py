#%%
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import seaborn as sns
os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")
cars_data = pd.read_csv('Toyota.csv', index_col=0, na_values=["??", "????"])
cars_data2 = cars_data.copy()
cars_data3 = cars_data.copy()

#%%
#NaN = not a number
# Check for missing values by isnull() and isna() functions
# returns dataframe of True for missing values and False for non-missing values
# Syntax: df.isnull() or df.isna()

cars_data2.isna().sum()

# %%
# Identify missing values in the dataset
missing = cars_data2[cars_data2.isnull().any(axis=1)]

# %%
# Filling of missing values

# 1. Fill missing values by mean/median of numerical variables
# 2. Fill missing values by maximum count of categorical variables

# Impute missing values in numerical variables by mean or median by looking at desciption of data df.describe()
cars_data2.describe()
cars_data2['Age'].mean()

# %%
# To fill NA/NaN values using specified value
# Syntax: DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
cars_data2['Age'].fillna(cars_data2['Age'].mean(), inplace=True)

# %%
# for KM mean value deviates from median value
# So impute using median
cars_data2['KM'].median()
cars_data2['KM'].fillna(cars_data2['KM'].median(), inplace=True)
# %%
# Impute missing values of HP
# mean value and median are almost same
cars_data2['HP'].mean()
cars_data2['HP'].fillna(cars_data2['HP'].mean(), inplace=True)

# %%
# Impute missing values of categorical variable "FuelType"
# Find the maximum count of FuelType
cars_data2['FuelType'].value_counts().index[0]
# fill missing value by maximum count of FuelType
cars_data2['FuelType'].fillna(cars_data2['FuelType'].value_counts().index[0], inplace=True)
# %%
# Imput missing values of MetColor
# using mode value
cars_data2['MetColor'].mode()
cars_data2['MetColor'].fillna(cars_data2['MetColor'].mode()[0], inplace=True)

# %%
# Check for missing values after imputation
cars_data2.isna().sum()

# %%
# To fill missing values in both numerical and categorical variables at one stretch
cars_data3 = cars_data3.apply(lambda x: x.fillna(x.mean()) 
                              if x.dtype == 'float' 
                              else x.fillna(x.value_counts().index[0]))
# %%
cars_data3.isna().sum()
# %%
