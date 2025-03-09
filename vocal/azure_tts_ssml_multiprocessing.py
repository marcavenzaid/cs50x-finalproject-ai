import azure.cognitiveservices.speech as speechsdk
import multiprocessing
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
    logger.info(f"Synthesizing text to speech using multiprocessing..")
    global process
    process = multiprocessing.Process(target=synthesize, args=(text,))
    process.start()


def synthesize(text):
    """Synthesizes the given text using azure text-to-speech.

    returns: 
        result.reason: A speechsdk.ResultReason specifying the result of the synthesis.
    """
    ssml_string = f"""\
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JaneNeural">
        <prosody pitch="+15%">
            {text}
        </prosody>
    </voice>
</speak>"""

    # This returns the result where you can check the status, but it stops being async.
    result = speech_synthesizer.speak_ssml(ssml_string)

    logger.debug(f"speechsdk.ResultReason = {result.reason} ({result.reason.name})")
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        logger.info(f"Speech synthesis completed.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        logger.warning(f"Speech synthesis canceled.")

        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            logger.error(f"Speech synthesis cancellation reason - error: {cancellation_details.error_details}")
            print("ŕ̶͇̂̊̓Ö̵̯͐Ų̸̮̏Ấ̴̰̭́͠ĭ̴̧͐͐̎¶̵̫̋̈́ắ̸̞̏̓·̸̻̂ŧ̸̞͌̏͑Š̸̛̩̮ţ̸̖̌̌̎ě̷̟̻̀ͅđ̷͕̩̀͜Ķ̸̡̢̞̉̈́͋ŵ̷̪̦͎͑ḉ̷̦̭Ŧ̵͖͊̎̔Į̶̡̛̃͠Í̷͖̉̔͆¨̷̘͕̺̌̾̕Ľ̴͎͎̮̃̾͘Þ̷̨̔̉͠Ĵ̴̧̇͋͝Ņ̴̨̯͐̋̕²̷͖͋í̴̡̯͑́ª̵̳͉̰̇͊Ŧ̶͎̪́͘ĸ̶̨͖͐́¸̵͈͐̉͜ͅĸ̷̡̬̀ō̶̯̤̬̃̓̍")
        elif cancellation_details.reason == speechsdk.CancellationReason.CancelledByUser:
            logger.warning(f"Speech synthesis cancellation reason - cancelled by user: {cancellation_details.error_details}")
        else:
            logger.warning(f"Speech cancellation reason: {cancellation_details.error_details}")
    else:
        logger.warning(f"Speech synthesis was not completed and not cancelled. Result reason: {result.reason} ({result.reason.name})")

    return result.reason


def stop_ongoing_speech():
    # Sometimes SpeechSynthesizer.stop_speaking_async does not work when the text is long.
    # That is why multiprocessing is used in this module, to be able to stop the speech
    # through termination of the process.
    # speech_synthesizer.stop_speaking_async()

    global process
    if process.is_alive():
        process.terminate()
        process.join()
        logger.debug("Multiprocessing process for speaking has been terminated.")
    else:
        logger.debug("Multiprocessing process for speaking is not alive.")
