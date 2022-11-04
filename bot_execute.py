import pyautogui
import time
pyautogui.hotkey('ctrl', 'alt', 'z')
time.sleep(5)
pyautogui.write('streamlit run C:/Users/admin/PycharmProjects/pythonProject/webapp.py')
pyautogui.press('Enter')

