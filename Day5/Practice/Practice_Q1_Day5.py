import numpy as np

# Creats a matrix where all the elements are zero
id_mat = np.zeros((5,5), dtype=int)
print(id_mat)

print("\n")

# Changes all the diagonal elements to 1
id_mat = np.diag((np.ones(5, dtype=int)))
print(id_mat)

print("\n")
print("=============================")
print("\n")

# Simple list with numbers
num_list = [1,2,3,4,5,6,7,8,9]
print(num_list)

print("\n")

# Conversion of the list into numpy array
np_list = np.array(num_list)
print(np_list)

print("\n")

# Reshaping the numpy array from 1-D to 2-D
reshaped = np_list.reshape(3,3)
print(reshaped)

print("\n")
print("=============================")
print("\n")

# Converting all the even elements in a numpy array to -1
arr = np.array([1,2,3,4,5,6,7,8,9])
arr[arr % 2 == 0] = -1
print(arr)

print("\n")
print("======PROGRAM COMPLETE======")