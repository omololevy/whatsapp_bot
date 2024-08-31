from twilio.twiml.messaging_response import MessagingResponse

def format_response(message):
    """
    Format a response to be sent via Twilio.
    """
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(message)
    return str(resp)

