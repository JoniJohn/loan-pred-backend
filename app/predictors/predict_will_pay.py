import pandas as pd
import numpy as np
import joblib

import app.data.preparing_data as cd


def predict(data):
    df = pd.DataFrame(data, index=[0])
    model = joblib.load("./app/data/lr_model.sav")

    df_cleaned = cd.cleaningData(df)

    predictors_logistics = ['Credit_History', 'Education', 'Gender', 'Property_Area']
    x_test = df_cleaned[predictors_logistics].values
    np_test = np.array(x_test)

    probability = model.predict_proba(np_test)
    print(probability)

    prediction = model.predict(np_test)
    print(prediction)

    return ("N" if prediction[0] == 0 else "Y", probability[0][prediction[0]])