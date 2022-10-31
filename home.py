import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import time
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,)

tab1, tab2, tab3 = st.tabs(['Simulador importação', 'Fornecedores', 'Registro Importações'])

with tab1:
    st.title('Simulador importação')
    preco = st.number_input('Preço:', 1, 999, step=1)
    imposto = st.number_input('Imposto:', 0, 60, 7)
    taxaloja = st.number_input('Taxa Loja:', 0.00, 4.99, 2.99, 1.00)
    resultado = ((imposto / 100) * preco + preco)
    input_cotacao = st.number_input('Câmbio Dólar:', 4.50, 5.50, 5.00, 0.01)
    input_spread = st.number_input('Spread:', 0.0, 5.0, 1.0)
    input_iof = st.number_input('Iof:', 1.0, 6.39, 1.1, 5.28)
    spread = (input_cotacao * (input_spread / 100)) + input_cotacao
    iof = (spread * (input_iof / 100)) + spread
    st.write(iof)
    st.info(f'U$ {resultado + taxaloja}')
    total = st.info(f'R$ {iof * resultado}')
    peso = st.slider('Peso:', 100, 2000, step=100)
    kg = st.slider('Preço KG:', 26.50, 27.50, 27.50, 0.50)
    aduana = st.slider('Aduana:', 0, 40, 20, 5)
    #redespacho = st.info(f'U$ {(kg * peso}')
    #st.write(redespacho)
    #st.info(f'R$ {iof * redespacho}')

with tab2:
    st.write("BACKMARKET: [RECONDICIONADOS](https://www.backmarket.com/en-us)")

with tab3:
    df = pd.read_excel(io='C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx',engine='openpyxl',sheet_name="MOTORISTAS")
    st.dataframe(df)

