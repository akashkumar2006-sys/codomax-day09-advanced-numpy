# ==========================================
# Codomax AI/ML Internship - Day 9
# Topic: Advanced NumPy
# Author: Akash Kumar Jha
# ==========================================

import numpy as np

print("=" * 60)
print("          ADVANCED NUMPY - DAY 9")
print("=" * 60)

# Create Array
arr = np.array([10, 20, 30, 40, 50, 60])

print("\nOriginal Array:")
print(arr)

# Indexing
print("\nFirst Element:", arr[0])
print("Last Element:", arr[-1])

# Slicing
print("\nArray Slicing:")
print(arr[1:5])

# Reshape
matrix = np.arange(1, 13).reshape(3, 4)

print("\n3 x 4 Matrix")
print(matrix)

# Transpose
print("\nTranspose")
print(matrix.T)

# Identity Matrix
print("\nIdentity Matrix")
print(np.eye(3))

# Random Numbers
print("\nRandom Array")
random_array = np.random.randint(1, 100, size=(3, 3))
print(random_array)

# Matrix Multiplication
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("\nMatrix A")
print(A)

print("\nMatrix B")
print(B)

print("\nMatrix Multiplication")
print(np.matmul(A, B))

print("\nMaximum Value:", np.max(random_array))
print("Minimum Value:", np.min(random_array))
print("Mean:", np.mean(random_array))

print("\nProgram Executed Successfully ✅")
print("=" * 60)
