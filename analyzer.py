# %% Testing
import numpy as np 
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True,precision=2)

stock_arr = np.genfromtxt("sentinel-one_stock_data.csv",delimiter=",",skip_header=3)
print("Array shape:", stock_arr.shape) 
print(stock_arr[:,1:])
stock_open_close = np.array(stock_arr[:,1::3])
stock_volume = np.array(stock_arr[:,-1:])
print(stock_volume)
print(stock_open_close)
# Calculate summary statistics(mean,median,standard-deviation) 
mean_close = np.nanmean(stock_open_close[:,0])
print("Average stock's closing price is:",mean_close.round(2))
mean_open = np.nanmean(stock_open_close[:, 1]) 
print("Average stock's opening price is:", mean_open.round(2))
med_close_open = np.nanmedian(stock_open_close, axis=0)
print("Median closing price:",med_close_open[0].round(2),"\nMedian opening price:", med_close_open[1].round(2))
std_close = np.std(stock_open_close[:-1, 0])
print("Standard deviation for closing is:",std_close.round(2))
std_open = np.std(stock_open_close[:-1, 1])
print("Standard deviation for opening is:",std_open.round(2))
open_close_corr = np.corrcoef(stock_open_close[:-1,:], rowvar=False)[0,1]
print("Correlation between close&open prices:",open_close_corr.round(2))
# Plotting for idiots
s_close = stock_open_close[:,0]
s_open = stock_open_close[:,1]
s_vol = stock_volume
plt.scatter(s_close,s_open,alpha=0.8,s=stock_volume * 0.00001)
# Labeling Axes
plt.xlabel("Closing Prices[in USD]")
plt.ylabel("Opening Prices[in USD]")
plt.title("SentinalOne | Ticker: S | May-June '26")
# Setting Ticks
plt.show()
# %%
