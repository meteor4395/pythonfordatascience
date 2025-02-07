#%%
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import seaborn as sns
os.chdir("C:\\uhh\\nptel\\python for datascience\\w03")
cars_data = pd.read_csv('Toyota.csv', index_col=0, na_values=["??", "????"])
cars_data.dropna(axis=0, inplace= True)
sns.set_theme(style='darkgrid')
#%%
# Seaborne: statistical data visualization provide high level drawing


# Scatter Plot: set of points in a 2D plane for two variables on x and y axis convey correlation between variables
# Syntax: sns.regplot(x, y, data=None, x_estimator=None, x_bins=None, x_ci='ci', scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, seed=None, order=1, logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, truncate=False, dropna=True, x_jitter=None, y_jitter=None, label=None, color=None, marker='o', scatter_kws=None, line_kws=None, ax=None)

# by default fit_reg=True, scatter=True, ci=95, n_boot=1000, order=1, logistic=False, lowess=False, robust=False, logx=False, truncate=False, dropna=True


sns.regplot(x=cars_data['Age'],y= cars_data['Price'])
sns.regplot(x=cars_data['Age'],y= cars_data['Price'],marker='*', fit_reg=False) # without regression line

# markers change the shape of points, color changes the color of points, scatter_kws changes the size of points

#%%

# Scatter plot Of Price vs Age by FuelType
# Hue parameter is used to color the points based on a variable
# Syntax: sns.lmplot(x, y, data, hue=None, col=None, row=None, palette=None, col_wrap=None, height=5, aspect=1, markers='o', sharex=True, sharey=True, hue_order=None, col_order=None, row_order=None, legend=True, legend_out=True, x_estimator=None, x_bins=None, x_ci='ci', scatter=True, fit_reg=True, ci=95, n_boot=1000, units=None, seed=None, order=1, logistic=False, lowess=False, robust=False, logx=False, x_partial=None, y_partial=None, truncate=False, x_jitter=None, y_jitter=None, scatter_kws=None, line_kws=None, size=None)

sns.lmplot(x='Age',y='Price',data=cars_data, fit_reg=False, hue='FuelType', legend=True, palette='Set1')

#%%

# Histogram with default kernel density estimate
# Syntax: sns.distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, axlabel=None, label=None, ax=None)

sns.displot(cars_data['Age'], kde=True) # kde gives estimate lines

sns.displot(cars_data['Age'],kde=False,bins= 5)

#%%

# Bar Plot
# Syntax: sns.countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, dodge=True, ax=None, **kwargs)

sns.countplot(x='FuelType',data=cars_data)

# Grouped Bar plot
# Grouped bar plot of FuelType and Automatic
sns.countplot(x='FuelType',data=cars_data, hue='Automatic')

#%%
# Box and Whisker Plot for numerical variables
# interpret five number summary: minimum, first quartile, median, third quartile, maximum
# Syntax: sns.boxplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, orient=None, color=None, palette=None, saturation=0.75, width=0.8, dodge=True, fliersize=5, linewidth=None, whis=1.5, notch=False, ax=None, **kwargs)

sns.boxplot(y=cars_data['Price'])

# Horizontal line called whiskers, vertical line called box, horizontal line in box called median
# minimum and maximum are the end points of whiskers
#first quartile is the bottom of the box, third quartile is the top of the box, second quartile is the line in the box
# outliers are the points outside the whiskers 1.5 times the interquartile range or 1.5 less than first quartile
# %%
# Box and Whisker Plot for numerical vs categorical variables
sns.boxplot(x=cars_data['FuelType'], y=cars_data['Price'])

# %%
# Grouped Box and Whisker Plot
sns.boxplot(x=cars_data['FuelType'], y=cars_data['Price'], hue='Automatic',data=cars_data)

# %%
# Box-Whisker plot and Histogram
# split the plot into two parts
# Syntax: plt.subplot(nrows, ncols, index, **kwargs)

f, (ax_box, ax_hist) = plt.subplots(2, gridspec_kw={"height_ratios": (.20, .80)}) #height ratio of box and histogram
sns.boxplot(x=cars_data['Price'], ax=ax_box)
sns.histplot(cars_data['Price'], ax=ax_hist, kde=False)

# %%
# Pairwise plot used to plot pairwise relationships in a dataset
# Creates scatter plot for joint relationships and histogram for univariate distributions
# Syntax: sns.pairplot(data, hue=None, hue_order=None, palette=None, vars=None, x_vars=None, y_vars=None, kind='scatter', diag_kind='auto', markers=None, height=2.5, aspect=1, corner=False, dropna=True, plot_kws=None, diag_kws=None, grid_kws=None, size=None)

sns.pairplot(cars_data, kind='scatter',hue='FuelType')
plt.show()


# %%
