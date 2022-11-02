import streamlit as st
import pandas
from streamlit_option_menu import option_menu
import requests
import json


st.set_page_config(page_title="Importações", page_icon=":laptop:", layout="centered")
# with st.sidebar:
#    selected = option_menu(menu_title=None, ["Fornecedores", 'Simulador', 'Importações', 'Gráficos'], icons=['credit-card', 'cash', 'cart', 'bar-chart'], menu_icon="cast", default_index=1)
selected = option_menu(None, ['Fornecedores', 'Simulador', 'Importações', 'Gráficos'],
                       icons=['credit-card', 'cash', 'cart', 'bar-chart'], orientation='horizontal', menu_icon="cast",
                       default_index=1)

if selected == 'Fornecedores':
    st.title(selected)
    st.write("BACKMARKET: [RECONDICIONADOS](https://www.backmarket.com/en-us)")
    st.write("COMPRAS PARAGUAI: [NOVO](https://mobile.comprasparaguai.com.br/)")
    st.write("APPLE: [NOVO](https://www.apple.com/)")

if selected == 'Simulador':
    st.title(selected)
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao.json()
    dolar = st.write(cotacao['USD']['bid'])
    col1, col2 =st.columns(2)
    with col1:
        preco = st.number_input('Preço:', 0, 10000, 50, step=100)
        imposto = st.number_input('Imposto:', 0, 60, 7)
        taxaloja = st.number_input('Taxa Loja:', 0.00, 4.99, 2.99, 1.00)
        resultado = ((imposto / 100) * preco + preco)
        st.info(f'U$ {resultado + taxaloja}')
    with col2:
        input_cotacao = st.number_input('Câmbio Dólar:', 4.50, 5.50, f'{dolar}', 0.01)
        input_spread = st.number_input('Spread:', 0.0, 5.0, 0.99)
        input_iof = st.number_input('Iof:', 1.0, 6.39, 1.1, 5.28)
        spread = (input_cotacao * (input_spread / 100)) + input_cotacao
        iof = (spread * (input_iof / 100)) + spread
        total = st.info(f'R$ {iof * resultado}')
        st.write(iof)
if selected == 'Importações':
    st.title(selected)
    st.write(
        "GOOGLE PLANILHA: [REGISTROS](https://docs.google.com/spreadsheets/d/1PwVx36z6Anr2PpsTLKt24wBGuCaT4GShj3aUdoa9u4I/edit#gid=0)")
