# Dataset form chapter 1

from collections import Counter
from typing import List
import matplotlib.pyplot as plt
import random
import string
num_friends = [100, 49, 41, 40, 25, 39, 40, 47, 16, 11, 2, 16, 31, 16, 38, 15, 12, 11, 19, 33, 11, 36, 29, 44, 23, 21, 38, 11, 7, 1, 45, 9, 20, 49, 39, 46, 39, 16, 16, 13, 14, 26, 13, 48, 39, 35, 3, 3, 39, 18, 49, 35, 1, 13, 4, 19, 35, 11, 9, 47, 8, 11, 9, 11, 39, 39, 9, 45, 15, 36, 6, 29, 17, 35, 34, 2, 7, 33, 7, 29, 18, 31, 6, 32, 1, 42, 49, 3, 28, 30, 3, 15, 37, 4, 10, 39, 35, 30, 8, 22, 2, 5, 17, 32, 25, 2, 40, 8, 45, 10, 5, 21, 19, 36, 21, 11, 2, 4, 16, 13, 11, 26, 23, 46, 43, 46, 16, 5, 38, 31, 49, 1, 7, 2, 25, 7, 35, 20, 45, 33, 29, 6, 37, 23, 34, 30, 42, 5, 5, 2, 48, 23, 15, 2, 16, 17, 19, 13, 13, 24, 37, 23, 7, 22, 48, 47, 39, 45, 22, 23, 13, 20, 47, 44, 30, 38, 26, 20, 39, 6, 47, 38, 17, 11, 31, 39, 1, 43, 32, 28, 47, 34, 17, 42, 35, 25, 38, 6, 28, 26, 4, 42, 21, 12, 41, 18, 12, 17]
friends_counts = Counter(num_friends)
xs = range(101)
ys = [friends_counts[x] for x in xs]
def plot_bar(xs: List, ys: List):
  plt.bar(xs, ys)
  plt.grid(True)
  plt.axis([0, 101, 0, 25])
  plt.title("Histogram of Friend Counts")
  plt.xlabel("# of friends")
  plt.ylabel("# of people")
  plt.show()
  plt.close()

# This chart is little bit messy so we start generating some statistics. Probably the simplest statistic is number fo data points:

num_points = len(num_friends)

largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
third_smallest_value = sorted_values[2]


# Finding mean of the data
def mean(xs: List[float]) -> float:
  return sum(xs) / len(xs)

# finding median

# The underscores indicate that these are "private" functions, as they're intended to e called by our median function but not by other people using our statistics library

def _median_odd(xs: List[float]) -> float:
  """If len(xs) is odd, the median is the middle element"""
  return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float])-> float:
  """If len(xs) is even, it's the average of the middle two elements"""
  sorted_xs = sorted(xs)
  hi_midpoint = len(xs) // 2
  return (sorted(xs)[hi_midpoint -1] + sorted_xs[hi_midpoint]) / 2

def median(v: list[float]) -> float:
  """Finds the middle most value of v"""
  return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)

assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

# now we can count the median number of friends

print(median(num_friends))

def quantile(xs: List[float], p: float) -> float:
  """Returns the p_th percentile value in x"""
  p_index = int(p * len(xs))
  return sorted(xs)[p_index]

assert quantile(num_friends, 0.10) == 4
assert quantile(num_friends, 0.25) == 11
assert quantile(num_friends, 0.75) == 38 
assert quantile(num_friends, 0.90) == 45 

# Mode : Most common values
def mode(x: List[float]) -> float:
  """Return a list, since there might be more than one mode"""
  counts = Counter(x)
  max_count = max(counts.values())
  return [x_i for x_i, count in counts.items() if count == max_count]

assert set(mode(num_friends)) == {39}

# Dispersion
# ?Dispersion refers to measures of how spread out our data is. Typically they're statistics for which values near zero signify not spread out at all and for which large values (whatever that means) signify very spread out. 

def data_range(xs : List[float]) -> float:
  return max(xs) - min(xs)

assert data_range(num_friends) == 99

# Variance
import sys
if not "/Users/cmlowerence/Documents/Personal/Coding/Tutorials/Python/Data_Science" in sys.path:
  sys.path.append("/Users/cmlowerence/Documents/Personal/Coding/Tutorials/Python/Data_Science")
