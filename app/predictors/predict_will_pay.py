from operator import index
import pandas as pd
import numpy as np
from keras import models
import data.preparing_data as cd

def predict(data):
    df = pd.DataFrame(data, index=[0])
    model = models.load_model("./data")

    df_cleaned = cd.cleaningData(df)

    predictors_logistics = ['Credit_History', 'Education', 'Gender', 'Property_Area']
    x_test = df_cleaned[predictors_logistics].values
    np_test = np.array(x_test)

    res = model.predict(np_test)

    return res[0][0]