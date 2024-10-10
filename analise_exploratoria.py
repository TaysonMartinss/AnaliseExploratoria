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

def load_data2():
    url2 = 'https://raw.githubusercontent.com/TaysonMartinss/AnaliseExploratoria/refs/heads/main/dataframe_tratado.csv'
    df2 = pd.read_csv(url2)
    return df2


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
    plt.figure(figsize=(6, 4.1))
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


def idade_ia():
        df2 = load_data2()
        idade_df2 = df2['Age']
        usa_IA_df2 = df2['AISelect']
        idade_usa_ia = pd.crosstab(idade_df2, usa_IA_df2, normalize='index') * 100
        plt.figure(figsize=(10, 6.3))
        sns.heatmap(idade_usa_ia, annot=True, cmap='coolwarm', fmt='.1f', cbar_kws={'label': 'Porcentagem'})
        plt.title('Distribuição Percentual de Usuários de IA por Idade')
        plt.xlabel('Usa IA')
        plt.ylabel('Idade')
        st.pyplot(plt)

def plot_tamanho_empresa_usa_ia_df2():
    df2 = load_data2()
    tamanho_empresa_df2 = df2['OrgSize']
    usa_IA_df2 = df2['AISelect']
    tamanho_empresa_usa_ia = round((pd.crosstab(tamanho_empresa_df2, usa_IA_df2, normalize='index') * 100), 2)
    plt.figure(figsize=(12, 12))
    tamanho_empresa_usa_ia.plot(kind='bar', stacked=False)
    plt.title('Correlação entre Tamanho da Empresa e Adoção de Ferramentas de IA (df2)')
    plt.xlabel('Tamanho da Empresa')
    plt.ylabel('Porcentagem (%)')
    plt.legend(title='Usa IA?')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

def plot_profissao_usa_ia_df2():
    df2 = load_data2()
    profissao_df2 = df2['MainBranch']
    usa_IA_df2 = df2['AISelect']
    profissao_usa_ia = round((pd.crosstab(profissao_df2, usa_IA_df2, normalize='index') * 100), 2)
    plt.figure(figsize=(10, 6))
    profissao_usa_ia.plot(kind='bar')
    plt.title('Porcentagem de desenvolvedores que usam IA por Profissão (df2)')
    plt.xlabel('Profissão')
    plt.ylabel('Porcentagem (%)')
    plt.legend(title='Usa IA?')
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

    with col23:
        idade_ia()

    coll32, col33 = st.columns(2)
    with coll32:
        plot_tamanho_empresa_usa_ia_df2()
    with col33:
      plot_profissao_usa_ia_df2()

elif selected_option == "Insights":

    st.markdown("""
            <div style="background-color: #333; padding: 15px; border-radius: 10px;">
                <h3 style="color: #f5f5f5;">Análise da Relação entre IA e Linguagens de Programação</h3>
                <p><strong>Dominância do Python:</strong> O Python se destaca como a linguagem mais popular entre as diversas IAs, sendo amplamente utilizada em projetos de IA devido à sua sintaxe clara, grande quantidade de bibliotecas e frameworks dedicados à IA (como TensorFlow, PyTorch e scikit-learn), e comunidade ativa.</p>
                <p><strong>JavaScript e TypeScript:</strong> Essas linguagens, principalmente utilizadas em desenvolvimento web, também possuem uma presença significativa, indicando a crescente integração de IA em aplicações web e interfaces.</p>
                <p><strong>SQL:</strong> A linguagem SQL, embora associada a bancos de dados, é fundamental para o trabalho com grandes volumes de dados, que são a base para o treinamento de modelos de IA.</p>
                <p><strong>Outras linguagens:</strong> Linguagens como C# e Java também são utilizadas, especialmente em ambientes corporativos e projetos de grande escala.</p>
            </div>
        """, unsafe_allow_html=True)

    st.text("")
    st.markdown("""
                <div style="background-color: #333; padding: 15px; border-radius: 10px;">
                    <h3 style="color: #f5f5f5;">Analisando o Uso de IA por Faixa Etária:</h3>
                    <p><strong>Adoção Massiva:</strong> É evidente uma alta taxa de adoção de ferramentas de IA em todas as faixas etárias. Isso indica uma rápida integração dessas tecnologias no dia a dia dos desenvolvedores, independentemente de sua experiência.</p>
                    <p><strong>Jovens à Frente:</strong>faixa etária entre 18 e 24 anos apresenta a maior taxa de uso, o que é esperado, já que essa geração cresceu imersa em tecnologias digitais e tem maior familiaridade com ferramentas inovadoras.</p>
                    <p><strong>Curva de Adoção Constante:</strong> À medida que a idade aumenta, observa-se uma leve diminuição na taxa de uso, mas a tendência geral é de alta adoção em todas as faixas etárias. Isso sugere que a IA está sendo adotada por profissionais de todas as gerações.</p>
                </div>
            """, unsafe_allow_html=True)

    st.text("")

    df2 = load_data2()

    usa_IA_df = df2['AISelect']
    porcentagem_usa_ia = round((usa_IA_df.value_counts(normalize=True) * 100), 2)


    porcentagem_ia_text = ""
    for key, value in porcentagem_usa_ia.items():
        porcentagem_ia_text += f"<strong>{key}:</strong> {value}%<br>"

    st.markdown(f"""
            <div style="background-color: #333; padding: 15px; border-radius: 10px;">
                <h3 style="color: #f5f5f5;">Utilização de IA no último ano? </h3>
                <p><strong>Porcentagem de Utilização de IA:</strong><br>{porcentagem_ia_text}</p>
            </div>
        """, unsafe_allow_html=True)

elif selected_option == "DATASET":
    st.title("Visualização dos Datasets")
    df1 = load_data()
    df2 = load_data2()
    st.subheader("Dataset 1 - df_tratado.csv")
    st.write("Visualizando o dataset 1 completo:")
    st.dataframe(df1)
    st.subheader("Dataset 2 - dataframe_tratado.csv")
    st.write("Visualizando o dataset 2 completo:")
    st.dataframe(df2)

