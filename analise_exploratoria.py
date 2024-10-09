import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/TaysonMartinss/AnaliseExploratoria/refs/heads/main/df_tratado.csv'
    df = pd.read_csv(url)
    return df
st.set_page_config(layout="wide")
df = load_data()


st.sidebar.title('Olá, Seja bem-vindo!')
selected_option = st.sidebar.radio("Escolha uma seção:", ["Dashboard", "Insights", "DATASET"])


#menu da dashboard

top_10_countries = df['Country'].value_counts().head(10)
pais_mais_usa_ia = df['Country'].loc[df['AISelect'].notna()].value_counts().idxmax()
ia_mais_usada = df['AISearchDevHaveWorkedWith'].value_counts().idxmax()
segunda_ia_mais_usada = df['AISearchDevHaveWorkedWith'].value_counts().index[1].split(';')[1]
qtd_brasileiros_usam_ia = (df['Country'].loc[df['AISelect'].notna()].value_counts()).index.get_loc('Brazil') + 1


def plot_top_countries():
    plt.figure(figsize=(12, 8.5))
    top_10_countries.plot(kind='bar')
    plt.title('Top 10 Países que Participaram da Pesquisa')
    plt.xlabel('País')
    plt.ylabel('Número de Participantes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

def plot_usa_python():
    df['UsaPython'] = df['LanguageHaveWorkedWith'].str.contains('Python', na=False)

    # Calcular a porcentagem de uso de Python
    porcentagem_python = df['UsaPython'].mean() * 100

    # Criar o gráfico de barras
    plt.figure(figsize=(6, 4))
    plt.bar(['Python'], [porcentagem_python])
    plt.ylabel('Porcentagem (%)')
    plt.title('Porcentagem de Utilização de Python no Último Ano')
    plt.ylim(0, 100)
    st.pyplot(plt)

def idade_uso_ia():
    idade_ia_counts = df.groupby('Age')['AISelect'].count()

    top_4_idades_ia = idade_ia_counts.nlargest(4)

    plt.figure(figsize=(10, 6))
    plt.bar(top_4_idades_ia.index, top_4_idades_ia.values)
    plt.xlabel('Idade')
    plt.ylabel('Número de Usuários de IA')
    plt.title('4 Idades que Mais Utilizam IA')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)
#########################################

if selected_option == "Dashboard":
    st.title(" 2024 Stack Overflow Developer Survey")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader('🌍País com mais usuários de IA:')
        st.text(pais_mais_usa_ia)


    with col2:
        st.subheader('🤖 IA mais utilizada:')
        st.text(ia_mais_usada)

    with col3:
        st.subheader('🤖🥈 Segunda IA mais utilizada:')
        st.text(segunda_ia_mais_usada)

    with col4:
        st.subheader('📊 Ranking do Brasil nas pesquisas:')
        st.text(f'{qtd_brasileiros_usam_ia}ª Lugar')

    col11, col12 = st.columns(2)
    with col11:
        plot_top_countries()
    with col12:
        plot_usa_python()

    coll22, col23 = st.columns(2)
    with coll22:
        idade_uso_ia()


elif selected_option == "Insights":
  st.subheader("teste")

elif selected_option == "DATASET":
    df.head()
