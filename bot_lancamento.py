import pandas as pd
import pyautogui
import time
xgestran = 121
ygestran = 741
seg = 1.5
# tabela
planilha = pd.read_excel(io='BOT.xlsx', engine='openpyxl', sheet_name='LER_ABA')
# filtros da tabela
tabela = planilha.loc[planilha['Unnamed: 1'] == 'ok']
# listar de acordo com que foi filtrado
variaveis = tabela[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11']].values.tolist()
pyautogui.click(x=xgestran, y=ygestran)
time.sleep(2)
pyautogui.alert(f'Gestran foi aberto? Pressione Ok se SIM')

for repita in variaveis:
    coluna2 = int(repita[0])  # Unnamed: 2
    coluna3 = int(repita[1])  # Unnamed: 3
    coluna4 = int(repita[2])  # Unnamed: 4
    coluna5 = int(repita[3])  # Unnamed: 5
    coluna6 = int(repita[4])  # Unnamed: 6
    coluna7 = (repita[5])  # Unnamed: 7
    coluna8 = int(repita[6])  # Unnamed: 8
    coluna9 = str(repita[7])  # Unnamed: 9
    coluna10 = str(repita[8])  # Unnamed: 10
    coluna11 = int(repita[9])  # Unnamed: 11

    pyautogui.hotkey('alt', 'i')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'i')
    time.sleep(seg)
    pyautogui.write(f'{coluna2}')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write(f'{coluna3}')
    time.sleep(seg)
    pyautogui.press('tab')
    pyautogui.write(f'{coluna4}')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write(f'{coluna5}')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write('22')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write(f'{coluna6}')
    time.sleep(seg)
    pyautogui.press('Delete')
    time.sleep(seg)
    pyautogui.press('Delete')
    time.sleep(seg)
    for clica in range(6):
        pyautogui.press('tab')
    pyautogui.write(f'{coluna7}')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'c')
    time.sleep(seg)
    pyautogui.hotkey('alt', 's')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'i')
    pyautogui.write(f'{coluna8}')
    time.sleep(seg)
    for clica in range(7):
        pyautogui.press('tab')
    pyautogui.write('1')
    time.sleep(seg)
    for clica in range(11):
        pyautogui.press('tab')
    pyautogui.hotkey('alt', 'down')
    time.sleep(seg)
    pyautogui.write(f'{coluna9}')
    time.sleep(seg)
    pyautogui.press('Enter')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.press('tab')
    # pyautogui.hotkey('alt', 'down')
    # time.sleep(seg)
    pyautogui.write(f'{coluna11}')
    time.sleep(seg)
    pyautogui.press('Enter')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'c')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'g')
    time.sleep(5)
pyautogui.alert(f'Processo finalizado')