import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color = "blue", marker = "x")
plt.title("Scatter Plot")
plt.show()
