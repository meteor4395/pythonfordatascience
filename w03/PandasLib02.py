import pandas as pd
import os
import numpy as np
os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")
cars_data = pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????'])
# Data Types
# Numeric and String Data Types
# Numeric Data Types integer and floats
# String Data Types string and unicode
# Pandas Data Types are different from Python Data Types
# int64, float64, object, bool, datetime64, timedelta[ns]
# 64 is the number of bits allocated to store the data

# Charater Types
# Difference between categorical and object data types
# Categorical data types are used to store data that has a fixed number of unique values
# Object data types are used to store data that has a variable number of unique values
# Special characters in object data types are stored as strings

# Checking Data Types of each column
# Syntax: DataFrame.dtypes
print("Data Types of each column:\n", cars_data.dtypes)

# Count of Data Types
# Syntax: DataFrame.get_dtypes_counts()
# Syntax: DataFrame.dtypes.value_counts()
print("Count of Data Types:\n", cars_data.dtypes.value_counts())

# Selecting Data based on Data Types
# Syntax: DataFrame.select_dtypes(include=None, exclude=None)
print("Selecting Data based on Data Types:\n", cars_data.select_dtypes(include='int64'))

# Summary of Dataframe
# Syntax: DataFrame.info()
print("Summary of DataFrame:\n", cars_data.info())

# Unique elements in a column
# Syntax: numpy.unique(array)
print("Unique elements in a column:\n", np.unique(cars_data['Price']))
# Unique elements in a column
# Syntax: pandas.Series.unique()
print("Unique elements in a column:\n", cars_data['HP'].unique())
print("Unique elements in a column:\n", cars_data['Doors'].unique())
