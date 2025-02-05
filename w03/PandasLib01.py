#%%
import pandas as pd
import os
import numpy as np
# Pandas is a powerful and flexible open-source data analysis and manipulation library for Python.
# It provides data structures like Series (1-dimensional) and DataFrame (2-dimensional) that make it easy to work with structured data.
# Pandas is built on top of NumPy and integrates well with other libraries like Matplotlib and SciPy.

os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")

cars_data = pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????'])
# Shallow copy: Creates a new object, but inserts references into it to the objects found in the original.
# Deep copy: Creates a new object and recursively adds copies of nested objects found in the original.

# Difference:
# Shallow copy: Changes made to the copied object may reflect in the original object if they involve mutable elements.
# Deep copy: Changes made to the copied object do not affect the original object as all elements are copied recursively.

# Example of shallow copy
shallow_copied_data = cars_data.copy(deep=False)

# Example of deep copy
deep_copied_data = cars_data.copy(deep=True)

# Attributes of DataFrame

# Shape of the DataFrame (rows, columns)
print("Shape of the DataFrame:", cars_data.shape)

# Column names
print("Column names:", cars_data.columns)

# Data types of each column
print("Data types of each column:\n", cars_data.dtypes)

# First few rows of the DataFrame
print("First few rows of the DataFrame:\n", cars_data.head())

# Summary statistics of the DataFrame
print("Summary statistics of the DataFrame:\n", cars_data.describe())

# Index of the DataFrame
print("Index of the DataFrame:", cars_data.index)

# Size of the DataFrame (number of elements)
print("Size of the DataFrame:", cars_data.size)

# Memory usage of the DataFrame
print("Memory usage of the DataFrame:\n", cars_data.memory_usage(deep=True))

# Number of dimensions of the DataFrame
print("Number of dimensions of the DataFrame:", cars_data.ndim)
# Indexing and Selecting Data

# Selecting a single column
print("Selecting a single column:\n", cars_data['Model'])

# Selecting multiple columns
print("Selecting multiple columns:\n", cars_data[['Model', 'Price']])

# Selecting rows by label using .loc[]
print("Selecting rows by label using .loc[]:\n", cars_data.loc[1:5])

# Selecting rows by position using .iloc[]
print("Selecting rows by position using .iloc[]:\n", cars_data.iloc[1:5])

# Selecting a specific value by row and column labels using .at[]
print("Selecting a specific value by row and column labels using .at[]:\n", cars_data.at[1, 'Model'])

# Selecting a specific value by row and column positions using .iat[]
print("Selecting a specific value by row and column positions using .iat[]:\n", cars_data.iat[1, 1])

# Selecting the first few rows using .head()
print("Selecting the first few rows using .head():\n", cars_data.head(3))

# Selecting the last few rows using .tail()
print("Selecting the last few rows using .tail():\n", cars_data.tail(3))

# %%
