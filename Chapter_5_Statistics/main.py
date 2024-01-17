# Dataset form chapter 1

from collections import Counter
from typing import List
import matplotlib.pyplot as plt
import random
import string
num_friends = [100, 49, 41, 40, 25, 39, 40, 47, 16, 11, 2, 16, 31, 16, 38, 15, 12, 11, 19, 33, 11, 36, 29, 44, 23, 21, 38, 11, 7, 1, 45, 9, 20, 49, 39, 46, 39, 16, 16, 13, 14, 26, 13, 48, 39, 35, 3, 3, 39, 18, 49, 35, 1, 13, 4, 19, 35, 11, 9, 47, 8, 11, 9, 11, 39, 39, 9, 45, 15, 36, 6, 29, 17, 35, 34, 2, 7, 33, 7, 29, 18, 31, 6, 32, 1, 42, 49, 3, 28, 30, 3, 15, 37, 4, 10, 39, 35, 30, 8, 22, 2, 5, 17, 32, 25, 2, 40, 8, 45, 10, 5, 21, 19, 36, 21, 11, 2, 4, 16, 13, 11, 26, 23, 46, 43, 46, 16, 5, 38, 31, 49, 1, 7, 2, 25, 7, 35, 20, 45, 33, 29, 6, 37, 23, 34, 30, 42, 5, 5, 2, 48, 23, 15, 2, 16, 17, 19, 13, 13, 24, 37, 23, 7, 22, 48, 47, 39, 45, 22, 23, 13, 20, 47, 44, 30, 38, 26, 20, 39, 6, 47, 38, 17, 11, 31, 39, 1, 43, 32, 28, 47, 34, 17, 42, 35, 25, 38, 6, 28, 26, 4, 42, 21, 12, 41, 18, 12, 17]
print(num_friends)
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

from..Chapter_4_Linear_Algebra.main import sum_of_squares

def de_mean(xs: List[float]) -> List[float]:
  """Translate xs by subtracting its mean (so the result has mean 0)"""
  x_bar = mean(xs)
  return [x-x_bar for x in xs]

def variance(xs: List[float]) -> float:
  """Almost the average squared deviation from the mean"""
  assert len(xs) >= 2, "Variance requires at least two elements"
  
  n = len(xs)
  deviations = de_mean(xs)
  return sum_of_squares(deviations) / (n - 1)
print(variance(num_friends))