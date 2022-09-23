import pandas as pd
import pyautogui
import time
xgestran = 120
ygestran = 740
seg = 0.4
seg2 =2.5
# tabela
planilha = pd.read_excel('C:/Users/Usuario/Desktop/ROBOCADASTRO.xlsx')
# filtros da tabela
tabela = planilha.loc[planilha['Unnamed: 1'] == 'ok']
# listar de acordo com que foi filtrado
variaveis = tabela[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8',
                'Unnamed: 9']].values.tolist()
pyautogui.click(x=xgestran, y=ygestran)
time.sleep(seg2)
# e-mail
for repita in variaveis:
    codsuperior = int(repita[0]) # Unnamed: 2
    mascara = int(repita[1])  # Unnamed: 3
    descricao = str(repita[2])  # Unnamed: 4
    resumo = int(repita[3])  # Unnamed: 5
    natureza = int(repita[4])  # Unnamed: 6
    tipo = int(repita[5])  # Unnamed: 7
    analise = int(repita[6])  # Unnamed: 8
    despesa = int(repita[7])  # Unnamed: 9
    pyautogui.hotkey('alt', 'i')
    time.sleep(seg)
    pyautogui.write(f'''{codsuperior}''')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    for tecle in range(10):
        pyautogui.press('backspace')
    time.sleep(seg)
    pyautogui.write(f'''{mascara}''')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write(f'''{descricao}''')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write(f'''{resumo}''')
    time.sleep(seg)
    pyautogui.press('tab')
    pyautogui.write(f'''{natureza}''')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write(f'''{tipo}''')
    time.sleep(seg)
    for clica in range(5):
        pyautogui.press('tab')
        time.sleep(seg)
    pyautogui.write(f'''{analise}''')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write(f'''{despesa}''')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'g')
    time.sleep(seg2)
pyautogui.alert('Cadastrado 1 Categorias')