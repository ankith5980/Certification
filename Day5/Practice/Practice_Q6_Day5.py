import numpy as np
import time

# Generate random matrices
A = np.random.rand(1000, 1000)
B = np.random.rand(1000, 1000)

# --- NumPy dot product ---
start = time.time()
C_np = np.dot(A, B)
end = time.time()
print("NumPy dot product time:", end - start, "seconds")

# --- Python nested loops ---
C_py = [[0] * 1000 for _ in range(1000)]

start = time.time()
for i in range(1000):
    for j in range(1000):
        s = 0
        for k in range(1000):
            s += A[i][k] * B[k][j]
        C_py[i][j] = s
end = time.time()
print("Python nested loop time:", end - start, "seconds")

print("\n")
print("========================")
print("\n")

# Create 10x10 matrix with values from 1 to 100
M = np.arange(1, 101).reshape(10, 10)

# Extract diagonal
diag = np.diag(M)

print("Matrix:\n", M)
print("Diagonal:", diag)


print("\n")
print("=========PROGRAM COMPLETE=========")
print("\n")
