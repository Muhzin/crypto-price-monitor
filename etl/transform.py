import pandas as pd

def calculate_moving_averages():
    df = pd.read_parquet("../api/bitcoin_prices.parquet")
    df["7d_avg"] = df["price"].rolling(window=7).mean()
    df["30d_avg"] = df["price"].rolling(window=30).mean()
    df.to_parquet("bitcoin_processed.parquet")

if __name__ == "__main__":
    calculate_moving_averages()
