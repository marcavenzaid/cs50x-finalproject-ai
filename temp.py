import openai
import logging
import definitions

logger = logging.getLogger(__name__)


conversation = list()
conversation.append({
    "role": "system", 
    "content": ""
})


def think_response(message, brain_config):
    logger.info(f"Brain is thinking of a response..")

    conversation.append({"role": "user", "content": message})

    logger.debug(f"Conversation: {conversation}")

    try:
        brain_response = gpt_chat_completion(conversation, brain_config)
    except Exception as e:
        raise e

    brain_response_message = brain_response["choices"][0]["message"]["content"]

    write_brain_response_output(brain_response_message)

    return brain_response


def gpt_chat_completion(messages, brain_config):

    try:
        brain_response = openai.ChatCompletion.create(
            model=brain_config["model"],
            messages=messages,
            temperature=brain_config["temperature"],
            max_tokens=brain_config["max_tokens"],
            top_p=brain_config["top_p"],
            frequency_penalty=brain_config["frequency_penalty"],
            presence_penalty=brain_config["presence_penalty"]
        )
    except Exception as e:
        raise e

    logger.info(f"brain_response: {brain_response}")

    return brain_response


def write_brain_response_output(brain_response_message):
    with open(definitions.BRAIN_RESPONSE_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(brain_response_message)
