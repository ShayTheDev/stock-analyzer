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
# %% Statistical Volatility Function
def analyze_market_volatility(df_slice, negbound, posbound):
    '''Calculate the volatility of a stock's time-frame
    based on the provided negative and positive dynamic
    bounds.'''
    for date, daily_return in df_slice['Daily Return'].items() :
        cl_date = date.strftime('%d-%m-%Y')

        if pd.isna(daily_return):
            continue

        if daily_return >= posbound:
            print(f'{cl_date}, {daily_return}% : Keep Going...')
        elif daily_return <= negbound:
            print(f'{cl_date}, {daily_return}% : Warning...stay put') 
        else:
            print(f'{cl_date}, {daily_return}% : As Uzhe')
# %% Statistical Baseline Function
def calculate_baseline(df_slice, scale:int):
    '''Calculate the statistical baseline of a time-frame
    from df_slice and scale'''
    df_med = np.nanmedian(df_slice['Daily Return'])
    df_upbound = np.nanquantile(df_slice['Daily Return'], .75)
    df_lowbound = np.nanquantile(df_slice['Daily Return'], .25)
    df_iqr = round(df_upbound - df_lowbound, 3) 
    df_hbound = df_upbound + (df_iqr * scale)
    df_lbound = df_lowbound - (df_iqr * scale)
    m_base = (df_hbound, df_lbound)
    print(f'IQR: {df_iqr} | UP: {df_hbound} | LOW: {df_lbound}')
    return m_base
# %% Testing Functionality
y1_high, y1_low = calculate_baseline(year_one, 1)
y2_high, y2_low = calculate_baseline(year_two, 1)
analyze_market_volatility(year_one, y1_low, y1_high)
analyze_market_volatility(year_two, y2_low, y2_high) 

# %%
