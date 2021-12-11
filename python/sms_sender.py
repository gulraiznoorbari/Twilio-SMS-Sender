from twilio.rest import Client


class SMSsender:
    # Get your Account SID (String Identifier) and Auth Token @ (twilio.com/console)
    # and set the environment variables (http://twil.io/secure)
    def __init__(self, account_SID, auth_token, from_number):
        self.client = Client(account_SID, auth_token)
        self.from_number = from_number

    def send(self, to_number, message_body):
        message = self.client.messages.create(
            to=to_number,
            from_=self.from_number,
            body=message_body,
        )
        print("Message has been Sent!")


SMS_Sender = SMSsender(
    account_SID="Your Account SID Here.",
    auth_token="Your Auth Token Here.",
    from_number="Twilio Generated Number Here.",
)
SMS_Sender.send(
    to_number="Receiver's Number Here.",
    message_body="Hello World!"
)
