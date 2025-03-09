import logging
import definitions
import os

logger = logging.getLogger(__name__)

class Memory():
    
    def __init__(self):
        pass


    def read_short_term_memory_last_thought(self):
        last_thought = None

        try:
            if os.path.exists(definitions.SHORT_TERM_MEMORY_LAST_THOUGHT_PATH):
                with open(definitions.SHORT_TERM_MEMORY_LAST_THOUGHT_PATH, "r", encoding="utf-8") as file:
                    last_thought = file.read()
        except Exception as e:
            raise e

        return last_thought


    def save_to_short_term_memory_last_thought(self, str):
        with open(definitions.SHORT_TERM_MEMORY_LAST_THOUGHT_PATH, "w", encoding="utf-8") as file:
            file.write(str)


    def save_to_long_term_memory(self, str):
        with open(definitions.LONG_TERM_MEMORY_PATH, "w", encoding="utf-8") as file:
            file.write(str)