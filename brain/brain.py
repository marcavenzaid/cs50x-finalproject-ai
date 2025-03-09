from openai import OpenAI
import logging
import os
from utilities.utilities import ExecutionTimeMeasurer
from brain.brain_config import BrainConfig
from brain.brain_speech_openai import BrainSpeechOpenAI
from brain.memory.memory import Memory

logger = logging.getLogger(__name__)

class Brain():

    def __init__(self):
        # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
        # if you saved the key under a different environment variable name, you can do something like:
        # client = OpenAI(
        #   api_key=os.environ.get("CUSTOM_ENV_NAME"),
        # )
        self._openai_client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        # self._brainConfig = BrainConfig("type_X")
        self._brainConfig = BrainConfig("type_A")
        self._brain_speech_openai = BrainSpeechOpenAI(self._openai_client, self._brainConfig)
        self._memory = Memory()


    def think(self, message):
        logger.info(f"Brain is thinking of a response..")
        execution_time_measurer = ExecutionTimeMeasurer()
        execution_time_measurer.start()
        # ----------------------------------------------

        chat_completion = self._brain_speech_openai.chat_completion(message)
        thought = chat_completion.choices[0].message.content

        self._memory.save_to_short_term_memory_last_thought(thought)

        # ----------------------------------------------
        execution_time = execution_time_measurer.get_elapsed_time()
        logger.info(f"Execution time of Brain thinking of a response is: {execution_time} seconds.")


    def get_openai_client(self):
        return self._openai_client
    

    def get_brain_speech_openai(self):
        return self._brain_speech_openai
    

    def get_memory(self):
        return self._memory
    