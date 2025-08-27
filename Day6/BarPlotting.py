import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

categories = ['A', 'B', 'C']
values = [3, 7, 5]
plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title("Bar Plot")
plt.show()
