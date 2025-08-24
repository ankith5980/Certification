import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6], dtype=float)

# Compute mean ignoring NaNs
mean_val = np.nanmean(arr)

# Replace NaNs with mean
arr[np.isnan(arr)] = mean_val

print(arr)

print("\n")
print("========================")
print("\n")

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])

common = np.intersect1d(a, b)
print(common)

print("\n")
print("========================")
print("\n")

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

# reshape
flat1 = matrix.reshape(-1)

# ravel
flat2 = matrix.ravel()

print(flat1)
print(flat2)

print("\n")
print("=========PROGRAM COMPLETE=========")
print("\n")
