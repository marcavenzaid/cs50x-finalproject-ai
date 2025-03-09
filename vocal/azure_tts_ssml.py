import azure.cognitiveservices.speech as speechsdk
import os
import logging

logger = logging.getLogger(__name__)

# Creates an instance of a speech config with specified subscription key and service region.
speech_config = speechsdk.SpeechConfig(
    subscription=os.getenv("MICROSOFT_AZURE_SPEECH_RESOURCE_KEY"), 
    region=os.getenv("MICROSOFT_AZURE_SPEECH_RESOURCE_SERVICE_REGION")
)

# To output synthesized speech to the current active output device such as a speaker, set the use_default_speaker parameter to true.
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

def speak(text):
    """This uses SpeechSynthesizer.speak_ssml which is not async, the program will need to 
    wait for the speech to finish before it continues to the next code. If you want an async 
    version either use the speak_async function or use the azure_tts_ssml_multiprocessing.py
    """
    logger.info(f"Synthesizing text to speech asynchronously..")

    ssml_string = f"""\
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JaneNeural">
        <prosody pitch="+20%">
            {text}
        </prosody>
    </voice>
</speak>"""

    # This returns the result where you can check the status, but it stops being async.
    result = speech_synthesizer.speak_ssml(ssml_string)

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        logger.debug("Speech synthesis completed.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        logger.debug(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            logger.debug(f"Speech synthesis error: {cancellation_details.error_details}")


def speak_async(text):
    logger.info(f"Synthesizing text to speech asynchronously..")
    
    ssml_string = f"""\
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JaneNeural">
        <prosody pitch="+20%">
            {text}
        </prosody>
    </voice>
</speak>"""

    # This returns the result where you can check the status, but it stops being async.
    # result = speech_synthesizer.speak_text_async(text).get() 

    speech_synthesizer.speak_ssml_async(ssml_string)


def stop_ongoing_speech():
    speech_synthesizer.stop_speaking_async()
