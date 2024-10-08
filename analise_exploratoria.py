import streamlit as st
import pandas as pd

# URL do seu dataset no GitHub
url = 'https://raw.githubusercontent.com/TaysonMartinss/AnaliseExploratoria/refs/heads/main/dataframe_tratado.csv'

# Carregar o dataset
@st.cache
def load_data():
    data = pd.read_csv(url)
    return data

# Carregar os dados
data = load_data()

# Título do app
st.title('Minha aplicação no Streamlit')

# Mostrar os dados
st.write("Aqui estão os dados do meu dataset:")
st.dataframe(data)
