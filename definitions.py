import os
import json
import utilities.utilities as utilities

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFINITIONS_JSON_PATH = os.path.join(ROOT_DIR, "definitions.json")

try:
    with open(DEFINITIONS_JSON_PATH, "r", encoding="utf-8") as file:
        definitions_json = json.load(file)
except FileNotFoundError as e:
    raise e
except json.JSONDecodeError as e:
    raise e
except Exception as e:
    raise e

# Replace ${ROOT_DIR} with the actual value of ROOT_DIR.
for key, value in definitions_json.items():
    if isinstance(value, str) and "${ROOT_DIR}" in value:
        value = value.replace("${ROOT_DIR}", ROOT_DIR)
        definitions_json[key] = value

CONFIG_PATH = definitions_json["CONFIG_PATH"]
CHATGPT_INIT_PROMPT_PATH = definitions_json["CHATGPT_INIT_PROMPT_PATH"]

CONVERSATION_HISTORY_PATH = definitions_json["CONVERSATION_HISTORY_PATH"]

SHORT_TERM_MEMORY_LAST_THOUGHT_PATH = definitions_json["SHORT_TERM_MEMORY_LAST_THOUGHT_PATH"]
LONG_TERM_MEMORY_PATH = definitions_json["LONG_TERM_MEMORY_PATH"]

VOCAL_OUTPUT_PATH = definitions_json["VOCAL_OUTPUT_PATH"]

LOG_OUTPUT_PATH = definitions_json["LOG_OUTPUT_PATH"]
LOG_WHEN = definitions_json["LOG_WHEN"]
LOG_INTERVAL = definitions_json["LOG_INTERVAL"]
LOG_BACKUP_COUNT = definitions_json["LOG_BACKUP_COUNT"]
LOG_FORMATTER_FORMAT = definitions_json["LOG_FORMATTER_FORMAT"]
