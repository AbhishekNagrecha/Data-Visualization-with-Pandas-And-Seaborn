#!/usr/bin/env python
# coding: utf-8

# # Let's Load the Automobile Price data set first
# #To do so I'll import the essential libraries
# 
# import pandas as pd
# import numpy as np
# import seaborn as sns
# from math import log, sqrt, sin
# import matplotlib.pyplot as plt
# %matplotlib inline

# In[6]:


def read_auto_data(fileName = "C:/Users/Abhishek Nagrecha/Desktop/Data_visualization/Automobile price data.csv"):
    'Function to load the auto price data set from a .csv file' 


    ## Read the .csv file with the pandas read_csv method
    auto_prices = pd.read_csv(fileName)
    
    ## Remove rows with missing values, accounting for mising values coded as '?'
    cols = ['price', 'bore', 'stroke', 
          'horsepower', 'peak-rpm']
    for column in cols:
        auto_prices.loc[auto_prices[column] == '?', column] = np.nan
    auto_prices.dropna(axis = 0, inplace = True)

    ## Convert some columns to numeric values
    for column in cols:
        auto_prices[column] = pd.to_numeric(auto_prices[column])
#    auto_prices[cols] = auto_prices[cols].as_type(int64)
        
    return auto_prices
auto_prices = read_auto_data()


# In[7]:


auto_prices.head(8)


# In[8]:


auto_prices.describe()


# # We will be Visualizing the above data using
# #Scatter plot
# #Line plots
# #Bar plots
# #Histograms
# #Box plots
# #Kernel Density Estimation Plots
# #Violin plots

# In[9]:


#Scatter Plots

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.plot(auto_prices['city-mpg'], auto_prices['price'], 'ro')


# In[10]:


#Using Pandas for the same plotting
auto_prices.plot(kind = 'scatter', x = 'city-mpg', y = 'price')


# In[13]:


#create and exectue code to plot auto price vs length.
auto_prices.plot(kind = 'scatter', x = 'length', y = 'price')

#This shows us an interesting thing, as longer is the car lrngth the more expensive is its price!!


# In[14]:


#create and exectue code to plot auto price vs bore.
auto_prices.plot(kind = 'scatter', x = 'bore', y = 'price')


# In[15]:


#we can control many plot attributes once we have specified the axes.
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(6, 6)) # define plot area
ax = fig.gca() # define axis                   
auto_prices.plot(kind = 'scatter', x = 'city-mpg', y = 'price', ax = ax)
ax.set_title('Scatter plot of price vs MPG') # Give the plot a main title
ax.set_xlabel('City MPG') # Set text for the x axis
ax.set_ylabel('Auto Price')# Set text for y axis

#This shows us that higher is the price of car lower is its average.


# In[16]:


#This shows us that Car's horsepower is directly proportional to its price barring few outliers.
fig = plt.figure(figsize=(8, 6)) # define plot area
ax = fig.gca() # define axis                   
auto_prices.plot(kind = 'scatter', x = 'horsepower', y = 'price', ax = ax)
ax.set_title('Scatter plot of price vs horsepower') # Give the plot a main title
ax.set_xlabel('horsepower') # Set text for the x axis
ax.set_ylabel('Auto Price')# Set text for y axis


# In[20]:


#Line plots are similar to the scatter plots

#First, we will create a dataframe, with a simple relationship between x and y.

import pandas as pd
x = list(range(100))
y = [z * z  for z in range(100)]
df = pd.DataFrame({'x':x, 'y':y})

fig = plt.figure(figsize=(8, 8)) # define plot area
ax = fig.gca() # define axis                   
df.plot(x = 'x', y = 'y', ax = ax) ## line is the default plot type
ax.set_title('Line plot of x^2 vs. x') # Give the plot a main title
ax.set_xlabel('x') # Set text for the x axis
ax.set_ylabel('x^2')# Set text for y axis


# In[21]:


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# In[22]:


#Here I use some psedo data to show the power of line plots
Data = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
        'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
       }
  
df = pd.DataFrame(Data,columns=['Year','Unemployment_Rate'])
  
plt.plot(df['Year'], df['Unemployment_Rate'], color='red', marker='o')
plt.title('Unemployment Rate Vs Year', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Unemployment Rate', fontsize=14)
plt.grid(True)
plt.show()

