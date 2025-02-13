from twilio.rest import Client
from dotenv import load_dotenv
from os import getenv

load_dotenv()

TWILIO_PHONE_NUMBER = getenv("TWILIO_PHONE_NUMBER")
TWILIO_SID = getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = getenv("TWILIO_AUTH_TOKEN")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_message(reciever, message):
    message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=message,
            to=reciever
    )

    print(f'{message.sid}: Attempting to send message to {reciever}')
