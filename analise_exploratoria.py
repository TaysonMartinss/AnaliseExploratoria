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

# Supondo que as colunas são 'idade' e 'usa_IA' no seu dataframe
idade_usa_ia = round((pd.crosstab(df['idade'], df['usa_IA'], normalize='index') * 100), 2)

# Criar gráfico com seaborn
fig, ax = plt.subplots()
sns.heatmap(idade_usa_ia, annot=True, cmap="YlGnBu", ax=ax)
ax.set_title("Uso de IA por Faixa Etária (%)")
st.pyplot(fig)

### Gráfico 2: Porcentagem de desenvolvedores que usam IA em cada profissão
st.header('Porcentagem de desenvolvedores que usam IA em cada profissão')

# Supondo que as colunas são 'profissao' e 'usa_IA' no seu dataframe
profissao_usa_ia = round((pd.crosstab(df['profissao'], df['usa_IA'], normalize='index') * 100), 2)

# Criar gráfico com seaborn
fig2, ax2 = plt.subplots()
sns.heatmap(profissao_usa_ia, annot=True, cmap="YlOrRd", ax=ax2)
ax2.set_title("Uso de IA por Profissão (%)")
st.pyplot(fig2)

### Gráfico 3: Opinião predominante sobre IA entre desenvolvedores
st.header('Opinião predominante sobre IA entre os desenvolvedores')

# Supondo que a coluna de opinião é 'opiniao_IA' no seu dataframe
opiniao_ia_contagem = df['opiniao_IA'].value_counts()

# Criar gráfico de barras
fig3, ax3 = plt.subplots()
opiniao_ia_contagem.plot(kind='bar', ax=ax3, color="skyblue")
ax3.set_title("Opinião sobre IA")
ax3.set_xlabel("Opinião")
ax3.set_ylabel("Quantidade")
st.pyplot(fig3)
