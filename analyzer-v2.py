# %% Import necessary modules
import yfinance as yf 
import pandas as pd
import datetime as dt
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
period_one = period_one[['Open', 'Close', 'Volume']]
# %% Slicing 'period_one' -----------------
period_one = period_one.round(2)
year_one = period_one.loc['2021-06-30':'2022-06-29'].copy()
year_two = period_one.loc['2022-06-30':'2023-06-29'].copy()
year_one['Daily Return'] = (year_one['Close'].pct_change() * 100).round(2)
year_two['Daily Return'] = (year_two['Close'].pct_change() * 100).round(2)
print(year_one.head())
print(year_two.head())
# %% Range **Test**
f_week = f_week.round(2)
for date, daily_return in f_week['Daily Return'].items() :
    if pd.isna(daily_return) :
        continue
    clean_date = date.strftime('%d-%m-%Y')
    if daily_return > 10 :
        print(f'{clean_date} : {daily_return}%')
    elif daily_return < -12.5 :
        print(f'{clean_date} : {daily_return}%')
    else :
        print(f'{clean_date} : {daily_return}%')
# %% period_one div

