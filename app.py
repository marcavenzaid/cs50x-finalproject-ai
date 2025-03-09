# Loading the dotenv should come first before the import so that os.getenv works on other imported python files.
from dotenv import load_dotenv
load_dotenv()

import os
import http
import subprocess
from flask import Flask, redirect, render_template, request, url_for, Response
from brain.brain import Brain
import azure.cognitiveservices.speech as azure_speech_sdk
import vocal.azure_tts_ssml_multiprocessing
import vocal.vocal as vocal
import definitions
import logging
import logger.logger_handler as logger_handler

app = Flask(__name__)

# Disable flask logger so that i can use my own logger. 
# To prevent error from using TimedRotatingFileHandler, because flask logger is accessing the log file as well.
# https://stackoverflow.com/questions/14888799/disable-console-messages-in-flask-server
# os.environ["WERKZEUG_RUN_MAIN"] = "true" 
log = logging.getLogger("werkzeug")
log.disabled = True
# Setup the logger by calling setup_logger(). Only need to call this once in main.
logger_handler.setup_logger()
logger = logging.getLogger(__name__)

brain: Brain = Brain()

error_list = []

@app.route("/", methods=("GET", "POST"))
def index():
    
    global error_list

    if request.method == "POST":

        error_list = []

        try:
            # Get the form data.
            input_message = request.form.get("inputMessage")

            # Think
            thought = brain.think(input_message)
            
        except Exception as e:
            error_list.append(e)
            logger.exception(f"{e}")

        return redirect(url_for("index"))

    # Read the saved thought.
    thought = None
    try:
        thought = brain.get_memory().read_short_term_memory_last_thought()
    except Exception as e:
        error_list.append(e)
        logger.exception(f"{e}")
    
    # Speak.
    try:
        vocal.speak(thought)
    except Exception as e:
        error_list.append(e)
        logger.exception(f"{e}")

    return render_template(
        "index.html", 
        thought=thought,
        error_list=error_list
    ) 


@app.route("/stop_ongoing_speech")
def stop_ongoing_speech():
    logger.info(f"Stopping ongoing speech..")
    vocal.tts_ssml_multiprocessing.stop_ongoing_speech()
    return ("", http.HTTPStatus.NO_CONTENT)


# Maybe remove this later and just use flask run. 
if __name__ == "__main__":

    # Run the app.
    app.run(debug=True, load_dotenv=False, use_reloader=False, port=os.getenv("PORT"))
