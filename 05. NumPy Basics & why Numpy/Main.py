# NumPy Basics & why Numpy
# The Problem NumPy Solves
# Python lists are flexible, but they are not designed for large numerical data.

# When working with data:

# operations become slow
# memory usage increases
# code becomes loop-heavy
# NumPy exists to solve this problem.

# What NumPy Really Is
# NumPy provides:

# fast numeric arrays
# fixed data types
# operations on entire collections at once
# Instead of processing values one by one, NumPy processes data in bulk.

# Python List vs NumPy Array
# Python list:

data = [1, 2, 3, 4]
result = []
 
for x in data:
    result.append(x * 2)

# NumPy array:

import numpy as np
 
data = np.array([1, 2, 3, 4])
result = data * 2

# Same result, less code, much faster for large data.

# Creating NumPy Arrays
# import numpy as np
 
a = np.array([10, 20, 30])
b = np.zeros(5)
c = np.ones(3)
d = np.arange(1, 6)

# These are common ways numeric data is created.

# Vectorized Operations
# NumPy allows operations on entire arrays:

# a = np.array([1, 2, 3])
 
a + 10
a * 2
a > 1

# No explicit loops required. These operations are fast and efficient.

# Basic Useful Operations
a.sum()
a.mean()
a.max()
a.min()

# These are frequently used in data analysis.

# Two and Three Dimensional Arrays
matrix = np.array([[1, 2], [3, 4]])
tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# NumPy handles multi-dimensional data easily.