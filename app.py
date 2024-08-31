from flask import Flask, request
from twilio_api import send_message
from dialogflow_api import detect_intent_texts
from responses import format_response
from decorators import log_activity

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
@log_activity
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From')
    response_text = detect_intent_texts(from_number, incoming_msg)
    return format_response(response_text)

if __name__ == '__main__':
    app.run(port=5000)