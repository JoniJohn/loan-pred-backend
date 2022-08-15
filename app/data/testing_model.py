import numpy as np
import pandas as pd
import joblib

import preparing_data as cd

model = joblib.load("lr_model.sav")

test_df = pd.read_csv('test.csv')

test_cleaned = cd.cleaningData(test_df)

predictors_logistics = ['Credit_History', 'Education', 'Gender', 'Property_Area']
x_test = test_cleaned[predictors_logistics].values

np_test = np.array(x_test)

prob = model.predict_proba(np_test)

pred = model.predict(np_test)

print((prob, pred))
