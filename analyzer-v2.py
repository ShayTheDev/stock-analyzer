# %% Import necessary modules
import yfinance as yf 
import pandas as pd 
# Download Stock Data 
# period_one = yf.download(tickers='S', start='2021-06-30', end='2023-06-30')
# period_one_csv = period_one.to_csv('symbol_s_period_one')
# %%
period_one = pd.read_csv('symbol_s_period_one')
period_one_np = period_one.to_numpy()
print(period_one_np)
period_one_df = pd.DataFrame(period_one_np) 
# QuickView 'period_one' -----------------
# %%
