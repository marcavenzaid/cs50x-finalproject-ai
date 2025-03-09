import azure.cognitiveservices.speech as speechsdk
import os
import logging

logger = logging.getLogger(__name__)

# Creates an instance of a speech config with specified subscription key and service region.
speech_config = speechsdk.SpeechConfig(
    subscription=os.getenv("MICROSOFT_AZURE_SPEECH_RESOURCE_KEY"), 
    region=os.getenv("MICROSOFT_AZURE_SPEECH_RESOURCE_SERVICE_REGION")
)

# Note: If the voice element is set via Speech Synthesis Markup Language (SSML), 
# the SpeechSynthesisVoiceName and SpeechSynthesisLanguage settings are ignored.
speech_config.speech_synthesis_voice_name = "en-US-JaneNeural"

audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

def speak(text):
    # This returns the result where you can check the status, but it stops being async.
    # result = speech_synthesizer.speak_text_async(text).get() 
    
    speech_synthesizer.speak_text_async(text)


def stop_ongoing_speech():
    speech_synthesizer.stop_speaking_async()
