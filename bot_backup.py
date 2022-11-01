import shutil
import os
import pyautogui

arquivos = r'\\Srv1-rdb01\G8BD' #C:\Gestran8\G8BD\MSSQL11.SQLG8_PRODUCAO\MSSQL\Backup\G8BD
nuvem = r'C:\Users\Usuario\OneDrive\TI\BACKUP_SERVIDOR'
files = os.listdir(arquivos)
for file in files:
    copilamento = shutil.copy(f"{arquivos}/{file}", nuvem)
pyautogui.alert(f'Back-Up feito com sucesso arquivo \n{copilamento}')

#notificar por email
#import win32com.client as win32
# outlook = win32.Dispatch('outlook.application')
# email = outlook.CreateItem(0)
# email.To = "administrativo@rodobrotto.com.br; carlos@rodobrotto.com.br; fiscal@rodobrotto.com.br; faturamento@rodobrotto.com.br; financeiro@rodobrotto.com.br"
# email.Subject = "E-mail automático Back-Up Servidor"
# email.HTMLBody = f"""
# <p>RodoBrotto informa:</p>
# <p>Back-Up servidore fetuado com sucesso \n{copilamento}</p>
# <p>Prezados colaboradores,</p>
# <p>Não responder este e-mail</p>
# """
# anexo = "C://Users/joaop/Downloads/arquivo.xlsx"
# email.Attachments.Add(anexo)
# email.Send()

#notificar por sms
# from twilio.rest import Client
# account_sid = "AC8fd04056ad8646971a5819e8a5fd3d64"
# auth_token = "ef2d9d99ef06df48abdc1a4469414e39"
# client = Client(account_sid, auth_token)
# message = client.messages.create(
#     body="RodoBrotto: BackUp sistema Gestran feito com sucesso na nuvem.",
#     from_="+12058919486",
#     to="+5541984544024")
# print(message.sid)
