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

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por Dia")
col1.plotly_chart(fig_date)

fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City",
                  title="Faturamento por Tipo de Produto", orientation="h")
col2.plotly_chart(fig_prod)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por Filial")
col3.plotly_chart(fig_city)

fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por Tipo de Pagamento")
col4.plotly_chart(fig_kind)

city_by_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_city_rating = px.bar(city_by_rating, y="City", x="Rating", title="Avaliação")
col5.plotly_chart(fig_city_rating, use_container_width=True)
