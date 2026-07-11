# ==========================================
# NumPy Linear Algebra
# ==========================================

import numpy as np

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# --------------------------
# Matrix Addition
# --------------------------

print("\nA + B:")
print(A + B)

# --------------------------
# Matrix Subtraction
# --------------------------

print("\nA - B:")
print(A - B)

# --------------------------
# Matrix Multiplication
# --------------------------

print("\nMatrix Multiplication (A @ B):")
print(A @ B)

# You can also use np.matmul()
print("\nUsing np.matmul():")
print(np.matmul(A, B))

# --------------------------
# Dot Product
# --------------------------

print("\nDot Product:")
print(np.dot(A, B))

# --------------------------
# Transpose
# --------------------------

print("\nTranspose of A:")
print(A.T)

# --------------------------
# Determinant
# --------------------------

print("\nDeterminant of A:")
print(np.linalg.det(A))

# --------------------------
# Inverse
# --------------------------

print("\nInverse of A:")
print(np.linalg.inv(A))

# --------------------------
# Eigenvalues and Eigenvectors
# --------------------------

eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)