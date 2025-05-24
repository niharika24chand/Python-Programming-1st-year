# Check Number of Dimension
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Numpy-Array Creation using empty()
from numpy import *
a = empty((3, 2), dtype=int)
print(a)
# numpy.empty(shape, dtype=float, order='C')

# Numpy-Array Creation using zeros()
a = zeros((3, 2), dtype=float)
print(a)

# Numpy-Array Creation using ones()
a = ones((3, 2), dtype=float)
print(a)

# Numpy Array creation using arange() and reshape()
import numpy as np
print("A\n", np.arange(4).reshape(2, 2), "\n")
print("A\n", np.arange(4, 10), "\n")
print("A\n", np.arange(4, 20, 3), "\n")

# Numpy-Array Creation using linspace()
from numpy import *
a = linspace(10, 20, 5, dtype=complex)
print(a)

# Numpy-Array- Indexing & Slicing
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

from numpy import *
a = array([1,2,3,4,5,6])
s = slice(2,5,1)
print(a[s])

# Slicing array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Slice elements from index 4 to the end of the array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

# Slice elements from the beginning to index 4 (not included)
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

# Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

# Reshaping array
from numpy import *
a = array([[1,2,3],[4,5,6]])
print(a)
b = a.reshape(3,2)
print(b)

# Joining NumPy Arrays
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# Splitting NumPy Arrays
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# Sorting Array
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

# Numpy-Array- Broadcasting
import numpy as np
a = np.array([17, 11, 19]) # 1x3 Dimension array
print(a)
b = 3
print(b)

# Broadcasting happened because of mismatch in array Dimension
c = a + b
print(c)

A = np.array([[11, 22, 33], [10, 20, 30]])
print(A)
b = 4
print(b)
C = A + b
print(C)