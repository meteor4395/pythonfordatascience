import pandas as pd
import os
import numpy as np
os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")
# Missing Values Present in the Data
cars_data1 = pd.read_csv('Toyota.csv',index_col=0)
print(cars_data1.info())
# Missing Values Without Na_Values
cars_data = pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????'])
print(cars_data1.info())


#Converting Variable Data Types
# Syntax: DataFrame.astype(dtype)
# Syntax: DataFrame.convert_dtypes()
cars_data['MetColor'] = cars_data['MetColor'].astype('object')
print(cars_data['MetColor'].dtypes)

cars_data['Automatic'] = cars_data['Automatic'].astype('object')
print(cars_data['Automatic'].dtypes)

# Category vs Object Data Types
# nbytes: Returns the memory usage of the DataFrame in bytes
# category use less memory
print(cars_data['FuelType'].nbytes)
print(cars_data['FuelType'].astype('category').nbytes)

# Cleaning column data 
# Syntax: DataFrame.replace(to_replace=None, value=None, inplace=False)
# to_replace is the value to be replaced
# value is the value to replace with
# inplace is a boolean value which makes the changes in the original DataFrame if True

cars_data['Doors'].replace({'three': 3, 'four': 4, 'five': 5}, inplace=True)
# add values as duplicate string must be converted
cars_data['Doors'] = cars_data['Doors'].astype('int64')
print("Unique elements in a column:\n", cars_data['Doors'].unique())


# Detecting Missing Values
# Syntax: DataFrame.isnull.sum()
print("Missing Values in the DataFrame:\n", cars_data.isnull().sum())
# Save the cleaned DataFrame to a new CSV file
cars_data.to_csv('ToyotaCleaned.csv')