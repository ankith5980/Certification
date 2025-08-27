import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data = df, hue="sex", style="time")
plt.title("Scatter Plot")
plt.show()
