import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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

# Função para carregar os dados (Substitua as URLs pelos links do seu dataset)
@st.cache
def load_data():
    idade_df = pd.read_csv('url_para_idade_dataset.csv')
    usa_IA_df = pd.read_csv('url_para_usa_IA_dataset.csv')
    profissao_df = pd.read_csv('url_para_profissao_dataset.csv')
    ia_opniao_df = pd.read_csv('url_para_opniao_dataset.csv')
    
    return idade_df, usa_IA_df, profissao_df, ia_opniao_df

# Carregar os dados
idade_df, usa_IA_df, profissao_df, ia_opniao_df = load_data()

# Título da aplicação
st.title('Análise do Uso de IA por Desenvolvedores')

### Gráfico 1: Porcentagem de desenvolvedores que usam IA em cada faixa etária
st.header('Porcentagem de desenvolvedores que usam IA em cada faixa etária')

idade_usa_ia = round((pd.crosstab(idade_df, usa_IA_df, normalize='index') * 100), 2)

# Criar gráfico com seaborn
fig, ax = plt.subplots()
sns.heatmap(idade_usa_ia, annot=True, cmap="YlGnBu", ax=ax)
ax.set_title("Uso de IA por Faixa Etária (%)")
st.pyplot(fig)

### Gráfico 2: Porcentagem de desenvolvedores que usam IA em cada profissão
st.header('Porcentagem de desenvolvedores que usam IA em cada profissão')

profissao_usa_ia = round((pd.crosstab(profissao_df, usa_IA_df, normalize='index') * 100), 2)

# Criar gráfico com seaborn
fig2, ax2 = plt.subplots()
sns.heatmap(profissao_usa_ia, annot=True, cmap="YlOrRd", ax=ax2)
ax2.set_title("Uso de IA por Profissão (%)")
st.pyplot(fig2)

### Gráfico 3: Opinião predominante sobre IA entre desenvolvedores
st.header('Opinião predominante sobre IA entre os desenvolvedores')

opiniao_ia_contagem = ia_opniao_df.value_counts()

# Criar gráfico de barras
fig3, ax3 = plt.subplots()
opiniao_ia_contagem.plot(kind='bar', ax=ax3, color="skyblue")
ax3.set_title("Opinião sobre IA")
ax3.set_xlabel("Opinião")
ax3.set_ylabel("Quantidade")
st.pyplot(fig3)
