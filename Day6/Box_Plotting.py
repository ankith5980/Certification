import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.random.normal(100, 20, 200)
plt.boxplot(data)
plt.title("Box Plot")
plt.show()
