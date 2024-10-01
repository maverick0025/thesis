import numpy as np
import time

# Create two large random matrices
matrix_size = 1000
A = np.random.rand(matrix_size, matrix_size)
B = np.random.rand(matrix_size, matrix_size)

# Perform matrix multiplication
start_time = time.time()
C = np.dot(A, B)  # Or use A @ B for matrix multiplication
end_time = time.time()

print(f"Matrix multiplication completed in {end_time - start_time} seconds.")

# Compute the eigenvalues of the result
start_time = time.time()
for i in range(1000000):
    eigenvalues, eigenvectors = np.linalg.eig(C)
end_time = time.time()

print(f"Eigenvalue calculation completed in {end_time - start_time} seconds.")

# Display the first 5 eigenvalues
print("First 5 eigenvalues:")
print(eigenvalues[:5])

