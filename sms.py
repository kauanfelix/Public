from twilio.rest import Client

account_sid = "AC8fd04056ad8646971a5819e8a5fd3d64"
auth_token = "ef2d9d99ef06df48abdc1a4469414e39"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="RodoBrotto: BackUp sistema Gestran feito com sucesso na nuvem.",
    from_="+12058919486",
    to="+5541984544024")
print(message.sid)