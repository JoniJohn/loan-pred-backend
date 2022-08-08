import pandas as pd

def getLoaneesDic():
    df = pd.read_csv('./data/test.csv')
    loanees = df[:4]
    loanees_dic = loanees.to_dict('records')
    return loanees_dic

def willRepayLoan(loane_details):
    return loane_details