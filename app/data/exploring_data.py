import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

plt.figure()

sns.pairplot(df, hue='Loan_Status')

plt.show()

print('Dataset stats: \n', df.describe())

print('Observations per class: \n', df['Loan_Status'].value_counts())

