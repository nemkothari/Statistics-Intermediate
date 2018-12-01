## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')


def range(a):
    return ( max(a) - min(a) )



k = houses['Yr Sold'].value_counts().reset_index()
range_by_year ={}
for i in k['index']:
    hou =houses[houses['Yr Sold']==i]
    range_by_year[i] = range(hou['SalePrice'])
    
one = False
two = True
    


## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]

sum1 =0 
for i in C :
    sum1 = sum1 + i
    
mean =  sum1/len(C)

dist =0
for i in C :
    dist = dist + (i-mean)
    
avg_distance = dist/len(C)

print(avg_distance)
    
    

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]
sum1 =0 
for i in C :
    sum1 = sum1 + i
    
mean =  sum1/len(C)

dist =0
for i in C :
    dist = dist + abs(i-mean)
    
mad = dist/len(C)

print(mad)
    

## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]

def variancecal(a):
    sum1 =0 
    for i in a :
        sum1 = sum1 + i
    mean =  sum1/len(a)
    squared_distance =[]
    dist =0
    for i in a :
        squared_distance.append(abs(i-mean)**2)
        
    return squared_distance

K= variancecal(C)

variance_C =  sum(K)/len(K)
    

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]

def StdDeviationcal(a):
    sum1 =0 
    for i in a :
        sum1 = sum1 + i
    mean =  sum1/len(a)
    squared_distance =[]
    dist =0
    for i in a :
        squared_distance.append((i-mean)**2)
    
    vari = sum(squared_distance)/len(squared_distance)
    return sqrt(vari)

standard_deviation_C = StdDeviationcal(C)


    

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

k = houses['Yr Sold'].value_counts().reset_index()
range_by_year ={}
for i in k['index']:
    hou = houses[houses['Yr Sold'] ==i]
    range_by_year[i] = standard_deviation(hou['SalePrice'])
 

print(range_by_year)

greatest_variability = max(range_by_year, key = range_by_year.get) 
lowest_variability =  min(range_by_year , key =range_by_year.get)

## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

sample1.plot.hist()
plt.show()
sample2.plot.hist()
plt.show()

bigger_spread = 'sample 2'
st_dev1 =standard_deviation(sample1)
st_dev2 = standard_deviation(sample2)

## 8. The Sample Standard Deviation ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt

list_std=[]
for i in range(5000):
    sam = houses['SalePrice'].sample(10, random_state =i)
    list_std.append(standard_deviation(sam))
    
plt.hist(list_std)
plt.axvline(standard_deviation(houses['SalePrice']))


plt.show()

    

## 9. Bessel's Correction ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances)-1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)
    
plt.hist(st_devs)
plt.axvline(standard_deviation(houses['SalePrice']))

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var

pandas_stdev = sample['SalePrice'].std(ddof = 1) # default ddof = 1
numpy_stdev = std(sample['SalePrice'], ddof = 1) # default ddof = 0
equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample['SalePrice'].var(ddof = 1) # default ddof = 1
numpy_var = var(sample['SalePrice'], ddof = 1) #default ddof = 0
equal_vars = pandas_var == numpy_var

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

from numpy import var, std

pop_var = var(population, ddof = 0)
pop_std = std(population, ddof = 0)

st_devs = []
variances = []

for sample in samples:
    st_devs.append(std(sample, ddof = 1))
    variances.append(var(sample, ddof = 1))
    
mean_std = sum(st_devs) / len(st_devs)
mean_var = sum(variances) / len(variances)

equal_stdev = pop_std == mean_std
equal_var = pop_var == mean_var