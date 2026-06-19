# %% Testing
import numpy as np 
np.set_printoptions(suppress=True,precision=2)

stock_arr = np.genfromtxt("sentinel-one_stock_data.csv",delimiter=",",skip_header=3)
print("Array shape:", stock_arr.shape) 
print(stock_arr[:,1:])
stock_open_close = np.array(stock_arr[:,1::3])
print(stock_open_close)
# %%
