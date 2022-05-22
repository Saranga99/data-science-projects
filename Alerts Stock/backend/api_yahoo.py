import yfinance as yf
import pandas as pd


def get_info_data(stock, start_d, end_d, interval_t):   ### Get data from yahoo finance
    df_yahoo = yf.download(stock, start=start_d, end=end_d, interval=interval_t,
                           progress=False, auto_adjust=True, group_by='tickers')
    df_yahoo.to_csv('df_yahoo.csv')
    df_yahoo = pd.read_csv('df_yahoo.csv')
    df_yahoo = df_yahoo.drop(df_yahoo.index[[0, 1]])
    df_yahoo = df_yahoo.rename(columns={'Unnamed: 0': 'Date'})
    df_yahoo.to_csv("df_yahoo.csv")
    result = df_yahoo["Close"].tolist()   ### Casting from df to list

    return result
