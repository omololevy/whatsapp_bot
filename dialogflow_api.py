from google.cloud import dialogflow_v2 as dialogflow
from config import DIALOGFLOW_PROJECT_ID
from decorators import log_activity, timing

@timing
@log_activity

def detect_intent_texts(session_id, text, language_code='en'):
    """
    Detect intent using the DialogFlow.
    """
    session_client = dialogflow.SessionClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text