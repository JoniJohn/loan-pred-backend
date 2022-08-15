import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

import preparing_data as cd

model = LogisticRegression()

df_train = pd.read_csv('train.csv')
print("Training DataFrame:")
print(df_train)

train = cd.cleaningData(df_train)
print("Training DataFrame Cleaning:")
print(train)

predictors_logistics = ['Credit_History', 'Education', 'Gender', 'Property_Area']
x_data = df_train[predictors_logistics].values
y_data = df_train[["Loan_Status"]].values

x_train = x_data[:300]
x_test = x_data[300:]
y_train = y_data[:300]
y_test = y_data[300:]

model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)

print("Accuracy: ", accuracy)

joblib.dump(model, 'lr_model.sav')