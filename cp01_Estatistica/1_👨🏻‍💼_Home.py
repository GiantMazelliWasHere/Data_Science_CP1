import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Eduardo Mazelli", layout="wide")

st.logo("crowdstrike.png")

st.sidebar.markdown("Desenvolvido por Eduardo Mazelli ®️ 2025")

col1, col2 = st.sidebar.columns([0.5, 0.5])
col1.markdown("""<a href="https://github.com/GiantMazelliWasHere"><img src="https://cdn3.emoji.gg/emojis/6705-githubblack.png" width="64px" height="64px" alt="github"></a>""", unsafe_allow_html=True)
col2.markdown("""<a href="https://www.linkedin.com/in/eduardo-mazelli/"><img src="https://cdn3.emoji.gg/emojis/70322-linkedin.png" width="64px" height="64px" alt="LinkedIn"></a>""""", unsafe_allow_html=True)

col1, col2 = st.columns([0.25, 0.75])
col1.image("perfil.png", width=150)
col2.title("Eduardo Mazelli")
col2.write("+55 (11) 97649-4397")
col2.write("eduardo.mazelli@gmail.com")

st.title("Sobre Mim!")

st.write("Nasci e cresci na cidade, sempre estive cercado por inovação, mudanças rápidas e infinitas oportunidades. Esse ambiente dinâmico moldou minha curiosidade e determinação, levando-me a seguir um caminho na tecnologia.")
st.write("Além disso, meu amor e paixão pela tecnologia alimenta meu desejo de aprender, criar e resolver problemas que possam fazer a diferença. Seja desenvolvendo novas soluções, otimizando processos ou explorando tendências emergentes, encontro entusiasmo na natureza em constante evolução do mundo da tecnologia.")
st.write("Uma das minhas maiores qualidades é minha capacidade de trabalhar bem em equipe, entendendo que a colaboração impulsiona a inovação. Junto com minhas fortes habilidades de gestão do tempo, próspero em ambientes acelerados, onde eficiência e criatividade são fundamentais.")
st.write("O que realmente me inspira—tanto no trabalho quanto na vida pessoal—é o impacto que posso ter na vida dos outros. Seja mentorando, criando soluções que melhorem vidas ou simplesmente compartilhando conhecimento, sou movido pelo potencial de gerar mudanças positivas.")
st.write("À medida que continuo minha jornada no mundo da tecnologia, espero ultrapassar limites, aprender com os outros e fazer contribuições significativas para a indústria e além.")
