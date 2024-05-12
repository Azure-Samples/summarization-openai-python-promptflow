# Speech to text sdk
import logging
import os

import azure.cognitiveservices.speech as speech
from azure.identity import ManagedIdentityCredential, DefaultAzureCredential
from dotenv import load_dotenv
from promptflow.core import (AzureOpenAIModelConfiguration,
                             OpenAIModelConfiguration, Prompty, tool)


# Load environment variables
load_dotenv()
# Change to logging.DEBUG for more verbose logging from Azure and OpenAI SDKs
logging.basicConfig(level=logging.WARNING)

from pathlib import Path
folder = Path(__file__).parent.absolute().as_posix()

if not os.getenv("OPENAI_HOST"):
    os.environ["OPENAI_HOST"] = "azure"

def process_input(input: str = None):

    # if input is non use existing file for testing
    if input is None:
        ticket_text = speech_to_text("/data/audio-data/issue1.wav")
    else:
    #check if input is an audio file or a string
        if input.endswith('.wav'):
            # process wav file if file is provided
            ticket_text = speech_to_text(input)
        else:
            # if text is provided just send text to endpoint
            ticket_text = input
    return ticket_text

def speech_to_text(filename: str = None, use_default_microphone: bool = False):
    region=os.environ["AZURE_SPEECH_REGION"]
    # Authenticate using an API key (not recommended for production)
    if os.getenv("SPEECH_KEY"):
        speech_config = speech.SpeechConfig(
        subscription=os.environ["SPEECH_KEY"], 
        region=region)
    else:
        # Authenticate using the default Azure credential chain
        azure_credential = DefaultAzureCredential() 
        access_token = azure_credential.get_token('https://cognitiveservices.azure.com/.default')
        resourceId = os.environ["AZURE_SPEECH_RESOURCE_ID"]
        authorizationToken = "aad#" + resourceId + "#" + access_token.token
        speech_config = speech.SpeechConfig(auth_token=authorizationToken, region=region)
    speech_config.speech_recognition_language="en-US"

    if use_default_microphone:
        logging.info("Using the default microphone.")
        audio_config = speech.audio.AudioConfig(
            use_default_microphone=use_default_microphone)
        logging.info("Speak into your microphone.")
    else:
        logging.info(f"Using the audio file: {filename}")
        audio_config = speech.audio.AudioConfig(filename=filename)


    speech_recognizer = speech.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_config)
    speech_recognition_result = speech_recognizer.recognize_once_async().get()


    if speech_recognition_result.reason == speech.ResultReason.RecognizedSpeech:
        print("Speech to text succesful!")
        print('')
        print(f'Full report: {speech_recognition_result.text}')
        print('')
    elif speech_recognition_result.reason == speech.ResultReason.NoMatch:
        logging.warning(
            f'''
            No speech could be recognized: 
            {speech_recognition_result.no_match_details}
            ''')
        logging.warning("No speech could be recognized.")
        exit(1)
    elif speech_recognition_result.reason == speech.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        logging.warning(f"Speech Recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speech.CancellationReason.Error:
            logging.warning(f"Error details: {cancellation_details.error_details}")
            logging.warning("Did you set the speech resource key and region values?")
            logging.warning(
                f"Speech Recognition canceled: {cancellation_details.reason}")
        exit(1)

    ticket_text = speech_recognition_result.text
    return ticket_text

def text_to_summary(ticket_text):
    # Load prompty with AzureOpenAIModelConfiguration override
    if os.getenv("OPENAI_HOST") == 'azure':
        configuration = AzureOpenAIModelConfiguration(
            azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
        )
        override_model = {
            "configuration": configuration,
            "parameters": {"max_tokens": 512}
        }
 
    elif os.getenv("OPENAI_HOST") == 'openai':
        configuration = OpenAIModelConfiguration(
            model="gpt-35-turbo",
            base_url=os.environ["OPENAI_BASE_URL"],
        )
        override_model = {
            "configuration": configuration,
            "parameters": {"max_tokens": 512}
        }

    path_to_prompty = folder + "/summarize.prompty"
    prompty_obj = Prompty.load(path_to_prompty, model=override_model)
    summary = prompty_obj(problem=ticket_text)

    return summary

# add main function that task string input as args and returns summary text string
@tool
def flow_entry(problem: str) -> str:
    reported_issue = process_input(problem)
    result = text_to_summary(reported_issue)
    return result
