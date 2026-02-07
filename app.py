import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Stocks_L.csv')
df['Date'] = pd.to_datetime(df['Date'])

st.title("Stock Price Visualization")

# Sidebar for interactivity
st.sidebar.header("Filter Options")

# Stock selection
stock_list = df['Stock'].unique()
selected_stock = st.sidebar.selectbox("Select Stock", stock_list)

# Date range selection
min_date = df['Date'].min()
max_date = df['Date'].max()
date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])

# Filter data by stock and date
filtered_df = df[(df['Stock'] == selected_stock) & 
                 (df['Date'] >= pd.to_datetime(date_range[0])) &
                 (df['Date'] <= pd.to_datetime(date_range[1]))]

# Metric selection
metric_options = ['Close', 'Open', 'Both']
selected_metric = st.sidebar.radio("Select Metric", metric_options)

# Plotting
st.subheader(f"{selected_stock} Stock Prices")
plt.figure(figsize=(10, 5))

if selected_metric == 'Close':
    sb.lineplot(x='Date', y='Close', data=filtered_df, label='Close Price')
elif selected_metric == 'Open':
    sb.lineplot(x='Date', y='Open', data=filtered_df, label='Open Price')
else:
    sb.lineplot(x='Date', y='Close', data=filtered_df, label='Close Price')
    sb.lineplot(x='Date', y='Open', data=filtered_df, label='Open Price')

plt.xlabel("Date")
plt.ylabel("Price")
plt.title(f"{selected_stock} Stock Price over Time")
plt.legend()
st.pyplot(plt)
