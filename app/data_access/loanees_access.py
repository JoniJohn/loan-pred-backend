import pandas as pd

def getLoaneesDic():
    df = pd.read_csv('./app/data/test.csv')
    loanees = df[:4]
    loanees_dic = loanees.to_dict('records')
    return loanees_dic
