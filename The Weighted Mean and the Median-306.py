## 1. Introduction ##

mean_new = houses_per_year['Mean Price'].mean()
mean_original = houses['SalePrice'].mean()

difference = mean_original - mean_new

## 2. Different Weights ##

houses_per_year['sum_per_year'] = houses_per_year['Mean Price'] * houses_per_year['Houses Sold']
all_sums_together = houses_per_year['sum_per_year'].sum()
total_n_houses = houses_per_year['Houses Sold'].sum()
weighted_mean = all_sums_together / total_n_houses

mean_original = houses['SalePrice'].mean()

difference = round(mean_original, 10) - round(weighted_mean, 10)

## 3. The Weighted Mean ##

import numpy as np
def mean_w(a,b):
    sumw =0  
    for x,y in zip(a,b):
        sumw = sumw + x*y
        
    s =sumw
    c= sum(b)
    f = s/c
    return f


weighted_mean_function = mean_w(houses_per_year['Mean Price'].tolist(),houses_per_year ['Houses Sold'].tolist())

weighted_mean_numpy = np.average(houses_per_year['Mean Price'] , weights=houses_per_year ['Houses Sold'])

equal = weighted_mean_function == weighted_mean_numpy


## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1 = 23
median2 = 55
median3 = 32
'20 years or lower,', 22, 23, 23, 24, 42, 35

## 5. Distributions with Even Number of Values ##

# Sort the values
rooms = houses['TotRms AbvGrd'].copy()
rooms = rooms.replace({'10 or more': 10})
rooms = rooms.astype(int)
rooms_sorted = rooms.sort_values()

# Find the median
middle_indices = [int((len(rooms_sorted) / 2)),
                  int((len(rooms_sorted) / 2 + 1))
                 ]
middle_values = rooms_sorted.iloc[middle_indices] # make sure you don't use loc[]
median = middle_values.mean()

## 6. The Median as a Resistant Statistic ##

houses['Lot Area'].plot.box()
plt.show()

houses['SalePrice'].plot.box()
plt.show()

lotarea_difference = houses['Lot Area'].mean() - houses['Lot Area'].median()

saleprice_difference = houses['SalePrice'].mean() - houses['SalePrice'].median()


## 7. The Median for Ordinal Scales ##

mean = houses['Overall Cond'].mean()
median =  houses['Overall Cond'].median()

houses['Overall Cond'].plot.hist()
more_representative= 'mean'
