import pandas as pd
import os
import matplotlib.pyplot as plt

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(symbol):
    """ Return file path for a specific symbol"""
    return os.path.join(CUR_DIR, "data", f"{symbol}.csv")

def get_data(symbols: list, dates):
    """ Get data from a list of symbols and panda date object"""
    df = pd.DataFrame(index= dates)
    if "SPY" not in symbols:
        symbols.append(0, 'SPY')

    for symbol in symbols:
        _file = get_path(symbol)
        dfp = pd.read_csv(_file,  index_col = 'Date', usecols = ['Date', 'Adj Close'], na_values = ['nan'])
        dfp = dfp.rename(columns={'Adj Close' : f'{symbol}'.upper()})
        df = df.join(dfp)
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])
    #print(df)
    return df

def get_data_slice(df, start: str, end: str):
    print(df[start:end])

def create_date_dataframe(start, end):
    return pd.date_range(start,end)

def plot_dataframe(df):
    """ Plot given dataframe"""
    #df = df / df[0]
    print(df)
    df = df / df.iloc[0]
    pl = df.plot(title = "Time vs Price")
    pl.set_xlabel("Time")
    pl.set_ylabel("Price")
    plt.show()

def create_df(file):
    start_date = "2010-01-22"
    end_date = "2010-01-26"
    dates = pd.date_range(start_date, end_date)
    print(dates[0])
    df1 = pd.DataFrame(index=dates)
    print(df1)
    for _ in file:
        _file = os.path.join(CUR_DIR, "data", f"{_}.csv")
        tdf = pd.read_csv(_file,  index_col="Date", parse_dates=True, na_values=['nan'], usecols=['Date', f'Adj Close'])
        tdf = tdf.rename(columns={'Adj Close':f'{_}'.upper()})
        df1 = df1.join(tdf) #default: left
    print(df1.dropna())

if __name__ == "__main__":
    # file = ["SPY", "GOOG", "IBM", "GLD"]
    file = ["SPY", "IBM"]
    df = get_data(file, create_date_dataframe('2010/1/1', '2010/12/31'))
    #df['2010-1-1':'2010-1-31']
    plot_dataframe(df)
    #get_data_slice(df, '2010-1-1', '2010-1-31')