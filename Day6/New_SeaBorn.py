import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.histplot(data=df, x="total_bill", bins=20, kde=True, color="skyblue")
plt.title("Histogram + KDE")
plt.show()
