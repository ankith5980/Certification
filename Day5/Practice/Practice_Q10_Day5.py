import pandas as pd

# stock DataFrame
stock_df = pd.DataFrame({
    "Date": pd.date_range(start="2025-01-01", periods=7),
    "Open": [100, 105, 110, 115, 120, 118, 125],
    "Close": [110, 100, 120, 125, 119, 130, 140],
    "Volume": [1000, 1200, 1500, 1700, 1600, 1800, 2000]
})

# Calculate price difference
stock_df["Diff"] = stock_df["Close"] - stock_df["Open"]

# Find day with max difference
max_diff_day = stock_df.loc[stock_df["Diff"].idxmax()]
print("Day with highest price difference:\n", max_diff_day)

print("\n")
print("========================")
print("\n")

stock_df["7D_Rolling_Avg"] = stock_df["Close"].rolling(window=7).mean()
print(stock_df[["Date", "Close", "7D_Rolling_Avg"]])

print("\n")
print("========================")
print("\n")

# bank transactions DataFrame
transactions_df = pd.DataFrame({
    "TransactionID": [1, 2, 3, 4, 5],
    "Account": ["A1", "A2", "A1", "A3", "A2"],
    "Amount": [250000, 600000, 450000, 800000, 300000]
})

# Filter suspicious transactions
suspicious_txn = transactions_df[transactions_df["Amount"] > 500000]
print("Suspicious Transactions:\n", suspicious_txn)

print("\n")
print("=========PROGRAM COMPLETE=========")
print("\n")
