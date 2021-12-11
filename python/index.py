import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

messages = client.messages.list()
for msg in messages:
    print(msg.body)

msg = client.messages.create(
    to="+923184188489",
    from_="+18124152070",
    body="Hello",
)

print(msg.body)

"""
Deletes all the messages in your Twilio account:

for msg in messages:
    print(f"Deleting: {msg.body}")
    msg.delete()

"""
