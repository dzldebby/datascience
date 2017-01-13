import pandas as pd


df = pd.read_csv('student-por.csv', delimiter=";")

print df.head()

print df.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x = 'famsize', data = df, palette='muted')
plt.show()