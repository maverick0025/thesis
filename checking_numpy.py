import numpy as np
import time

# Start the timer
start_time = time.time()

# Generate two large random matrices
matrix_size = 5000  # Adjust size to roughly hit 2 seconds, depending on your system
A = np.random.rand(matrix_size, matrix_size)
B = np.random.rand(matrix_size, matrix_size)

# Perform matrix multiplication
C = np.dot(A, B)

# End the timer
end_time = time.time()

# Check how long it took
print(f"Time taken: {end_time - start_time} seconds")

