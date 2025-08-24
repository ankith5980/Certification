import numpy as np

# stores 100 random numbers from 0 - 1000
arr = np.random.randint(0,1000, 100, dtype=int)
print(arr)

print("\n")

# Calculates the MEAN of element in the array
mean_arr = np.mean(arr, axis=0)
print("Mean :: ",mean_arr)

# Calculates the MEDIAN of the elements in the array
median_arr = np.median(arr, axis=0)
print("Median :: ", median_arr)

# Calculates the Standard Deviation of the elements in the array
std_arr = np.std(arr, axis=0)
print("Standard Deviation :: ", std_arr)

print("\n")
print("========================")
print("\n")

arr_a = np.array([12, 23, 34, 45, 56, 67, 78, 89, 90, 1])
arr_b = np.array([9, 98, 87, 76, 65, 54, 43, 32, 21, 10])

# Calculates the elements wise product
prod_arr_ab = arr_a * arr_b
print("Product of Array :: ", prod_arr_ab)

print("\n")
print("========================")
print("\n")


new_arr = np.array([2, 6, 67, 23, 4, 21, 9, 44])
print("Original Array :: ", new_arr)

# Storing new array after normalizing the original array
norm_arr = (new_arr - new_arr.min())/(new_arr.max() - new_arr.min())
print("Normalized Array :: ", norm_arr)

print("\n")
print("=========PROGRAM COMPLETE=========")
