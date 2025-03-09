import definitions
import logging
import utilities.utilities as utilities

logger = logging.getLogger(__name__)

class BrainConfig():

    def __init__(self, type_name):
        """
        Parameters: 
            type_name: The configuration type defined in config/config.json "openai_chat_completion".
        """
        logger.info(f"Initializing Brain {type_name}..")
        self._openai_chat_completion_config = None
        self._chatgpt_init_prompt = None
        self._type_name = type_name
        self._load_openai_config()
        self._load_chatgpt_init_prompt()
        logger.info(f"Brain {type_name} initialized.")


    def get_openai_chat_completion_config(self):
        return self._openai_chat_completion_config

    
    def get_chatgpt_init_prompt(self):
        return self._chatgpt_init_prompt


    def _load_openai_config(self):
        """Loads the openai config from the json file."""
        openai_config_json = utilities.read_json_file(definitions.CONFIG_PATH)

        self._openai_chat_completion_config = openai_config_json["openai_chat_completion"][self._type_name]

        logger.info(f"Brain config {self._type_name}: {self._openai_chat_completion_config}")

        # self._openai_chat_completion_config = {
        #     "model": openai_config_json["openai_chat_completion"][0]["model"],
        #     "message": openai_config_json["openai_chat_completion"][0]["messages"],
        #     "temperature": openai_config_json["openai_chat_completion"][0]["temperature"],
        #     "max_tokens": openai_config_json["openai_chat_completion"][0]["max_tokens"],
        #     "top_p": openai_config_json["openai_chat_completion"][0]["top_p"],
        #     "frequency_penalty": openai_config_json["openai_chat_completion"][0]["frequency_penalty"],
        #     "presence_penalty": openai_config_json["openai_chat_completion"][0]["presence_penalty"]
        # }


    def _load_chatgpt_init_prompt(self):
        chatgpt_init_prompt_path = definitions.CHATGPT_INIT_PROMPT_PATH

        try:
            with open(chatgpt_init_prompt_path, "r", encoding="utf-8") as chatgpt_init_prompt_file:
                self._chatgpt_init_prompt = chatgpt_init_prompt_file.read()
        except Exception as e:
            logger.exception(f"An error occurred while reading the file: {e}")
            raise e
