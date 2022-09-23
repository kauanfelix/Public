# import shutil
# import os
from twilio.rest import Client

account_sid = "AC8fd04056ad8646971a5819e8a5fd3d64"
auth_token = "ef2d9d99ef06df48abdc1a4469414e39"
client = Client(account_sid, auth_token)

# arquivos = r'C:\Users\Usuario\Documents\Arquivos do Outlook'
# #C:\Gestran8\G8BD\MSSQL11.SQLG8_PRODUCAO\MSSQL\Backup\G8BD
# nuvem = r'C:\Users\Usuario\OneDrive\TI\BACK-UP EMAIL'
# files = os.listdir(arquivos)
# for file in files:
#     copilamento = shutil.copy(f"{arquivos}/{file}", nuvem)
# #pyautogui.alert(f'Backup feito com sucesso arquivo \n{copilamento}')


message = client.messages.create(
    body="RodoBrotto: BackUp sistema Gestran feito com sucesso na nuvem.",
    from_="+12058919486",
    to="+5541984544024")
print(message.sid)
