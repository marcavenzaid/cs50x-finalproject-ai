import logging
import definitions
from brain.brain import BrainConfig

logger = logging.getLogger(__name__)

class BrainSpeechOpenAI:

    def __init__(self, openai_client, brain_config: BrainConfig):
        self._openai_client = openai_client
        self._brain_config = brain_config
        self._openai_chat_completion_config = self._brain_config.get_openai_chat_completion_config()

        self._conversation = list()
        self._conversation.append({
            "role": "system", 
            "content": self._brain_config.get_chatgpt_init_prompt()
        })


    def chat_completion(self, message):
        # self._is_message_valid(message)

        self._conversation.append({"role": "user", "content": message})

        logger.debug(f"Conversation: {self._conversation}")

        try:
            chat_completion = self._openai_client.chat.completions.create(
                model=self._openai_chat_completion_config["model"],
                messages=self._conversation,
                temperature=self._openai_chat_completion_config["temperature"],
                max_tokens=self._openai_chat_completion_config["max_tokens"],
                top_p=self._openai_chat_completion_config["top_p"],
                frequency_penalty=self._openai_chat_completion_config["frequency_penalty"],
                presence_penalty=self._openai_chat_completion_config["presence_penalty"]
            )
        except Exception as e:
            raise e

        logger.info(f"chat_completion: {chat_completion}")

        # self._is_response_valid(brain_response)

        return chat_completion


    def _is_message_valid(self, message) -> bool:
        # check length
        # check message language?
        # check for bad words?

        return True


    def _is_response_valid(self, response) -> bool:
        # finish_reason = response["choices"][0]["finish_reason"]

        # print("finish_reason:", finish_reason)

        # if finish_reason == ChatCompletionContants.FinishReason.STOP:
        #     print()
        # elif finish_reason == ChatCompletionContants.FinishReason.LENGTH:
        #     print()
        # elif finish_reason == ChatCompletionContants.FinishReason.CONTENT_FILTER:
        #     print()
        # elif finish_reason == ChatCompletionContants.FinishReason.NULL:
        #     print()

        return True
