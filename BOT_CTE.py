import pandas as pd
import pyautogui
import time
xgestran = 220
ygestran = 1060
xcampoplaca = 316
ycampoplaca = 217
xcampovalor = 1155
ycampovalor = 216
rafitec = 4763
seg = 1.5
seg2 = 5
# tabela
planilha = pd.read_excel('C:/ROBOCTE.xlsx')
# filtros da tabela
tabela = planilha.loc[planilha['Unnamed: 1'] == 'ok']
# listar de acordo com que foi filtrado
variaveis = tabela[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']].values.tolist()
pyautogui.click(x=xgestran, y=ygestran)
time.sleep(seg2)
#aviso
qtdnfe = (tabela['Unnamed: 5'] [0])
totalnfe = (tabela['Unnamed: 5'] [1])   
pyautogui.alert(f'''Proceder inclusão {qtdnfe} totalizando {totalnfe}''')

#gestran
for repita in variaveis:
    nfe = int(repita[0])  # Unnamed: 2
    valor = repita[1]  # Unnamed: 3
    placa = repita[2]  # Unnamed: 4
    # Emitir conhecimento
    pyautogui.hotkey('alt', 'i')
    pyautogui.press('tab')
    pyautogui.hotkey('alt', 's')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write(f'{nfe}')
    time.sleep(seg)
    for clica in range(2):
        pyautogui.press('tab')
    pyautogui.write(f'{rafitec}')
    time.sleep(seg)
    pyautogui.hotkey('alt', 't')
    time.sleep(seg)
    for clica in range(8):
        pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.press('enter')
    time.sleep(seg)
    # aqui será feita escolha do caminhão
    pyautogui.hotkey('alt', 'd')
    time.sleep(seg)
    pyautogui.doubleClick(x=xcampoplaca, y=ycampoplaca)
    time.sleep(seg)
    pyautogui.press('Delete')
    time.sleep(seg)
    pyautogui.write(f'{placa}')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    # aqui será feita a escolha da unidade de negócio dentro de contrações
    pyautogui.hotkey('alt', 'e')
    time.sleep(seg)
    pyautogui.press('Enter')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'a')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write("R")
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.click(x=xcampovalor, y=ycampovalor)
    time.sleep(seg)
    pyautogui.write(f'{valor}')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'c')
    time.sleep(seg)
    # aqui será feita a gravação e impressão
    pyautogui.hotkey('alt', 'r')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'g')
    time.sleep(seg2)
    pyautogui.hotkey('alt', 'p')
    time.sleep(seg2)
    pyautogui.hotkey('alt', 'i')
    time.sleep(30)
    pyautogui.press('Enter')
    time.sleep(30)
pyautogui.alert(f'''Processo finalizado''')