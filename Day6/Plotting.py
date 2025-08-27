import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, color = "red", linestyle = "--", marker = "o")
plt.title("Line Plot") # Graph Title
plt.xlabel("X-axis") # Label for x
plt.ylabel("Y-axis") # Label for y 
plt.show()