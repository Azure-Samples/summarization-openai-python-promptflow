# Speech to text sdk

import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
from promptflow import tool
from promptflow.connections import CustomConnection

# %%
# Load environment variables
load_dotenv("../local.env")
print(os.environ.get("SPEECH_REGION"))

# %%
use_default_microphone = False
filename = "../data/audio-data/issue0.wav"

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
    print(speech_recognition_result.text)
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



