## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]

mean = (0+2+3+3+3+4+13)/len(distribution)
center=False
equal_distances =True

## 3. The Mean as a Balance Point ##

from numpy.random import randint, seed
equal_distances = 0

for i in range(5000):
    seed(i)
    print(seed(i))
    distribution = randint(0,1000,10)
    mean = sum(distribution) / len(distribution)
    
    above = []
    below = []
    for value in distribution:
        if value == mean:
            continue # continue with the next iteration because the distance is 0
        if value < mean:
            below.append(mean - value)
        if value > mean:
            above.append(value - mean)
    
    sum_above = round(sum(above),1)
    sum_below = round(sum(below),1)
    if (sum_above == sum_below):
        equal_distances += 1

## 4. Defining the Mean Algebraically ##

one=False
two =False
three =False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def calmean(a):
    count =0
    suma=0
    for i in a :
        suma = suma + i
        count = count + 1
        
    return (suma/count)



mean_1 = calmean(distribution_1)
mean_2 = calmean(distribution_2)
mean_3 = calmean(distribution_3)
        

## 6. Introducing the Data ##

import pandas as pd
df= pd.read_csv("AmesHousing_1.txt",sep='\t')
df.head()
df.shape
one=True
two=False
three = True


## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

pandas_mean=houses['SalePrice'].mean()
function_mean=mean(houses['SalePrice'])

means_are_equal = pandas_mean ==function_mean


## 8. Estimating the Population Mean ##

parameter = houses['SalePrice'].mean()
sample_size = 5

sample_sizes = []
sampling_errors = []

for i in range(101):
    sample = houses['SalePrice'].sample(sample_size , random_state = i)
    statistic = sample.mean()
    sampling_error = parameter - statistic
    sampling_errors.append(sampling_error)
    sample_sizes.append(sample_size)
    sample_size += 29
    
import matplotlib.pyplot as plt
plt.scatter(sample_sizes, sampling_errors)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel('Sample size')
plt.ylabel('Sampling error')

## 9. Estimates from Low-Sized Samples ##

means = []
for i in range(10000):
    sample = houses['SalePrice'].sample(100 , random_state=i)
    means.append(sample.mean())

plt.hist(means)
plt.axvline(houses['SalePrice'].mean())
plt.xlabel("Sample mean")
plt.ylabel("Frequency")
plt.xlim(0,500000)

## 11. The Sample Mean as an Unbiased Estimator ##

population = [3, 7, 2]

population = [3, 7, 2]
samples = [[3, 7], [3, 2],
           [7, 2], [7, 3],
           [2, 3], [2, 7]
          ]

sample_means = []
for sample in samples:
    sample_means.append(sum(sample) / len(sample))
    
population_mean = sum(population) / len(population)
mean_of_sample_means = sum(sample_means) / len(sample_means)

unbiased = (population_mean == mean_of_sample_means)