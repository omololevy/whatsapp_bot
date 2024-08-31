from decorators import log_activity
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@log_activity
def send_message(body, to, from_):
    """
    Send a whatsapp message via Twilio

    """
    
    message = client.message.create(body=body, from_=from_, to=to)
    return message.sid
