from typing import List
from matplotlib import pyplot as pt
Vector = List[float]
height_weight_age = [ 70, # inches
                      170,# pounds
                      40 ]#years

grades = [95, #exam1
          80, #exam2
          75, #exam3
          62  #exam4
          ]

# adding two vectors
def add(v: Vector, w: Vector) -> Vector:
  """Adds corresponding elements"""
  assert len(v) == len(w), 'vectors must be the same length'
  return [v_i + w_i for v_i, w_i in zip(v,w)]
assert add([1,2,3],[4,5,6]) == [5,7,9]

# subtracting two vectors
def subtract(v: Vector, w: Vector)->Vector:
  """Subtracts corresponding elements"""
  assert len(v) == len(w), "vectors must be the same length"
  return [v_i - w_i for v_i, w_i in zip(v,w)]
assert subtract([5,7,9], [4,5,6]) == [1,2,3]

def vector_sum(vectors: List[Vector])->Vector:
  """Sum all corresponding elements"""
  assert vectors, 'no vectors provided'
  
  # Check the vectors are all the same size
  num_elements = len(vectors[0])
  assert all(len(v) == num_elements for v in vectors), "different sizes!"

  # the i-th element of the result is the sum of every vector[i]
  return [sum(vector[i] for vector in vectors)
          for i in range(num_elements)]
# Testing
assert vector_sum([[1,2], [3,4], [5,6], [7,8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
  """Multiples every element by C"""
  return [c * v_i for v_i in v]

assert scalar_multiply(2, [1,2,3]) == [2, 4, 6]


# vector mean
def vector_mean(vectors: List[Vector]) -> Vector:
  """Computes the element wise average"""
  n = len(vectors)
  return scalar_multiply(1/n, vector_sum(vectors))
assert vector_mean([[1,2], [3,4], [5,6]]) == [3,4]


# The dot product of two vectors is the sum of their component_wise products

def dot(v: Vector, w: Vector) -> float:
  """Compute v_i * w_i + ...... + v_n * w_n"""
  assert len(v) == len(w), "vectors must be of same length"

  return sum(v_i * w_i for v_i, w_i in zip(v,w))

assert dot([1,2,3], [4,5,6]) == 32 

a = [0,2]
b = [0,4]
# _dot = dot(a, b)

# pt.plot(a)
# pt.plot(b)
# pt.show()

# Vector's sum of squares
def sum_of_squares(v:Vector) -> float:
  """Return v_i * v_i + ......... + v_n * v_n"""
  return dot(v, v)

assert sum_of_squares([1,2,3]) == 14

# This can be used to compute its magnitude

import math
def magnitude(v:Vector) -> float:
  """Returns the magnitude (or length) of v"""
  return math.sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5

# Now we have all the pieces needed to compute distance between two vectors

def squared_distance(v: Vector, w: Vector) -> float:
  """Computes (v_i - w_i) ** 2 + ....... + (v_n - w_n) ** 2"""
  return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector) -> float:
  """Computes the distance between v and w"""
  return math.sqrt(squared_distance(v,w))


#! ======================== Matrices =======================

# Another type of alias
Matrix = List[List[float]]

A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [1,2],
    [3,4],
    [5,6]
]

from typing import Tuple

def shape(A:Matrix) -> Tuple[int, int]:
  """Returns (# of rows of A, # of columns of A)"""
  num_rows = len(A)
  num_cols = len(A[0]) if A else 0
  return num_rows, num_cols

assert shape([[1,2,3],[4,5,6]]) == (2,3)


# Getting a matrix row
def get_row(A: Matrix, i:int) -> Vector:
  """Returns the i-it row of A (as a vector)"""
  return A[i]

def get_column(A: Matrix, j: int) -> Vector:
  """Returns the j-th column of A (as a vector)"""
  return [A_i[j]
          for A_i in A]

# Creating a matrix from the given the shape of matrix and the function for generating the elements. We can do it using a nested list comprehension:

from typing import Callable

def make_matrix(num_rows: int,
                num_cols : int,
                entry_fn : Callable[[int, int], float]) -> Matrix:
  """
  Returns a num_rows X num_cols matrix whose (i,j)-th entry is entry_fn(i,j)
  """
  return [[entry_fn(i,j)
            for j in range(num_cols)]
          for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
  """Returns the n x n identity Matrix"""
  return make_matrix(n, n, lambda i,j : 1 if i == j else 0)

assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]



