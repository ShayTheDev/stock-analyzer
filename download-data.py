import yfinance as yf 

# Define the stock ticker and the time window
ticker = "S" 

# Download the historical data as a pandas DataFrame 
stock_data = yf.download(ticker, start="2026-05-18", end="2026-06-19")

# Export it directly to a clean CSV file in your folder
stock_data.to_csv("sentinel-one_stock_data.csv") 

print("Data successfully downloaded and saved to sentinel-one_stock_data.csv!")