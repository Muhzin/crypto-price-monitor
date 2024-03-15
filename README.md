Final README.md
markdown

# Cryptocurrency Price Monitor with Alerts
**Real-time Bitcoin price tracker with moving averages and automated alerts**   

---

##  Features
- **API Data Fetcher**: Pulls live Bitcoin prices from CoinGecko (FastAPI)
- **ETL Pipeline**: Calculates 7-day/30-day moving averages (Pandas + DuckDB)
- **Streamlit Dashboard**: Interactive candlestick charts + price drop alerts (>5%)
- **CI/CD**: GitHub Actions for automated testing

---

##  Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/crypto-price-monitor.git
   cd crypto-price-monitor

    Set up a virtual environment:
    bash

python -m venv venv
source venv/bin/activate  # Linux

Install dependencies:
bash

    pip install -r api/requirements.txt
    pip install -r dashboard/requirements.txt

## Usage
1. Run the API Fetcher
bash

cd api
uvicorn main:app --reload

    Endpoint: GET /fetch (saves data to bitcoin_prices.parquet)

2. Run the ETL Pipeline
bash

cd ../etl
python transform.py

    Output: bitcoin_processed.parquet with moving averages

3. Launch the Dashboard
bash

cd ../dashboard
streamlit run app.py

    Open http://localhost:8501 to view the dashboard

## License

MIT License - See LICENSE for details.
