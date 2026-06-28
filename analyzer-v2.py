# %% Import necessary modules
import yfinance as yf 
import pandas as pd 
# Download Stock Data 
# period_one = yf.download(tickers='S', start='2021-06-30', end='2023-06-30')
# period_one_csv = period_one.to_csv('symbol_s_period_one')
# %% "Clean Slate" Ingestion
period_one = pd.read_csv(
    'symbol_s_period_one',
    header=[0,1],
    index_col=0,
    parse_dates=True)
period_one.dropna(axis=0)
period_one.columns = period_one.columns.get_level_values(0)
period_one.columns.name = None
period_one.index.name = 'Date'
# %% QuickView 'period_one' -----------------
period_one = period_one.round(2)
print(period_one.head()) 
# %%
