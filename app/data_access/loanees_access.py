import pandas as pd

def getLoaneesDic():
    df = pd.read_csv('./data/test.csv')
    loanees = df[:4]
    print(loanees, flush=True)
    loanees_dic = loanees.to_dict('records')
    return loanees_dic
