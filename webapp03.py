# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import plotly.graph_objects as go

import altair as alt
from urllib.error import URLError

r = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTcZCtGN-r35mPV_i1n-K1mQR6u6stcBNbynSz7vCujCOzJ22w9-gGTTO3Bb8Rm6pj-7JqChQf9Evaq/pub?gid=958030580&single=true&output=csv')
data = r.content
df = pd.read_csv(BytesIO(data), index_col=0)
df.columns = ['e-mail', 'equipe', 'nome', 'duvida', 'obs']
nREGISTROS = len(df)
print(nREGISTROS)
indice = list(range(0, nREGISTROS))

image01 = Image.open('desenvolvimento.jpg')
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title(" 1ª EDIÇÃO DO DESAFIO HACKATHON: MACKENZIE WEEK CAMPINAS - LOGITHINK.IT 2022")
st.header("PAINEL DE ACOMPANHAMENTO PARA OS TUTORES CCT")
# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app

# Use st.write("") para adicionar um texto ao seu Web app
#st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")
st.subheader("------ **Desenvolvido por: Massaki de O. Igarashi** -----")

menu = ["Saldo_ESTOQUE",
        "Análise de Dados",
        # "Texto_Colunas",
        # "Texto_Markdown",
        # "Inserir_Figura"
        ]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.write("Texto Side Bar")

if choice == "Saldo_ESTOQUE": 
    st.header("Saldo em ESTOQUE")
    st.subheader("Fonte: Google Forms em https://forms.gle/ofUVkwswMGGUBJms5")
    st.markdown(
    """
    Analise de Dados de Estoque
    """)

    a1, a2 = st.columns((1,1))
    with a1:
        st.subheader("Saldo atual em estoque = ")
    with a2:
        st.info(saldo)  
elif choice == "Texto_Colunas":       
    st.subheader("Texto formatado em colunas")
    st.write("Veja a seguir uma opção de formatação em colunas")    
    cols01 = st.columns(2)    
    cols01[0].write('Texto da Coluna 01')
    cols01[1].write('Texto da Coluna 02')
elif choice == "Texto_Markdown":
    st.subheader("Texto Markdown")
    st.write("Veja a seguir opção de formatação de texto Markdown")
    st.markdown(
    """
    ## *Alguns sites referências*:    
    - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
    - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
    - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 2 | ?h | ? a ?
    Dia 2 de 2 | ?h | ? a ?
    """
    )
elif choice == "Inserir_Figura":
    st.image(image01, width=800, caption='Rótulo da Imagem 01') 
    
