import pyautogui
import time
pyautogui.alert(f'Após clicar em OK terá 4 segundos para posicionar o mouse!')
segundo = 4
time.sleep(segundo)
x, y = pyautogui.position()
pyautogui.alert(f'Posicao atual do mouse:\n x = {x} y = {y}')
