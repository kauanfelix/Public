import pandas as pd
import pyautogui
import time
xgestran = 120; ygestran = 740
yempresa = 336; xempresa = 276
seg = 0.4; seg2 = 2.5809
# tabela
planilha = pd.read_excel('C:/Users/Usuario/Desktop/TABELA.xlsx')
# filtros da tabelalocal
tabela = planilha.loc[planilha['Unnamed: 1'] == 'OK']
# listar de acordo com que foi filtrado
variaveis = tabela[['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']].values.tolist()#, 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'
# abrir gestran
pyautogui.click(x=xgestran, y=ygestran)
time.sleep(seg2)
pyautogui.alert('Leitura feita com Sucesso, Gestran está aberto na tabela')
# processo
for repita in variaveis:
    codempresa = int(repita[0])  # Unnamed: 4
    cidadeouestado = str(repita[1]) # Unnamed: 3
    truck = int(repita[2])  # Unnamed: 4
    bitruck = int(repita[3])  # Unnamed: 5
    carreta = int(repita[4])  # Unnamed: 6
    pyautogui.hotkey('alt', 'i')
    time.sleep(seg)
    pyautogui.click(x=xempresa, y=yempresa)
    time.sleep(seg)
    for tecle in range(6):
        pyautogui.press('delete')
        time.sleep(seg)
    pyautogui.write('local')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.write(f'''{codempresa}''')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'down')
    time.sleep(seg)
    pyautogui.write('cidade')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'down')
    time.sleep(seg)
    pyautogui.write(f'''{cidadeouestado}''')
    time.sleep(seg)
    pyautogui.press('enter')
    time.sleep(seg)
    pyautogui.press('tab')
    time.sleep(seg)
    pyautogui.press('space')
    time.sleep(seg)
    pyautogui.write(f'''{truck}''')
    time.sleep(seg)
    pyautogui.press('down')
    time.sleep(seg)
    pyautogui.press('space')
    time.sleep(seg)
    pyautogui.write(f'''{bitruck}''')
    time.sleep(seg)
    pyautogui.press('down')
    time.sleep(seg)
    pyautogui.press('space')
    time.sleep(seg)
    pyautogui.write(f'''{carreta}''')
    time.sleep(seg)
    pyautogui.hotkey('alt', 'c')
    time.sleep(seg)
pyautogui.alert(f'Cadastrado feito com sucesso')