"""
You survey households in your area to find the average rent they are paying. Find the
standard deviation from the following data:
$1550,$1700,$900,$850,$1000,$950.
"""

def find_mean(arr):
 return sum(arr)/len(arr)

def find_variance(arr):
 variance = 0.0
 from math import sqrt
 
 mean = find_mean(arr)
 variance = sum((x - mean)**2 for x in arr) / (len(arr)-1)
 return variance

def find_std_dev(arr):
 return find_variance(arr)**0.5

arr = [1550,1700,900,850,1000,950]

print("Calculation using custom method")
print ("Mean " + str(find_mean(arr)))
print ("variance " + str(find_variance(arr)))
print("std_dev " + str(find_std_dev(arr)))

print("Calculation using statistics library")
import statistics as stat
print(str("Mean " + str(stat.mean(arr))))
print(str("Variance " + str(stat.variance(arr))))
print(str("std_dev " + str(stat.stdev(arr))))

