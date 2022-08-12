import numpy as np
from keras import models
import pandas as pd
import preparing_data as cd

model = models.load_model(".")

test_df = pd.read_csv('test.csv')

test_cleaned = cd.cleaningData(test_df)

predictors_logistics = ['Credit_History', 'Education', 'Gender', 'Property_Area']
x_test = test_cleaned[predictors_logistics].values
print(x_test)
np_test = np.array(x_test)

res = model.predict(np_test)

print(res)
