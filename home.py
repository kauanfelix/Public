import streamlit as st
import pandas as pd
from openpyxl import load_workbook
import time
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,)

tab1, tab2, tab3, tab4, tab5, tab6  = st.tabs(['Multas', 'Placas', 'Motoristas', 'Infrações', 'Locais', 'Consultar'])

with tab1:
    def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        modify = st.checkbox('Adicione filtros')
        if not modify:
            return df
        df = df.copy()
        for col in df.columns:
            if is_object_dtype(df[col]):
                try:
                    df[col] = pd.to_datetime(df[col])
                except Exception:
                    pass
            if is_datetime64_any_dtype(df[col]):
                df[col] = df[col].dt.tz_localize(None)
        modification_container = st.container()
        with modification_container:
            to_filter_columns = st.multiselect('Filter dataframe on', df.columns)
            for column in to_filter_columns:
                left, right = st.columns((1, 20))
                left.write('↳')
                # Treat columns with < 10 unique values as categorical
                if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                    user_cat_input = right.multiselect(f'Valores da coluna {column}',df[column].unique(),default=list(df[column].unique()),)
                    df = df[df[column].isin(user_cat_input)]
                elif is_numeric_dtype(df[column]):
                    _min = float(df[column].min())
                    _max = float(df[column].max())
                    step = (_max - _min) / 100
                    user_num_input = right.slider(f'Values for {column}',_min,_max,(_min, _max),step=step,)
                    df = df[df[column].between(*user_num_input)]
                elif is_datetime64_any_dtype(df[column]):
                    user_date_input = right.date_input(f'Values for {column}',value=(df[column].min(),df[column].max(),),)
                    if len(user_date_input) == 2:
                        user_date_input = tuple(map(pd.to_datetime, user_date_input))
                        start_date, end_date = user_date_input
                        df = df.loc[df[column].between(start_date, end_date)]
                else:
                    user_text_input = right.text_input(f'Substring or regex in {column}',)
                    if user_text_input:
                        df = df[df[column].str.contains(user_text_input, na=False)]
        return df
    df = pd.read_excel(io='C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx',engine='openpyxl',sheet_name='DADOS',usecols='A:P',nrows=1000)
    st.dataframe(filter_dataframe(df))

with tab2:
    funcao = st.radio('Selecione:',('Cadastrar', 'Atualizar', 'Excluir'))
    if funcao == 'Cadastrar':
        placa = st.text_input('Digite a placa:', max_chars=7)
        renavam = st.number_input('Digite o renavam:', step=1)
        if st.button('Cadastrar veículo'):
            with st.spinner(text='Cadastrando'):
                time.sleep(2)
                wb = load_workbook('C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx')
                ws = wb['PLACAS']
                ws = wb.active
                to_append = ['ATIVO', placa, renavam,]
                ws.append(to_append)
                wb.save('C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx')
        df = pd.read_excel(io='C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx', engine='openpyxl', sheet_name='PLACAS')
        st.table(df)
    if funcao == 'Excluir':
        df = pd.read_excel(io='C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx', engine='openpyxl', sheet_name='PLACAS')
        excluir = st.selectbox('SELECIONE PLACA:', options=df['Placa'].unique())
        if st.button('Excluir veículo'):
            with st.spinner(text='Excluindo'):
                time.sleep(2)
                wb = load_workbook('C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx')
                ws = wb['PLACAS']
                ws = wb.active
                for CELULA in ws['B']:
                    if CELULA.value == excluir:
                        LINHA = CELULA.row
                        ws.delete_rows(LINHA)
                        wb.save('C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx')
        df = pd.read_excel(io='C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx', engine='openpyxl', sheet_name='PLACAS')
        st.table(df)
    if funcao == 'Atualizar':
        df = pd.read_excel(io='C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx', engine='openpyxl', sheet_name='PLACAS')
        atualizar = st.selectbox('Selecione placa:', options=df['Placa'].unique())
        status = st.selectbox('Selecione status:', options=['DESATIVADO', 'ATIVO'])
        if st.button('Atualizar veículo'):
            with st.spinner(text='Atualizando'):
                time.sleep(2)
                wb = load_workbook('C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx')
                ws = wb['PLACAS']
                ws = wb.active
                for CELULA in ws['B']:
                    if CELULA.value == atualizar:
                        LINHA = CELULA.row
                        ws[f'A{LINHA}'] = status
                        wb.save('C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx')
        df = pd.read_excel(io='C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx', engine='openpyxl', sheet_name='PLACAS')
        st.table(df)

with tab3:
    df = pd.read_excel(io='C:/Users/admin/PycharmProjects/pythonProject/testes.xlsx',engine='openpyxl',sheet_name="MOTORISTAS")
    st.dataframe(df)