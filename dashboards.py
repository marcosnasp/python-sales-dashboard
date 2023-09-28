import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
df = pd.read_csv("./datasets/supermarket_sales.csv", sep=",", decimal=".")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Month", df["Month"].unique())
df_filtered = df[df["Month"] == month]
df_filtered