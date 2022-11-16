import time
import pyautogui
import streamlit as st

st.warning('Após clicar no botão terá 4 segundos para posicionar o mouse!')
if st.button('Cordenadas'):
    segundos = 4
    time.sleep(segundos)
    x, y = pyautogui.position()
    st.info(f'Posicao atual do mouse:\n x = {x} y = {y}')