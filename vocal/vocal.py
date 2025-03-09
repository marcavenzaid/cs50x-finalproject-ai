import azure.cognitiveservices.speech as azure_speech_sdk
import vocal.azure_tts_ssml_multiprocessing as tts_ssml_multiprocessing
import definitions
import logging

logger = logging.getLogger(__name__)

def speak(text):    
    logger.info(f"Attempting to say: {text}..")

    try:
        if text is not None and text != "":
            logger.info(f"Synthesizing text..")
            tts_ssml_multiprocessing.speak(text)
    except Exception as e:
        raise e
    