# %% Testing
import numpy as np 
np.set_printoptions(suppress=True,precision=2)

stock_arr = np.genfromtxt("sentinel-one_stock_data.csv",delimiter=",",skip_header=3)
print("Array shape:", stock_arr.shape) 
print(stock_arr[:,1:])
stock_open_close = np.array(stock_arr[:,1::3])
print(stock_open_close)
# Calculate summary statistics(mean,median,standard-deviation) 
mean_close = np.nanmean(stock_open_close[:,0])
print("Average stock's closing price is:",mean_close.round(2))
mean_open = np.nanmean(stock_open_close[:, 1]) 
print("Average stock's open price is:", mean_open.round(2))
std_close = np.std(stock_open_close[:-1, 0])
print("Standard deviation for closing is:",std_close.round(2))
std_open = np.std(stock_open_close[:-1, 1])
print("Standard deviation for opening is:",std_open.round(2))
open_close_corr = np.corrcoef(stock_open_close[:-1,:], rowvar=False)[0,1]
print("Correlation between close&open prices:",open_close_corr.round(2))
med_close = np.median(stock_open_close[:-1,0])
med_open = np.median(stock_open_close[:-1,1]) 
print("Median close:",med_close.round(2),"Median open:",med_open.round(2))
# %%
