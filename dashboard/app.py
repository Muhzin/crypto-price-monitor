import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Cryptocurrency Price Monitor")
df = pd.read_parquet("../etl/bitcoin_processed.parquet")

# Plot candlestick chart
fig = px.line(df, x="date", y=["price", "7d_avg", "30d_avg"], 
              title="BTC Price with Moving Averages")
st.plotly_chart(fig)

# Alert logic
price_drop = (df["price"].iloc[-1] / df["price"].iloc[-24] - 1) * 100
if price_drop < -5:
    st.error(f"ALERT: Price dropped {price_drop:.2f}% in 24h!")
