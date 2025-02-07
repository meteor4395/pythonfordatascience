# Data Visuliaztion
# types of plots are: line, bar, scatter, bubble, histogram, box, density, violin, pair, heat, joint, rug, kde, hexbin, contour, and 3D plots
# Why? to understand the data, to see the relationship between variables, to see the distribution of data, to see the trend of data, to see the outliers, to see the correlation between variables, to see the pattern of data, to see the comparison between variables, to see the frequency of data, to see the density of data, to see the shape of data, to see the structure
# How? by using the matplotlib, seaborn, ggplot, plotly and pandas libraries


# Matplotlib: 2d plotting library

# Scatter Plot: set of points in a 2D plane for two variables on x and y axis convey correlation between variables

import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")


cars_data = pd.read_csv('Toyota.csv', index_col=0, na_values=["??", "????"])
cars_data.dropna(axis=0, inplace=True)

plt.scatter(cars_data['Age'],cars_data['Price'],c='blue')
plt.title('Scatter plot of Price vs Age')
plt.xlabel('Age(months)')
plt.ylabel('Price(Euros)')
plt.show()


# Histogram: frequency distribution of a variable using bars height depicts the frequency of data grouped into intervals
# Syntax: plt.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, *, data=None, **kwargs)

plt.hist(cars_data['KM'], color='green', edgecolor='white', bins=5)
plt.title('Histogram of KM')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.show()

# Bar Plot: categorical data using bars height depicts the frequency of data grouped into categories
# When to use? to compare the frequency of data, to compare the distribution of data, to compare the relationship between variables, to compare the trend of data, to compare the outliers, to compare the correlation between variables, to compare the pattern of data, to compare the shape of data, to compare the structure
# Syntax: plt.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)

counts = [979,120,12]
fueltype = ('Petrol', 'Diesel', 'CNG')
index = np.arange(len(fueltype))
plt.bar(index, counts, color=['red', 'blue', 'cyan'])
plt.title('Bar plot of fuel type')
plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.show()