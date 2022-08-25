import shutil
import os
import pyautogui
import win32com.client as win32

arquivos = r'\\Srv1-rdb01\G8BD' #C:\Gestran8\G8BD\MSSQL11.SQLG8_PRODUCAO\MSSQL\Backup\G8BD
nuvem = r'C:\Users\Usuario\OneDrive\TI\BACKUP_SERVIDOR'
files = os.listdir(arquivos)
for file in files:
    copilamento = shutil.copy(f"{arquivos}/{file}", nuvem)

    # criar a integração com o outlook
    outlook = win32.Dispatch('outlook.application')
    # criar um email
    email = outlook.CreateItem(0)
    # configurar as informações do seu e-mail
    email.To = "administrativo@rodobrotto.com.br; carlos@rodobrotto.com.br; fiscal@rodobrotto.com.br; faturamento@rodobrotto.com.br; financeiro@rodobrotto.com.br"
    email.Subject = "E-mail automático Back-Up Servidor"
    email.HTMLBody = f"""
    <p>RodoBrotto informa:</p>

    <p>Back-Up efetuado com sucesso</p>
    <p>Salvo na nuvem na pasta C:\Users\Usuario\OneDrive\TI\BACKUP_SERVIDOR</p>
    <p>Arquivo \n{copilamento}</p>

    <p>Prezados colaboradores,</p>
    <p>Não responder este e-mail</p>
    """
    # anexo = "C://Users/joaop/Downloads/arquivo.xlsx"
    # email.Attachments.Add(anexo)

    email.Send()