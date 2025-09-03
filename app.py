import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Load datasets
df_country = pd.read_csv("country_wise_latest.csv")
df_daywise = pd.read_csv("day_wise.csv")
df_grouped = pd.read_csv("full_grouped.csv")

fig = go.Figure()
st.title("Covid19 Tracking App 🚑")
st.markdown("Using **Kaggle Clean Complete Dataset** instead of API")

st.write(
    "Coronavirus is officially a pandemic. Since the first case in December the disease has spread fast reaching almost every corner of the world. "
    "The number of people that needs hospital care is growing as fast as the new cases. "
    "Some governments are taking measures to prevent a sanitary collapse. "
    "Let's see how some countries/regions are doing!"
)

# Sidebar
st.sidebar.header('Create/Filter your search')
graph_type = st.sidebar.selectbox('Cases type', ('Confirmed', 'Deaths', 'Recovered'))
st.sidebar.subheader('Search by country 📍')
country = st.sidebar.selectbox('Country', ["Worldwide"] + df_country["Country/Region"].tolist())
country1 = st.sidebar.selectbox('Compare with another Country', ["None"] + df_country["Country/Region"].tolist())

# Worldwide data
if country == "Worldwide":
    st.subheader("🌍 Worldwide Data")
    total = df_country["Confirmed"].sum()
    deaths = df_country["Deaths"].sum()
    recovered = df_country["Recovered"].sum()
    st.write(f"Total cases: {total:,}, Total deaths: {deaths:,}, Total recovered: {recovered:,}")

    fig.add_trace(go.Scatter(x=df_daywise["Date"], y=df_daywise[graph_type],
                             mode="lines", name=f"Worldwide {graph_type}"))
    st.plotly_chart(fig, use_container_width=True)

# Country-specific data
else:
    st.subheader(f"📍 {country} Data")
    row = df_country[df_country["Country/Region"] == country]
    st.write(f"Total cases: {int(row['Confirmed'])}, "
             f"Total deaths: {int(row['Deaths'])}, "
             f"Total recovered: {int(row['Recovered'])}")

    df_filtered = df_grouped[df_grouped["Country/Region"] == country]
    fig.add_trace(go.Scatter(x=df_filtered["Date"], y=df_filtered[graph_type],
                             mode="lines", name=country))

    # Compare with another country
    if country1 != "None":
        row2 = df_country[df_country["Country/Region"] == country1]
        st.write(f"Total cases in {country1}: {int(row2['Confirmed'])}, "
                 f"Total deaths: {int(row2['Deaths'])}, "
                 f"Total recovered: {int(row2['Recovered'])}")

        df_filtered2 = df_grouped[df_grouped["Country/Region"] == country1]
        fig.add_trace(go.Scatter(x=df_filtered2["Date"], y=df_filtered2[graph_type],
                                 mode="lines", name=country1))

    st.plotly_chart(fig, use_container_width=True)

st.sidebar.subheader("Created with 💖 in India")
st.sidebar.image('logo.jpg', width=300)