from Chapter_4_Linear_Algebra import main as L_A


def de_mean(xs: List[float]) -> List[float]:
  """Translate xs by subtracting its mean (so the result has mean 0)"""
  x_bar = mean(xs)
  return [x-x_bar for x in xs]

def variance(xs: List[float]) -> float:
  """Almost the average squared deviation from the mean"""
  assert len(xs) >= 2, "Variance requires at least two elements"
  
  n = len(xs)
  deviations = de_mean(xs)
  return L_A.sum_of_squares(deviations) / (n - 1)
assert 241.15 < variance(num_friends) < 241.164

import math

def standard_deviation(xs: List[float]) -> float:
  """The standard deviation is the square root of the variance"""
  return math.sqrt(variance(xs))

assert 15.51 < standard_deviation(num_friends)  < 15.53

def interquartile_range(xs: List[float]) -> float:
  """Returns the deference between the 75%-ile and the 25%-ile"""
  return quantile(xs, 0.75) - quantile(xs, 0.25)

assert interquartile_range(num_friends) == 27


# ! Correlation
from Chapter_4_Linear_Algebra.main import dot
def covariance(xs : List[float], ys: List[float]) -> float:
  assert len(xs) == len(ys), "xs and ys must have same numbers of elements"
  return dot(de_mean(xs), de_mean(ys)) // (len(xs) - 1)


def correlation(xs : List[float], ys: List[float]) -> float:
  """Measures how much xs and ys vary in tandem about their means"""
  stdev_x = standard_deviation(xs)
  stdev_y = standard_deviation(ys)
  if stdev_x > 0 and stdev_y > 0:
    return covariance(xs, ys) / stdev_x / stdev_y
  else:
    return 0

daily_minutes = [54, 125, 31, 79, 12, 90, 74, 61, 15, 58, 132, 73, 97, 56, 54, 148, 25, 143, 86, 101, 107, 11, 114, 115, 67, 22, 119, 69, 87, 58, 44, 87, 63, 17, 129, 10, 112, 91, 115, 34, 108, 89, 145, 85, 33, 75, 88, 126, 98, 29, 48, 44, 88, 10, 100, 115, 101, 49, 121, 74, 44, 119, 121, 57, 114, 137, 101, 81, 94, 67, 28, 78, 89, 101, 18, 56, 117, 127, 115, 122, 132, 104, 10, 40, 77, 23, 115, 115, 32, 76, 70, 95, 83, 118, 92, 118, 129, 97, 143, 64, 122, 46, 97, 46, 134, 55, 69, 57, 32, 81, 29, 48, 101, 142, 21, 22, 59, 15, 88, 29, 99, 42, 136, 85, 148, 106, 63, 38, 39, 36, 119, 119, 95, 111, 73, 139, 132, 31, 96, 74, 144, 146, 79, 139, 111, 149, 136, 50, 102, 107, 63, 48, 107, 32, 131, 53, 72, 36, 64, 41, 68, 92, 17, 135, 79, 25, 144, 91, 125, 147, 45, 79, 49, 76, 69, 72, 77, 63, 25, 93, 101, 18, 144, 144, 122, 89, 94, 11, 113, 143, 138, 14, 113, 89, 102, 31, 50, 112, 12, 99, 115, 36, 77, 121, 32, 149, 11, 28]

daily_hours = [round(min/60,2) for min in daily_minutes]

def Correlation_with_outlier():
  plt.scatter(num_friends, daily_minutes)
  plt.axis([0, 100, 0, 100])
  plt.xlabel("# of friends")
  plt.ylabel("Minutes per day")
  plt.title("Correlation with an outlier")
  plt.show()


outlier = num_friends.index(100)
num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

daily_hours_good = [dm/60 for dm in daily_minutes_good]

def correlation_after_removing_outlier():
  plt.scatter(num_friends_good, daily_minutes_good)
  plt.ylabel("Minutes per day")
  plt.xlabel("Correlation after removing the outlier")
  plt.title("Correlation After Removing Outlier")
  plt.show()
# correlation_after_removing_outlier()


# ! Simpson's Paradox
