import smtplib
import email.message
import streamlit as st

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)



        def enviar_email(): 
            corpo_email = '''
            <p>Parágrafo1</p>
            <p>Parágrafo2</p>
            '''

            msg = email.message.Message()
            msg['Subject'] = 'Assunto'
            msg['From'] = 'kauanfelix@icloud.com'
            msg['To'] = 'administrativo@rodobrotto.com.br'
            password = 'kvvlmclppzxufuys'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email )

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            print('Email enviado')
st.write("Outside the form")
