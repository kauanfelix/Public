import pandas as pd
import streamlit as st
from st_aggrid import AgGrid # pip install streamlit-aggrid


tabela = st.radio("ESCOLHA TABELA:",('PERFIPAR', 'BARBIERI', 'IBEMA ARA','IBEMA TVO','IBEMA EMF'))

if tabela == 'NENHUMA':
    st.write('NENHUMA.')
else:
    st.title(f'TABELA {tabela}')
    planilha = 'Tabelas.xlsx'
    df = pd.read_excel(io=planilha,engine='openpyxl',sheet_name=f'{tabela}')#,nrows=1000, usecols='A:Q')
    AgGrid(data=df)
