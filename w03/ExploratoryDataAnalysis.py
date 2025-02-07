import os
import numpy as np
import pandas as pd
os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")
cars_data = pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????'])
cars_data2 = cars_data.copy()

# Frequency Table
# A frequency table is a table that displays the frequency of various outcomes in a sample.
# Each entry in the table contains the count or frequency of the occurrences of values within a particular group or interval.
# Frequency tables are useful for summarizing categorical data and for identifying patterns or trends.

# Example: Creating a frequency table for the 'FuelType' column in the cars_data DataFrame
# Syntax: pandas.crosstab(index, columns, values=None, rownames=None, colnames=None, aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False)
# index: array-like, Series, or list of arrays/Series
# columns: array-like, Series, or list of arrays/Series
# values: array-like, optional
# rownames: sequence, default None
# colnames: sequence, default None
# aggfunc: function, optional
# margins: bool, default False
# margins_name: str, default 'All'
# dropna: bool, default True
# normalize: bool, {'all', 'index', 'columns'}, or {0,1}, default False
# Returns: DataFrame

print(pd.crosstab(index=cars_data2['FuelType'],columns='count',dropna=True))

# Two Way Table
# A two-way table is a table that displays the frequency of two categorical variables.
# The rows represent one variable, and the columns represent the other variable.
# The intersection of a row and a column represents the frequency of a particular combination of values.

print(pd.crosstab(index=cars_data2['Automatic'],columns=cars_data2['FuelType'],dropna=True))

# Two Way Table joint probability
# Joint probability is the probability of two events occurring at the same time.
print(pd.crosstab(index = cars_data2['Automatic'],
            columns= cars_data2['FuelType'],
            normalize=True,
            dropna=True))

# Two Way Table marginal probability
# Marginal probability is the probability of a single event occurring.
print(pd.crosstab(index = cars_data2['Automatic'],
                  columns= cars_data2['FuelType'],
                  margins= True,
                  dropna= True,
                  normalize= True))

# Two Way Table conditional probability
# Conditional probability is the probability of an event occurring given that another event has already occurred.
print(pd.crosstab(index = cars_data2['Automatic'],
                  columns= cars_data2['FuelType'],
                  margins= True,
                  dropna= True,
                  normalize= 'index')) # row sum is 1
print(pd.crosstab(index = cars_data2['Automatic'],
                  columns= cars_data2['FuelType'],
                  margins= True,
                  dropna= True,
                  normalize= 'columns')) # column sum is 1

# Correlation
# Correlation is a statistical measure that describes the relationship between two variables.
# It indicates the strength and direction of a linear relationship between two variables.
# The correlation coefficient ranges from -1 to 1.
# SCATTER PLOT is used to visualize the correlation between two variables.
# Syntax: DataFrame.corr(method='pearson', min_periods=1)
# method: {‘pearson’, ‘kendall’, ‘spearman’}
numeric_data = cars_data2.select_dtypes(exclude='object')
print(numeric_data.shape)

corr_matrix = numeric_data.corr(method='pearson')
print(corr_matrix)
