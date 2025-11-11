import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(r"C:\Users\rafae\OneDrive\Documentos\Documentos\Vick\TripleTen\GitVsCode\Projetos\Sprint 5 - Projeto\Sprint5Project\vehicles.csv")

hist_button = st.button('Criar histograma')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
    fig.show()

scatter_button = st.button('Criar Dispersão')
if scatter_button:
    st.write('Criando um Dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.show()
