import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Função para carregar os dados do GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/TaysonMartinss/AnaliseExploratoria/refs/heads/main/dataframe_tratado.csv'
    df = pd.read_csv(url)
    return df

# Carregar os dados
df = load_data()

# Título da aplicação
st.title('Análise do Uso de IA por Desenvolvedores')

### Gráfico 1: Porcentagem de desenvolvedores que usam IA em cada faixa etária
st.header('Porcentagem de desenvolvedores que usam IA em cada faixa etária')

# Ajuste para os nomes das colunas
if 'Age' in df.columns and 'AISelect' in df.columns:
    idade_usa_ia = round((pd.crosstab(df['Age'], df['AISelect'], normalize='index') * 100), 2)

    # Criar gráfico com seaborn
    fig, ax = plt.subplots()
    sns.heatmap(idade_usa_ia, annot=True, cmap="YlGnBu", ax=ax)
    ax.set_title("Uso de IA por Faixa Etária (%)")
    st.pyplot(fig)
else:
    st.error("As colunas 'Age' ou 'AISelect' não foram encontradas no DataFrame.")

### Gráfico 2: Porcentagem de desenvolvedores que usam IA em cada profissão
st.header('Porcentagem de desenvolvedores que usam IA em cada profissão')

if 'MainBranch' in df.columns and 'AISelect' in df.columns:
    profissao_usa_ia = round((pd.crosstab(df['MainBranch'], df['AISelect'], normalize='index') * 100), 2)

    # Criar gráfico com seaborn
    fig2, ax2 = plt.subplots()
    sns.heatmap(profissao_usa_ia, annot=True, cmap="YlOrRd", ax=ax2)
    ax2.set_title("Uso de IA por Profissão (%)")
    st.pyplot(fig2)
else:
    st.error("As colunas 'MainBranch' ou 'AISelect' não foram encontradas no DataFrame.")

### Gráfico 3: Opinião predominante sobre IA entre desenvolvedores
st.header('Opinião predominante sobre IA entre os desenvolvedores')

if 'AISent' in df.columns:
    opiniao_ia_contagem = df['AISent'].value_counts()

    # Criar gráfico de barras
    fig3, ax3 = plt.subplots()
    opiniao_ia_contagem.plot(kind='bar', ax=ax3, color="skyblue")
    ax3.set_title("Opinião sobre IA")
    ax3.set_xlabel("Opinião")
    ax3.set_ylabel("Quantidade")
    st.pyplot(fig3)
else:
    st.error("A coluna 'AISent' não foi encontrada no DataFrame.")
