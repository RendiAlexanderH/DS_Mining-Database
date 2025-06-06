import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("diabetes.csv")

df.head()

df.tail()

df.sample(5)

df.shape

df.info()

df.dtypes

df.describe()

df['Pregnancies'].describe()

# Visualisasi
data['label'].value_counts().plot(kind='bar')
plt.title('Distribusi Label')
plt.xlabel('Label')
plt.ylabel('Jumlah')
plt.show()
