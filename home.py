import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Importações", page_icon=":laptop:", layout="centered")

#with st.sidebar:
selected = option_menu(None, ["Fornecedores", 'Simulador', 'Importações'], icons=['credit-card', 'cash', 'cart'], orientation="horizontal", menu_icon="cast", default_index=1)

    
if selected == 'Fornecedores':
    st.title(selected)
    st.write("BACKMARKET: [RECONDICIONADOS](https://www.backmarket.com/en-us)")
    st.write("COMPRAS PARAGUAI: [NOVO](https://mobile.comprasparaguai.com.br/)")
    st.write("APPLE: [NOVO](https://www.apple.com/)")
    
if selected == 'Simulador':
    st.title(selected)
    preco = st.number_input('Preço:', 1, 10000, step=100)
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

