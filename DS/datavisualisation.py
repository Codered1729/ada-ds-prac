import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\cvr\Downloads\iris-data.csv')

sns.scatterplot(
    x='Sepal length',
    y='petal length',
    hue='class',
    data=df,
    palette='Set1',
    s=80
)

plt.title('Scatter plot of Sepal length vs petal length')
plt.xlabel('Sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.legend(title='Species')
plt.show()
