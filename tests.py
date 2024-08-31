import unittest
from unittest.mock import patch, MagicMock
from twilio_api import send_message
from dialogflow_api import detect_intent_texts
from responses import format_response

class TestWhatsAppChatbot(unittest.TestCase):

    @patch('twilio_api.client.messages.create')
    def test_send_message(self, mock_create):
        mock_create.return_value.sid = 'SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        message_sid = send_message("Hello, World!", "+254114918899", "whatsapp:+14155238886")
        self.assertEqual(message_sid, 'SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        mock_create.assert_called_once()

    @patch('dialogflow_api.dialogflow.SessionsClient')
    def test_detect_intent_texts(self, mock_sessions_client):
        mock_session = MagicMock()
        mock_sessions_client.return_value.session_path.return_value = 'test_session_path'
        mock_sessions_client.return_value.detect_intent.return_value.query_result.fulfillment_text = 'Test response'
        response_text = detect_intent_texts("test_session_id", "Hello!")
        self.assertEqual(response_text, 'Test response')
        mock_sessions_client.return_value.session_path.assert_called_once_with('prime-hydra-434221-v4', 'test_session_id')

    def test_format_response(self):
        response = format_response("Hello, World!")
        self.assertIn('<Response><Message><Body>Hello, World!</Body></Message></Response>', response)

if __name__ == '__main__':
    unittest.main()
