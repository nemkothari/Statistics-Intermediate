## 1. Individual Values ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')

houses['SalePrice'].plot.kde(xlim = [min(houses['SalePrice']) , max(houses['SalePrice'])])

plt.axvline(houses['SalePrice'].mean(), color='Black', label='Mean')
plt.axvline(( houses['SalePrice'].std(ddof = 0) + houses['SalePrice'].mean()), color='Red', label='Standard deviation')
plt.axvline(220000, color='Orange', label='220000')

plt.legend()
very_expensive = False

## 2. Number of Standard Deviations ##

st_devs_away= (220000 - houses['SalePrice'].mean()) / houses['SalePrice'].std(ddof=0)

## 3. Z-scores ##

import numpy as np
min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

min_z = z_score(min_val ,houses['SalePrice'])
mean_z = z_score(mean_val ,houses['SalePrice'])

max_z = z_score(max_val,houses['SalePrice'])

## 4. Locating Values in Different Distributions ##

def z_score(value, array, bessel = 0):
    mean = sum(array) / len(array)
    
    from numpy import std
    st_dev = std(array, ddof = bessel)
    
    distance = value - mean
    z = distance / st_dev
    
    return z

ng =['NAmes','CollgCr','OldTown','Edwards','Somerst']
result ={}
for i in ng :
    hou = houses[houses['Neighborhood'] == i ]
    result[i] = abs(z_score(200000,hou['SalePrice']))

print(result)

best_investment = 'College Creek'





## 5. Transforming Distributions ##

mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)
houses['z_prices'] = houses['SalePrice'].apply(
    lambda x: ((x - mean) / st_dev)
    )

z_mean_price = houses['z_prices'].mean()
z_stdev_price = houses['z_prices'].std(ddof =0)

z_mena =  houses['Lot Area'].mean()
st_deva = houses['Lot Area'].std(ddof = 0)
z_men_a = houses['Lot Area'].apply( lambda x :  ((x - z_mena) / st_deva) )
z_mean_area  = z_men_a.mean()

z_stdev_area = z_men_a.std(ddof =0)


    

## 6. The Standard Distribution ##

from numpy import std, mean
population = [0,8,0,8]

stdev_z = ((mean(population) + std(population)) - mean(population)) / std(population)

mean_z = ( mean(population) - mean(population) ) / std(population)

## 7. Standardizing Samples ##

from numpy import std, mean
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = []
for value in sample:
    z = (value - x_bar) / s
    standardized_sample.append(z)
    
stdev_sample = std(standardized_sample , ddof=1)

## 8. Using Standardization for Comparisons ##

mean_index1 = houses['index_1'].mean()
stdev_index1 = houses['index_1'].std(ddof = 0)
houses['z_1'] = houses['index_1'].apply(lambda x: 
                                      (x - mean_index1) / stdev_index1
                                     )

mean_index2 = houses['index_2'].mean()
stdev_index2 = houses['index_2'].std(ddof = 0)
houses['z_2'] = houses['index_2'].apply(lambda x: 
                                      (x - mean_index2) / stdev_index2
                                     )

print(houses[['z_1', 'z_2']].head(2))
better = 'first'

## 9. Converting Back from Z-scores ##

mean = 50
st_dev = 10
houses['transformed'] = houses['z_merged'].apply(
                                lambda z: (z * st_dev + mean)
                                )
mean_transformed = houses['transformed'].mean()
stdev_transformed = houses['transformed'].std(ddof = 0)