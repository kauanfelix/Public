import streamlit as st
from streamlit_option_menu import option_menu
import requests
import pandas as pd

st.set_page_config(page_title="Gestão", page_icon=":bar-chart:", layout="centered")
# with st.sidebar:
#    selected = option_menu(menu_title=None, ["Fornecedores", 'Simulador', 'Importações', 'Gráficos'], icons=['credit-card', 'cash', 'cart', 'bar-chart'], menu_icon="cast", default_index=1)
selected = option_menu(None, [ 'Financeiro', 'Importações'],
                       icons=['cash', 'cart'], orientation='horizontal', menu_icon="cast",
                       default_index=1)

if selected == 'Financeiro':
    st.title(selected)
    df = pd.read_excel(io='debitos.xlsx', engine='openpyxl', sheet_name='DEBITOS', skiprows=0, usecols='A:C',nrows=100)


if selected == 'Importações':
    st.title(selected)
    st.markdown('---')
    st.subheader('Fornecedores')
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao.json()
    st.sidebar.text('DOLAR HOJE')
    dolar = st.sidebar.write(cotacao['USD']['bid'])
    st.write("BACKMARKET: [RECONDICIONADOS](https://www.backmarket.com/en-us)")
    st.write("COMPRAS PARAGUAI: [NOVO](https://mobile.comprasparaguai.com.br/)")
    st.write("APPLE: [NOVO](https://www.apple.com/)")
    st.markdown('---')
    st.subheader('Simular')
    col1, col2 = st.columns(2)
    with col1:
        preco = st.number_input('Preço:', 0, 10000, 1000, step=100)
        imposto = st.number_input('Imposto:', 0, 60, 7)
        taxaloja = st.number_input('Taxa Loja:', 0.00, 4.99, 2.99, 1.00)
        resultado = ((imposto / 100) * preco + preco)
        st.info(f'U$ {resultado + taxaloja}')
    with col2:
        input_cotacao = st.number_input('Câmbio Dólar:', 4.50, 5.50, 5.10, 0.01)
        input_spread = st.number_input('Spread:', 0.0, 5.0, 0.99)
        input_iof = st.number_input('Iof:', 1.0, 6.39, 1.1, 5.28)
        spread = (input_cotacao * (input_spread / 100)) + input_cotacao
        iof = (spread * (input_iof / 100)) + spread
        total = st.info(f'R$ {iof * resultado}')
        st.write(iof)
    st.markdown('---')
    st.subheader('Registros')
    st.write("GOOGLE PLANILHA: [REGISTROS](https://docs.google.com/spreadsheets/d/1PwVx36z6Anr2PpsTLKt24wBGuCaT4GShj3aUdoa9u4I/edit#gid=0)")
    st.markdown('---')



