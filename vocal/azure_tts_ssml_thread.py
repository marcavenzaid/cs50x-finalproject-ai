import azure.cognitiveservices.speech as azure_speech_sdk
from utilities.utilities import CustomThreadPoolExecutor
import os
import logging

logger = logging.getLogger(__name__)

# Creates an instance of a speech config with specified subscription key and service region.
speech_config = azure_speech_sdk.SpeechConfig(
    subscription=os.getenv("MICROSOFT_AZURE_SPEECH_RESOURCE_KEY"), 
    region=os.getenv("MICROSOFT_AZURE_SPEECH_RESOURCE_SERVICE_REGION")
)

# To output synthesized speech to the current active output device such as a speaker, set the use_default_speaker parameter to true.
audio_config = azure_speech_sdk.audio.AudioOutputConfig(use_default_speaker=True)

speech_synthesizer = azure_speech_sdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

def speak(text):
    logger.info(f"Synthesizing text to speech in a thread..")

    synthesize(text)


def synthesize(text):
    ssml_string = f"""\
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JaneNeural">
        <prosody pitch="+15%">
            {text}
        </prosody>
    </voice>
</speak>"""

    # Sometimes SpeechSynthesizer.stop_speaking or SpeechSynthesizer.stop_speaking_async 
    # does not work when the text is long. That is why threading is used in this module 
    # instead of simply using SpeechSynthesizer.speak_ssml_async, to be able to stop the 
    # speech through stoppage of the process.
    global executor
    executor = CustomThreadPoolExecutor()
    future = executor.submit(speech_synthesizer.speak_ssml, ssml_string)
    
    # Check if the executor has been shut down before calling future.result()
    if executor.is_running():
        result = future.result() # Get the return value of the speech_synthesizer.speak_ssml

    # CustomThreadPoolExecutor does not automatically shut down. You need to explicitly 
    # call the shutdown() method on the executor to initiate the shutdown process.
    executor.shutdown()

    if result == None:
        logger.debug("Speech synthesis canceled using executor.shutdown().")
    else:
        logger.debug(f"speechsdk.ResultReason = {result.reason} ({result.reason.name})")
        if result.reason == azure_speech_sdk.ResultReason.SynthesizingAudioCompleted:
            logger.debug("Speech synthesis completed.")
        elif result.reason == azure_speech_sdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            logger.debug(f"Speech synthesis canceled: {cancellation_details.reason}")
            logger.debug(f"Speech synthesis canceled: {cancellation_details.reason.name}")

            if cancellation_details.reason == azure_speech_sdk.CancellationReason.Error:
                logger.debug(f"Speech synthesis cancellation reason - error: {cancellation_details.error_details}")
                print("ŕ̶͇̂̊̓Ö̵̯͐Ų̸̮̏Ấ̴̰̭́͠ĭ̴̧͐͐̎¶̵̫̋̈́ắ̸̞̏̓·̸̻̂ŧ̸̞͌̏͑Š̸̛̩̮ţ̸̖̌̌̎ě̷̟̻̀ͅđ̷͕̩̀͜Ķ̸̡̢̞̉̈́͋ŵ̷̪̦͎͑ḉ̷̦̭Ŧ̵͖͊̎̔Į̶̡̛̃͠Í̷͖̉̔͆¨̷̘͕̺̌̾̕Ľ̴͎͎̮̃̾͘Þ̷̨̔̉͠Ĵ̴̧̇͋͝Ņ̴̨̯͐̋̕²̷͖͋í̴̡̯͑́ª̵̳͉̰̇͊Ŧ̶͎̪́͘ĸ̶̨͖͐́¸̵͈͐̉͜ͅĸ̷̡̬̀ō̶̯̤̬̃̓̍")
                update_brain_response_output("ŕ̶͇̂̊̓Ö̵̯͐Ų̸̮̏Ấ̴̰̭́͠ĭ̴̧͐͐̎¶̵̫̋̈́ắ̸̞̏̓·̸̻̂ŧ̸̞͌̏͑Š̸̛̩̮ţ̸̖̌̌̎ě̷̟̻̀ͅđ̷͕̩̀͜Ķ̸̡̢̞̉̈́͋ŵ̷̪̦͎͑ḉ̷̦̭Ŧ̵͖͊̎̔Į̶̡̛̃͠Í̷͖̉̔͆¨̷̘͕̺̌̾̕Ľ̴͎͎̮̃̾͘Þ̷̨̔̉͠Ĵ̴̧̇͋͝Ņ̴̨̯͐̋̕²̷͖͋í̴̡̯͑́ª̵̳͉̰̇͊Ŧ̶͎̪́͘ĸ̶̨͖͐́¸̵͈͐̉͜ͅĸ̷̡̬̀ō̶̯̤̬̃̓̍")   
        else:
            logger.warning(f"Speech synthesis was not completed nor cancelled. Result reason: {result.reason} ({result.reason.name})")


def stop_ongoing_speech():
    speech_synthesizer.stop_speaking()
    
    global executor
    if executor.is_running():
        # wait=False is used to forcefully terminate the tasks and the executor since
        # shutdown method is not an immediate termination; it allows the currently 
        # running tasks to complete while preventing new tasks from being accepted.
        executor.shutdown(wait=False)
        logger.debug("CustomThreadPoolExecutor.shutdown(wait=False) was executed.")
