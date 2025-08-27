import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.DataFrame({
    "category" : ['A', 'B', 'C', 'D'],
    "value" : [4, 7, 2, 9]
})
sns.barplot(x="category", y="value", data=data)
plt.title("Normal Bar Chart (SeaBorn)")
plt.show()