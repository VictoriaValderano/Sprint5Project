import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles.csv")

st.header('Anúncios de vendas de Carros')

hist_button = st.button('Criar histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer", color_discrete_sequence=["#FFB6C1"])
    st.plotly_chart(fig, use_container_width=True)
    fig.show()

scatter_button = st.button('Criar Dispersão')
if scatter_button:
    st.write('Criando um Dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.update_traces(marker=dict(color="#FFB6C1"))
    st.plotly_chart(fig, use_container_width=True)
    fig.show()
