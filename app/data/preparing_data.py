import numpy as np
import pandas as pd
from sklearn import preprocessing

def cleaningData(df):    
    # Replace missing value of Self_Employed with more frequent category
    df['Self_Employed'] = df['Self_Employed'].fillna('No',inplace=True)
    # df['LoanAmount'] = df['LoanAmount'].fillna(0)

    # Add both ApplicantIncome and CoapplicantIncome to TotalIncome
    df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']

    # Looking at the distribtion of TotalIncome
    df['LoanAmount'].hist(bins=20)

    # Perform log transformation of TotalIncome to make it closer to normal
    df['LoanAmount_log'] = np.log(df['LoanAmount'])

    # Looking at the distribtion of TotalIncome_log
    df['LoanAmount_log'].hist(bins=20)

    # Impute missing values for Gender
    df['Gender'].fillna(df['Gender'].mode()[0],inplace=True)
    # Impute missing values for Married
    df['Married'].fillna(df['Married'].mode()[0],inplace=True)
    # Impute missing values for Dependents
    df['Dependents'].fillna(df['Dependents'].mode()[0],inplace=True)
    # Impute missing values for Credit_History
    df['Credit_History'].fillna(df['Credit_History'].mode()[0],inplace=True)
    # Convert all non-numeric values to number
    # cat=['Gender','Married','Dependents','Education','Self_Employed','Credit_History','Property_Area', 'Loan_Status']

    cat = pd.Categorical(df)
    # print("cats: ",)

    for var in cat:
        le = preprocessing.LabelEncoder()
        df[var]=le.fit_transform(df[var].astype('str'))

    df = df.dropna()
    
    return df