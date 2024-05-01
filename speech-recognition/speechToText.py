# Speech to text sdk

import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv, find_dotenv
from promptflow.core import Prompty, AzureOpenAIModelConfiguration, OpenAIModelConfiguration

# %%
# Load environment variables
load_dotenv(find_dotenv())

# %%
use_default_microphone = False
filename = "../ticket-processing/data/audio-data/issue2.wav"

# %%
speech_config = speechsdk.SpeechConfig(subscription=os.environ["SPEECH_KEY"], region=os.environ["SPEECH_REGION"])
speech_config.speech_recognition_language="en-US"

if use_default_microphone:
    print("Using the default microphone.")
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=use_default_microphone)
    print("Speak into your microphone.")
else:
    print("Using the audio file: {}".format(filename))
    audio_config = speechsdk.audio.AudioConfig(filename=filename)

        
# %%
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
speech_recognition_result = speech_recognizer.recognize_once_async().get()


# %%
if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(speech_recognition_result.text))
elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    print("No speech could be recognized.")
elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_recognition_result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
        print("Did you set the speech resource key and region values?")
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))

ticket_text = speech_recognition_result.text

# Load prompty with AzureOpenAIModelConfiguration override
configuration = AzureOpenAIModelConfiguration(
    azure_deployment="prompty-ai",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
)
override_model = {
    "configuration": configuration,
    "parameters": {"max_tokens": 512}
}

# If you'd like to use your OpenAI account instead, use the following configuration
# configuration = OpenAIModelConfiguration(
#     model="gpt-35-turbo",
#     base_url="${env:OPENAI_BASE_URL}",
#     api_key="${env:OPENAI_API_KEY}",
# )
# override_model = {
#     "configuration": configuration,
#     "parameters": {"max_tokens": 512}
# }

prompty_obj = Prompty.load("../ticket-processing/summarize.prompty", model=override_model)
summary = prompty_obj(problem=f'{ticket_text}')

print(" ")
print("Reported Issue: ")
print(summary)

