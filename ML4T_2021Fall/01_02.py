import pandas as pd
import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def create_df(file):
    start_date = "2010-01-22"
    end_date = "2010-01-26"
    dates = pd.date_range(start_date, end_date)
    print(dates[0])
    df1 = pd.DataFrame(index=dates)
    print(df1)

    _file = os.path.join(CUR_DIR, "data", f"{file}.csv")
    dspy = pd.read_csv(_file,  index_col="Date", parse_dates=True, na_values=['nan'])

    df1 = df1.join(dspy)
    print(df1)

if __name__ == "__main__":
    file = "SPY"
    create_df(file)