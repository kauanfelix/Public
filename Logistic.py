import pandas as pd
import streamlit as st
from PIL import Image # pip install pil
from openpyxl import load_workbook # pip install pil openpyxl
# from st_aggrid import AgGrid, GridOptionsBuilder  # pip install streamlit-aggrid

# configurações navegador
caminho_icone = 'C:/Users/admin/OneDrive/Nuvem-Kauan/IconeRb.ico'
icone = Image.open(caminho_icone)
st.set_page_config(page_title="RODOBROTTO SISTEMAS", page_icon=icone, layout="wide")
# sidebar
st.sidebar.title(f'TABELAS')
tabela = st.sidebar.radio("ESCOLHA TABELA:",('PERFIPAR', 'BARBIERI', 'IBEMA ARA','IBEMA TVO','IBEMA EMF'))

if tabela == 'PERFIPAR':
    planilha = 'Logistic.xlsx'
    st.header(f'{tabela}')
    df = pd.read_excel(io=planilha,engine='openpyxl',sheet_name=f'{tabela}')#,nrows=1000, usecols='A:Q')
    st.dataframe(data=df,)

    col1, col2, = st.columns(2)
    total_frete = col1.number_input('VALOR TOTAL FRETE:', step=1000, min_value=0)
    quantidade_notas = col2.number_input(label='QUANTIDADE NOTAS:', value=1, min_value=1, max_value=10, step=1)
    st.markdown('---')
    st.subheader(body=f'DILUIÇÃO POR PESO:')
    if quantidade_notas == 1:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)

        total_peso = nota1

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')
    if quantidade_notas == 2:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)
        nota2 = st.sidebar.number_input(label='PESO NOTA 2:', value=0, min_value=0, step=1)

        total_peso = nota1 + nota2

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))
        col2.text('VALOR NOTA 2:');
        valor2 = col2.code(((total_frete / total_peso) * nota2) + 150)

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')
    if quantidade_notas == 3:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)
        nota2 = st.sidebar.number_input(label='PESO NOTA 2:', value=0, min_value=0, step=1)
        nota3 = st.sidebar.number_input(label='PESO NOTA 3:', value=0, min_value=0, step=1)

        total_peso = nota1 + nota2 + nota3
        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))
        col2.text('VALOR NOTA 2:');
        valor2 = col2.code(((total_frete / total_peso) * nota2) + 150)
        col3.text('VALOR NOTA 3:');
        valor3 = col3.code(((total_frete / total_peso) * nota3) + 150)

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')
    if quantidade_notas == 4:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)
        nota2 = st.sidebar.number_input(label='PESO NOTA 2:', value=0, min_value=0, step=1)
        nota3 = st.sidebar.number_input(label='PESO NOTA 3:', value=0, min_value=0, step=1)
        nota4 = st.sidebar.number_input(label='PESO NOTA 4:', value=0, min_value=0, step=1)

        total_peso = nota1 + nota2 + nota3 + nota4

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))
        col2.text('VALOR NOTA 2:');
        valor2 = col2.code(((total_frete / total_peso) * nota2) + 150)
        col3.text('VALOR NOTA 3:');
        valor3 = col3.code(((total_frete / total_peso) * nota3) + 150)
        col4.text('VALOR NOTA 4:');
        valor4 = col4.code(((total_frete / total_peso) * nota4) + 150)

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')
    if quantidade_notas == 5:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)
        nota2 = st.sidebar.number_input(label='PESO NOTA 2:', value=0, min_value=0, step=1)
        nota3 = st.sidebar.number_input(label='PESO NOTA 3:', value=0, min_value=0, step=1)
        nota4 = st.sidebar.number_input(label='PESO NOTA 4:', value=0, min_value=0, step=1)
        nota5 = st.sidebar.number_input(label='PESO NOTA 5:', value=0, min_value=0, step=1)

        total_peso = nota1 + nota2 + nota3 + nota4 + nota5

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))
        col2.text('VALOR NOTA 2:');
        valor2 = col2.code(((total_frete / total_peso) * nota2) + 150)
        col3.text('VALOR NOTA 3:');
        valor3 = col3.code(((total_frete / total_peso) * nota3) + 150)
        col4.text('VALOR NOTA 4:');
        valor4 = col4.code(((total_frete / total_peso) * nota4) + 150)
        col5.text('VALOR NOTA 5:');
        valor5 = col5.code(((total_frete / total_peso) * nota5) + 150)

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')
    if quantidade_notas == 6:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)
        nota2 = st.sidebar.number_input(label='PESO NOTA 2:', value=0, min_value=0, step=1)
        nota3 = st.sidebar.number_input(label='PESO NOTA 3:', value=0, min_value=0, step=1)
        nota4 = st.sidebar.number_input(label='PESO NOTA 4:', value=0, min_value=0, step=1)
        nota5 = st.sidebar.number_input(label='PESO NOTA 5:', value=0, min_value=0, step=1)
        nota6 = st.sidebar.number_input(label='PESO NOTA 6:', value=0, min_value=0, step=1)

        total_peso = nota1 + nota2 + nota3 + nota4 + nota5 + nota6

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))
        col2.text('VALOR NOTA 2:');
        valor2 = col2.code(((total_frete / total_peso) * nota2) + 150)
        col3.text('VALOR NOTA 3:');
        valor3 = col3.code(((total_frete / total_peso) * nota3) + 150)
        col4.text('VALOR NOTA 4:');
        valor4 = col4.code(((total_frete / total_peso) * nota4) + 150)
        col5.text('VALOR NOTA 5:');
        valor5 = col5.code(((total_frete / total_peso) * nota5) + 150)
        col1.text('VALOR NOTA 6:');
        valor6 = col1.code(((total_frete / total_peso) * nota6) + 150)

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')
    if quantidade_notas == 7:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)
        nota2 = st.sidebar.number_input(label='PESO NOTA 2:', value=0, min_value=0, step=1)
        nota3 = st.sidebar.number_input(label='PESO NOTA 3:', value=0, min_value=0, step=1)
        nota4 = st.sidebar.number_input(label='PESO NOTA 4:', value=0, min_value=0, step=1)
        nota5 = st.sidebar.number_input(label='PESO NOTA 5:', value=0, min_value=0, step=1)
        nota6 = st.sidebar.number_input(label='PESO NOTA 6:', value=0, min_value=0, step=1)
        nota7 = st.sidebar.number_input(label='PESO NOTA 7:', value=0, min_value=0, step=1)

        total_peso = nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))
        col2.text('VALOR NOTA 2:');
        valor2 = col2.code(((total_frete / total_peso) * nota2) + 150)
        col3.text('VALOR NOTA 3:');
        valor3 = col3.code(((total_frete / total_peso) * nota3) + 150)
        col4.text('VALOR NOTA 4:');
        valor4 = col4.code(((total_frete / total_peso) * nota4) + 150)
        col5.text('VALOR NOTA 5:');
        valor5 = col5.code(((total_frete / total_peso) * nota5) + 150)
        col1.text('VALOR NOTA 6:');
        valor6 = col1.code(((total_frete / total_peso) * nota6) + 150)
        col2.text('VALOR NOTA 7:');
        valor7 = col2.code(((total_frete / total_peso) * nota7) + 150)

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')
    if quantidade_notas == 8:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)
        nota2 = st.sidebar.number_input(label='PESO NOTA 2:', value=0, min_value=0, step=1)
        nota3 = st.sidebar.number_input(label='PESO NOTA 3:', value=0, min_value=0, step=1)
        nota4 = st.sidebar.number_input(label='PESO NOTA 4:', value=0, min_value=0, step=1)
        nota5 = st.sidebar.number_input(label='PESO NOTA 5:', value=0, min_value=0, step=1)
        nota6 = st.sidebar.number_input(label='PESO NOTA 6:', value=0, min_value=0, step=1)
        nota7 = st.sidebar.number_input(label='PESO NOTA 7:', value=0, min_value=0, step=1)
        nota8 = st.sidebar.number_input(label='PESO NOTA 8:', value=0, min_value=0, step=1)

        total_peso = nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))
        col2.text('VALOR NOTA 2:');
        valor2 = col2.code(((total_frete / total_peso) * nota2) + 150)
        col3.text('VALOR NOTA 3:');
        valor3 = col3.code(((total_frete / total_peso) * nota3) + 150)
        col4.text('VALOR NOTA 4:');
        valor4 = col4.code(((total_frete / total_peso) * nota4) + 150)
        col5.text('VALOR NOTA 5:');
        valor5 = col5.code(((total_frete / total_peso) * nota5) + 150)
        col1.text('VALOR NOTA 6:');
        valor6 = col1.code(((total_frete / total_peso) * nota6) + 150)
        col2.text('VALOR NOTA 7:');
        valor7 = col2.code(((total_frete / total_peso) * nota7) + 150)
        col3.text('VALOR NOTA 8:');
        valor8 = col3.code(((total_frete / total_peso) * nota8) + 150)

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')
    if quantidade_notas == 9:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)
        nota2 = st.sidebar.number_input(label='PESO NOTA 2:', value=0, min_value=0, step=1)
        nota3 = st.sidebar.number_input(label='PESO NOTA 3:', value=0, min_value=0, step=1)
        nota4 = st.sidebar.number_input(label='PESO NOTA 4:', value=0, min_value=0, step=1)
        nota5 = st.sidebar.number_input(label='PESO NOTA 5:', value=0, min_value=0, step=1)
        nota6 = st.sidebar.number_input(label='PESO NOTA 6:', value=0, min_value=0, step=1)
        nota7 = st.sidebar.number_input(label='PESO NOTA 7:', value=0, min_value=0, step=1)
        nota8 = st.sidebar.number_input(label='PESO NOTA 8:', value=0, min_value=0, step=1)
        nota9 = st.sidebar.number_input(label='PESO NOTA 9:', value=0, min_value=0, step=1)

        total_peso = nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))
        col2.text('VALOR NOTA 2:');
        valor2 = col2.code(((total_frete / total_peso) * nota2) + 150)
        col3.text('VALOR NOTA 3:');
        valor3 = col3.code(((total_frete / total_peso) * nota3) + 150)
        col4.text('VALOR NOTA 4:');
        valor4 = col4.code(((total_frete / total_peso) * nota4) + 150)
        col5.text('VALOR NOTA 5:');
        valor5 = col5.code(((total_frete / total_peso) * nota5) + 150)
        col1.text('VALOR NOTA 6:');
        valor6 = col1.code(((total_frete / total_peso) * nota6) + 150)
        col2.text('VALOR NOTA 7:');
        valor7 = col2.code(((total_frete / total_peso) * nota7) + 150)
        col3.text('VALOR NOTA 8:');
        valor8 = col3.code(((total_frete / total_peso) * nota8) + 150)
        col4.text('VALOR NOTA 9:');
        valor9 = col4.code(((total_frete / total_peso) * nota9) + 150)

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')
    if quantidade_notas == 10:
        nota1 = st.sidebar.number_input(label='PESO NOTA 1:', value=1, min_value=0, step=1)
        nota2 = st.sidebar.number_input(label='PESO NOTA 2:', value=0, min_value=0, step=1)
        nota3 = st.sidebar.number_input(label='PESO NOTA 3:', value=0, min_value=0, step=1)
        nota4 = st.sidebar.number_input(label='PESO NOTA 4:', value=0, min_value=0, step=1)
        nota5 = st.sidebar.number_input(label='PESO NOTA 5:', value=0, min_value=0, step=1)
        nota6 = st.sidebar.number_input(label='PESO NOTA 6:', value=0, min_value=0, step=1)
        nota7 = st.sidebar.number_input(label='PESO NOTA 7:', value=0, min_value=0, step=1)
        nota8 = st.sidebar.number_input(label='PESO NOTA 8:', value=0, min_value=0, step=1)
        nota9 = st.sidebar.number_input(label='PESO NOTA 9:', value=0, min_value=0, step=1)
        nota10 = st.sidebar.number_input(label='PESO NOTA 10:', value=0, min_value=0, step=1)

        total_peso = nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.text('VALOR NOTA 1:');
        valor1 = col1.code(((total_frete / total_peso) * nota1))
        col2.text('VALOR NOTA 2:');
        valor2 = col2.code(((total_frete / total_peso) * nota2) + 150)
        col3.text('VALOR NOTA 3:');
        valor3 = col3.code(((total_frete / total_peso) * nota3) + 150)
        col4.text('VALOR NOTA 4:');
        valor4 = col4.code(((total_frete / total_peso) * nota4) + 150)
        col5.text('VALOR NOTA 5:');
        valor5 = col5.code(((total_frete / total_peso) * nota5) + 150)
        col1.text('VALOR NOTA 6:');
        valor6 = col1.code(((total_frete / total_peso) * nota6) + 150)
        col2.text('VALOR NOTA 7:');
        valor7 = col2.code(((total_frete / total_peso) * nota7) + 150)
        col3.text('VALOR NOTA 8:');
        valor8 = col3.code(((total_frete / total_peso) * nota8) + 150)
        col4.text('VALOR NOTA 9:');
        valor9 = col4.code(((total_frete / total_peso) * nota9) + 150)
        col5.text('VALOR NOTA 10:');
        valor10 = col5.code(((total_frete / total_peso) * nota10) + 150)

        st.subheader(body=f'PESO TOTAL: {total_peso}')
        st.markdown('---')

else:
    planilha = 'Logistic.xlsx'
    st.header(f'{tabela}')
    df = pd.read_excel(io=planilha,engine='openpyxl',sheet_name=f'{tabela}')
    st.dataframe(df)
    #AgGrid(data=df, fit_columns_on_grid_load=True,)
