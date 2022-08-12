import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.layers import Dense

import preparing_data as cd

model = Sequential()

model.add(Dense(1, input_shape=(4,), activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

model.summary()

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

model.fit(x_train, y_train, epochs=200)

accuracy = model.evaluate(x_test, y_test)[1]

print("Accuracy: ", accuracy)

model.save('.')