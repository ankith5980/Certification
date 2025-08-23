import numpy as np

a = np.arange(6)
print("Primary output :: ", a)

b = a.reshape((2,3))

print("Reshaped to :: \n", b)