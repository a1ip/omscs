import csv
import os
import pandas as pd
import matplotlib.pyplot as plt


CUR_DIR = os.path.dirname(os.path.abspath(__file__))
HCP_FILE =  os.path.join(CUR_DIR, "data", "HCP.csv")

#os.path.dirname(HCP_FILE)
def read_csv(_file):
    with open(_file, 'r') as fp:
        csv_file = csv.reader(fp)
        for _ in csv_file:
            print(_)

def read_pd(comp):
    _file = os.path.join(CUR_DIR, "data", f"{comp}.csv")
    df = pd.read_csv(_file)
    print(df.head(1)) #first 10 lines viewing
    # print(df.tail(10)) # last 10 lines
    # print(df[10:21])

def read_by_company(comp, stat):
    """ Find the max and mean value for given symbol"""
    _file = os.path.join(CUR_DIR, "data", f"{comp}.csv" )
    df = pd.read_csv(_file)
    if stat == "max":
        return df['Close'].max()
    elif stat == "mean":
        return df['Volume'].mean()

def plot_data(comp, col_list):
    _file = os.path.join(CUR_DIR, "data", f"{comp}.csv")
    df = pd.read_csv(_file)
    # for item in col_list:
    #     df[item].plot()
    df[col_list].plot()
    plt.show()

if __name__ == '__main__':
    #read_csv(HCP_FILE)
    #read_pd(HCP_FILE)
    ll = ["AAPL"]
    type_stat = "mean"
    print(f"Company {type_stat}")
    for item in ll:
        #read_pd(item)
        #print(f"{item} {read_by_company(item,type_stat)}")
        plot_data(item, ["Close", "Adj Close"])
