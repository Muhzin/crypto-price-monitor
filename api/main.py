import requests
import pandas as pd
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()
COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"

@app.get("/fetch")
def fetch_crypto_data():
    response = requests.get(COINGECKO_URL)
    data = response.json()
    prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    prices["date"] = pd.to_datetime(prices["timestamp"], unit="ms")
    prices.to_parquet("bitcoin_prices.parquet")
    return {"status": "Data saved to parquet"}
# Minor update 1.1
# Minor update 1.2
# Minor update 1.3
# Minor update 2.1
# Minor update 2.2
# Minor update 2.3
# Minor update 3.1
# Minor update 3.2
# Minor update 3.3
# Minor update 4.1
# Minor update 4.2
# Minor update 4.3
# Minor update 5.1
# Minor update 5.2
# Minor update 5.3
