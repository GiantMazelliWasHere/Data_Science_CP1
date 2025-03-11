import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *
import statistics

ataques = pd.read_csv("databases/Ataques de Identidade e Explorações de Vulnerabilidades por Mês no Ano de 2024.csv")
vishing = pd.read_csv("databases/Campanhas de Vishing.csv")
ict = pd.read_csv("databases/ICT regulator have a cybersecurity mandate.csv")
leis = pd.read_csv("databases/Cybersecurity legislation_regulation exist.csv")

st.set_page_config(page_title="Análise de Dados", layout="wide")

st.logo("images/crowdstrike.png")

st.sidebar.markdown("Desenvolvido por Eduardo Mazelli ®️ 2025")
col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/GiantMazelliWasHere"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/eduardo-mazelli/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

st.image("images/estatistica.png", width=150)

st.title("Análise de Dados")

st.write("Nesta seção irei fazer uma breve análise de alguns dados relacionados a área de cybersecurity. Tirados de um relatório feito pela Crowdstrike, uma empresa de segurança cibernética e da ITU (International Telecommunication Union), uma agência especializada em tecnologia da informação e comunicação das Nações Unidas.")

st.header("Relatório da Crowdstrike:")

col1, col2 = st.columns([0.5, 0.5])

col1.subheader("Ataques por Mês 2024:")
col1.write("Nesse primeiro conjunto de dados temos o levantamento de dados feito pela Crowdstrike que nos mostra quantos ataques e explorações houveram em 2024, isso separando elas por mês.")
col1.table(ataques)
col1.write("Nesse conjuto de dados temos váriaveis do tipo qualitativas nomiais: os meses do ano e quantitativas discretas: a quantidade de ataques e explorações.")

col2.subheader("Campanhas de Vishing por Mês 2024:")
col2.write("Neste segundo ainda temos dados do mesmo relatório da Crowdstrike. Porém aqui podemos ver a quantidade de campanhas de Vishing realizadas no ano de 2024.")
col2.table(vishing)
col2.write("Nesse conjuto de dados temos váriaveis do tipo qualitativas nomiais: os meses do ano e quantitativas discretas: a quantidade de campanhas de Vishing.")

st.subheader("Perguntas:")
st.write("1. Qual foi o mês com mais ataques e explorações em 2024?")
st.write("3. Qual é a tendência dos ataques?")
st.write("4. Qual é a tendência das campanhas de Vishing?")
st.write("5. Quais intervalos de meses geralmente temos mais ataques para uma possível prevenção?")
st.write("6. Quais meses podemos prever um maior número de vishing para nos protegermos mais?")
st.write("7. Quando podemos prever um aumento nos ataques e assim talvez podermos entender melhor os hábitos daqueles que nos atacam?")


st.header("Relatório da ITU:")

col1, col2 = st.columns([0.5, 0.5])

col1.subheader("Tabela de Dados Proteção:")
col1.write("Nesta tabela podemos analisar quais países da américa do sul possuem algum tipo de proteção sobre as informações e comunicação no âmbito tecnológico.")
col1.table(ict)
col1.write("Neste conjunto de dados temos váriaveis apenas do tipo qualitativas nominais: os países da américa do sul e se eles possuem ou não alguma proteção.")

col2.subheader("Tabela de Dados Legislação:")
col2.write("Nesta segunda tabela analisamos quais países da américa do sul possuem algum tipo de legislação ou regulamentação sobre a segurança cibernética.")
col2.table(leis)
col2.write("Neste conjunto de dados temos váriaveis apenas do tipo qualitativas nominais: os países da américa do sul e se eles possuem ou não alguma legislação ou regulamentação.")

st.subheader("Perguntas:")
st.write("1. Quais países da américa do sul possuem proteção sobre as informações e comunicação no âmbito tecnológico?")
st.write("2. Quais países da américa do sul possuem legislação ou regulamentação sobre a segurança cibernética?")
st.write("3. Qual é a porcentagem de países que possuem proteção e legislação ou regulamentação?")
st.write("4. Qual é a porcentagem de países que possuem proteção e não possuem legislação ou regulamentação?")
st.write("5. Qual é a porcentagem de países que não possuem proteção e possuem legislação ou regulamentação?")
st.write("6. Qual é a porcentagem de países que não possuem proteção e nem legislação ou regulamentação?")
st.write("7. Na questão turística, quais países devemos tomar cuidado ao usar a tecnologia por não possuir nenhuma proteção?")

st.header("Análise inicial dos dados")

st.write("Para começar a análise dos dados, vamos começar com os dados da Crowdstrike.")

st.markdown("#### Tabela de Ataques:")

media_ataques = round(ataques["Quantidade de Ataques"].mean())
median_ataques = round(ataques["Quantidade de Ataques"].median())
moda_ataques = round(statistics.mode(ataques["Quantidade de Ataques"]))

st.write("A média de ataques e explorações em 2024 foi de:", media_ataques)
st.write("A mediana de ataques e explorações em 2024 foi de:", median_ataques)
st.write("A moda de ataques e explorações em 2024 foi de:", moda_ataques)

st.markdown("#### Tabela de Campanhas de Vishing:")

media_campanha = round(vishing["Quantidade de Campanhas"].mean())
median_campanha = round(vishing["Quantidade de Campanhas"].median())
moda_campanha = round(statistics.mode(vishing["Quantidade de Campanhas"]))

st.write("A média de campanhas de Vishing em 2024 foi de:", media_campanha)
st.write("A mediana de campanhas de Vishing em 2024 foi de:", median_campanha)
st.write("A moda de campanhas de Vishing em 2024 foi de:", moda_campanha)