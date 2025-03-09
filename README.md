# cs50-finalproject-ai

#### Video Demo:  <URL HERE>

#### Description: 
The name of the AI is **Project**.

Project is an AI friend that you can talk to. 

She is designed to be amoral, sadistic, and manipulative. 

Project uses text-to-speech so you can hear her voice, making the interaction more immersive.

Project is designed to engage users in conversations, providing responses based on the input it receives. The AI leverages the power of OpenAI's language model to generate human-like text and Microsoft Azure's Text-To-Speech (TTS) service to convert text responses into speech. This combination allows Project to interact with users in a more immersive and realistic manner.

The AI's personality is intentionally crafted to be amoral, sadistic, and manipulative, making interactions with Project unique and potentially challenging. 

Users can modify her personality by editing the initialization prompt in the `config/chatgpt_init_prompt.txt` file, allowing for a customizable experience. This flexibility enables users to tailor the AI's behavior to better suit their preferences or to explore different personality traits.

The application is built using Flask, a lightweight web framework for Python, making it easy to set up and run locally. Flask provides a robust foundation for building web applications, allowing for seamless integration with other components and services. The project also includes logging functionality to track interactions and system performance, with logs being rotated and saved in the `logger_output` directory. This logging system helps in monitoring the application's behavior, debugging issues, and ensuring smooth operation.

Project's architecture is modular, making it easy to extend and customize. The core components include the brain, memory management, vocal synthesis, and frontend interface. Each component is designed to be independent yet seamlessly integrated, allowing for flexibility in development and deployment.

The `brain` module is responsible for processing user input and generating responses using the OpenAI language model. It manages the AI's state and ensures that responses are contextually appropriate. The memory management module handles both short-term and long-term memory, allowing the AI to maintain context and remember past interactions. The `vocal` module uses Microsoft Azure's Text-To-Speech service to convert text responses into speech, providing a more immersive user experience. The frontend interface, built using HTML, CSS, and JavaScript, provides a user-friendly platform for interacting with the AI.

Project's memory management system is designed to handle both short-term and long-term memory, although long-term memory is not yet implemented. Short-term memory is stored in `last_thought.txt`, enabling the AI to maintain context within a single session. This allows Project to provide coherent and contextually relevant responses during interactions, enhancing the overall user experience.

Overall, Project aims to provide an engaging and interactive AI experience, pushing the boundaries of conversational AI and exploring the ethical implications of creating AI with complex personalities. By combining advanced language processing capabilities with customizable personality traits and immersive vocal synthesis, Project offers a unique platform for users to interact with and explore the potential of AI-driven conversations.

Project also explores the ethical implications of creating AI with complex personalities. By intentionally crafting an AI with amoral, sadistic, and manipulative traits, the project raises questions about the responsibilities of AI developers and the potential impact of AI on society. Users are encouraged to reflect on these ethical considerations and to experiment with modifying the AI's personality to better understand the consequences of different design choices.

In summary, Project is a versatile and powerful AI friend that leverages cutting-edge technologies to provide a unique and immersive conversational experience. With its customizable personality, robust memory management, and high-quality vocal synthesis, Project pushes the boundaries of what is possible with conversational AI and invites users to explore the ethical implications of AI development.

![](README_assets/0_1.png?raw=true "screenshot_01")

## Setup

1. Clone this repository.

2. Navigate into the project directory.

3. Create a new virtual environment:
   ```bash
   $ python -m venv venv
   $ venv\Scripts\activate
   ```

4. Install the requirements. The requirements.txt file lists all the dependencies required to run the application. These dependencies can be installed using the following command:
   ```bash
   $ pip install -r requirements.txt
   ```

5. Create a `.env` file and copy the contents of the `.env.example` file into it. Then, add your OpenAI API key, Microsoft Azure Text-To-Speech (TTS) resource key and service region to the newly created `.env` file.

6. (Optional) You can change her personality in `config/chatgpt_init_prompt.txt`

7. Run the app:

   ```bash
   $ flask run
   ```
   You should now be able to access the app at http://localhost:[PORT].

## Project Structure
```
cs50-finalproject-ai/
│
├── app.py
├── brain/
│   ├── brain.py
│   ├── brain_config.py
│   ├── brain_speech_openai.py
│   └── memory/
│       ├── memory.py
│       ├── memory_transferrer.py
│       └── short_term_memory/
│           └── last_thought.txt
├── config/
│   ├── chatgpt_init_prompt.txt
│   ├── config.json
│   └── config.py
├── definitions.json
├── definitions.py
├── logger/
│   ├── logger_handler.py
│   └── logger_output/
├── README.md
├── README_assets/
│   └── 0_1.png
├── requirements.txt
├── static/
│   ├── img/
│   ├── js/
│   │   └── script.js
│   └── styles.css
├── templates/
│   ├── base.html
│   └── index.html
├── utilities/
│   └── utilities.py
└── vocal/
    ├── azure_tts.py
    ├── azure_tts_ssml.py
    ├── azure_tts_ssml_multiprocessing.py
    ├── azure_tts_ssml_thread.py
    └── vocal.py
```

## Environment Variables (.env)
The environment file that contains sensitive information such as API keys. This file should not be committed to version control and should be kept secure (that is why .env is in the gitignore). 

The `.env` file is used to override settings in `config.json` for different environments (e.g., development, production).

The `.env` file should contain the following environment variables:
```
FLASK_APP=app
FLASK_ENV=development

PORT=5001

# OpenAI
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
OPENAI_API_KEY=

# Microsoft Azure Text-To-Speech (TTS)
MICROSOFT_AZURE_SPEECH_RESOURCE_KEY=
MICROSOFT_AZURE_SPEECH_RESOURCE_SERVICE_REGION=
```

The configuration system ensures that the application can be easily customized and deployed in different environments, with settings that can be adjusted without modifying the code. 

### Obtaining API Keys
To use the AI and text-to-speech functionalities, you need to obtain API keys from OpenAI and Microsoft Azure. 

Follow the steps below to get the required keys:

**OpenAI API Key**
1. Go to the OpenAI website.
2. Sign up for an account if you don't have one, or log in to your existing account.
3. Navigate to the API section of your account.
4. Create a new API key or use an existing one.
5. Copy the API key and add it to your `.env` file as `OPENAI_API_KEY`.

**Microsoft Azure Text-To-Speech (TTS) API Key and Service Region**
1. Go to the Microsoft Azure website.
2. Sign up for an account if you don't have one, or log in to your existing account.
3. Navigate to the Azure Portal.
4. Create a new resource and search for "Cognitive Services" or "Speech" to create a new Speech resource.
5. Once the resource is created, go to the resource's overview page.
6. Copy the `Key1` or `Key2` value and add it to your `.env` file as `MICROSOFT_AZURE_SPEECH_RESOURCE_KEY`.
7. Copy the `Location/Region` value and add it to your .env file as `MICROSOFT_AZURE_SPEECH_RESOURCE_SERVICE_REGION`.

By following these steps, you will have the necessary API keys to enable the AI and text-to-speech functionalities in your application.

## Configuration
The configuration settings for the application are managed in the config directory. These settings are crucial for customizing the behavior of the AI and integrating with external services. 

Key configuration files include:
- `chatgpt_init_prompt.txt`: Contains the initialization prompt for the AI. This prompt is used to set the initial context and personality of the AI when it starts a new session. By editing this file, users can customize the AI's behavior and responses to better suit their preferences.

   Key aspects of `chatgpt_init_prompt.txt` include:
   - **Personality Customization**: The prompt defines the AI's personality traits, such as being amoral, sadistic, and manipulative. Users can modify these traits to create a different personality for the AI.
   - **Context Setting**: The prompt provides the initial context for the AI, helping it understand the type of interactions it should engage in with users.
   - **Instructions**: The prompt can include specific instructions for the AI on how to respond to user inputs, ensuring consistent and coherent interactions.

   By customizing the `chatgpt_init_prompt.txt` file, users can tailor the AI's interactions to create a unique and personalized experience.

- `config.json`: Contains configuration settings for the application. This file includes parameters such as API keys, service endpoints, and other settings that control the behavior of the AI and the application.
```json
{
    "openai_chat_completion": {
        "type_A": {
            "model": "gpt-3.5-turbo",
            "messages": [],
            "temperature": 1,
            "max_tokens": 256,
            "top_p": 1,
            "frequency_penalty": 1,
            "presence_penalty": 1
        },
        "type_C": {
            "model": "gpt-3.5-turbo",
            "messages": [],
            "temperature": 1.3,
            "max_tokens": 256,
            "top_p": 1,
            "frequency_penalty": 2,
            "presence_penalty": 2
        },
        "type_X": {
            "model": "gpt-3.5-turbo",
            "messages": [],
            "temperature": 2,
            "max_tokens": 256,
            "top_p": 1,
            "frequency_penalty": 2,
            "presence_penalty": 2
        }
    }
}
```

- `config.py`: Python module for loading and accessing configuration settings.

## definitions.json and definitions.py

### definitions.json
The `definitions.json` file contains various configuration paths and settings used throughout the application. These paths and settings are referenced in the code to ensure consistency and ease of maintenance. 

Key entries include:
- `CONFIG_PATH`: The path to the main configuration file (`config.json`).
- `CHATGPT_INIT_PROMPT_PATH`: The path to the initialization prompt file for the AI (`chatgpt_init_prompt.txt`).
- `CONVERSATION_HISTORY_PATH`: The path to the file where conversation history is stored.
- `LONG_TERM_MEMORY_PATH`: The path to the file where long-term memory data will be stored (not yet implemented).
- `SHORT_TERM_MEMORY_LAST_THOUGHT_PATH`: The path to the file where short-term memory data is stored (last_thought.txt).
- `VOCAL_OUTPUT_PATH`: The path to the file where vocal output (audio) is stored.
- `LOG_OUTPUT_PATH`: The path to the log file where application logs are stored.
- `LOG_WHEN`, `LOG_INTERVAL`, `LOG_BACKUP_COUNT`, `LOG_FORMATTER_FORMAT`: Logging configuration settings, including when to rotate logs, the interval for log rotation, the number of backup logs to keep, and the log format.

### definitions.py
The `definitions.py` file is a Python module that loads and provides access to the configuration paths and settings defined in `definitions.json`. This module ensures that the application can easily reference these settings without hardcoding paths and values throughout the codebase.

## app.py
The app.py file is the main entry point for the Flask application. It sets up the Flask app, configures routes, and initializes various components of the application. 

Key functionalities include:
- Initializing the Flask app and configuring settings.
- Setting up routes for the main application and API endpoints.
- Handling requests and responses.
- Managing sessions and middleware.
- Integrating with the AI brain and vocal synthesis modules.
- Error handling and logging.

## API Endpoints
The application exposes several API endpoints for interacting with the AI. These endpoints allow users to send messages to the AI and stop ongoing speech.

Here are the key endpoints:
- `GET /`: Render the main page of the application and display the AI's thought.
   - **Response**: Renders the `index.html` template with the AI's thought and any errors that occurred.
- `POST /`: Send a message to the AI and receive a response.
   - **Request Body**: Form data containing the message to be sent to the AI.
   - **Response**: Redirects to the `GET /` endpoint to display the AI's thought.
- `GET /stop_ongoing_speech`: Stop any ongoing speech synthesis.
   - **Response**: Returns a `204 No Content` status to indicate that the speech synthesis has been stopped.

## Brain
The brain directory contains the core logic and functionality of the AI. It includes modules for processing user input, generating responses, and maintain context during interactions.. 

Key components include:
- `brain.py`: The main module that orchestrates the AI's behavior. It processes user input, generates responses using the OpenAI language model, and manages the AI's state.
- `brain_config.py`: Contains configuration settings specific to the AI's brain, such as model parameters and response generation settings.
- `brain_speech_openai.py`: Integrates the OpenAI language model with the vocal synthesis module to generate spoken responses.
- `memory/`: A subdirectory that handles the AI's memory management.
   - `memory.py`: Manages the AI's memory, including storing and retrieving information.
   - `memory_transferrer.py`: Handles the transfer of information between short-term and long-term memory (not yet implemented).
   - `short_term_memory/last_thought.txt`: Stores the AI's short-term memory, allowing it to maintain context within a single session.

## Memory Management
The AI's memory management is handled in the `memory` directory.

### Short-term memory
Short-term memory is a crucial component of the AI's functionality, allowing it to maintain context within a single session. This enables the AI to provide coherent and contextually relevant responses during interactions with users. The short-term memory is managed in the `memory` subdirectory and is stored in the `last_thought.txt` file.

Key aspects of short-term memory include:

- **Context Maintenance**: The AI uses short-term memory to remember the context of the current conversation. This helps the AI to provide responses that are relevant to the ongoing interaction.
- **Session-based Memory**: Short-term memory is specific to a single session. When a new session starts, the short-term memory is reset, ensuring that the AI does not carry over information from previous sessions.
- **Storage**: The short-term memory is stored in the `last_thought.txt` file. This file contains the most recent thoughts or context that the AI needs to remember for the current session.
- **Retrieval and Update**: The AI retrieves information from the `last_thought.txt` file to maintain context and updates this file with new information as the conversation progresses.

### Long-term memory (Not implemented yet)
This functionality is to allow the AI to remember information from a long time ago.
Long-term memory management is planned to be implemented in `memory.py` and `memory_transferrer.py`

## Vocal Synthesis
The vocal synthesis functionality is implemented using Microsoft Azure Text-To-Speech (TTS) in the vocal directory. This module is responsible for converting text responses generated by the AI into spoken words, providing a more immersive and interactive experience for users.

By leveraging Microsoft Azure Text-To-Speech (TTS) service, the application can provide high-quality, natural-sounding speech output, enhancing the overall user experience.

You can change the pitch by changing the value of `prosody pitch` of the `ssml_string`.

Example:
```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JaneNeural">
        <prosody pitch="+15%">
            {text}
        </prosody>
    </voice>
</speak>
```

## Frontend
The frontend of the application is built using HTML, CSS, and JavaScript. The main files are located in the templates and static directories:

- `base.html`: The base template for the application.
- `index.html`: The main page of the application.
- `styles.css`: The stylesheet for the application.
- `script.js`: The JavaScript file for handling frontend interactions.

### Templates
The `templates` directory contains HTML templates used to render the frontend of the application. The templates are built using Jinja2, a templating engine for Python. Jinja2 allows for dynamic content rendering and template inheritance, making it easier to manage and maintain the HTML structure of the application.

The application also utilizes Bootstrap, a popular CSS framework, to create responsive and visually appealing layouts. Bootstrap provides a wide range of pre-designed components and utilities that help streamline the development of the frontend.

Key templates include:
- `base.html`: The base template that includes common elements such as the header, footer, and navigation bar. Other templates extend this base template to ensure a consistent layout across different pages.
- `index.html`: The main page template that includes the chat interface. This template extends base.html and provides the structure for the chat functionality, including the input field and message display area.

### Static Assets
The `static` directory contains static assets such as images, JavaScript files, and CSS stylesheets. These assets are served directly to the client and are used to enhance the frontend user experience. By organizing these assets in a dedicated directory, the application can efficiently manage and serve static content.

Key components of the `static` directory include:
- **Images**: The `img` subdirectory contains image files used in the application. These images can include logos, icons, and other visual elements that enhance the user interface.
- **JavaScript Files**: The `js` subdirectory contains JavaScript files that handle frontend interactions and enhance the functionality of the application. 
- **CSS Stylesheets**: The `styles.css` file contains CSS styles that define the visual appearance of the application. 

## Logging
The logging configuration is set up in `logger_handler.py`. Logging is an essential part of the application, as it helps track interactions, monitor system performance, and debug issues. The application uses Python's built-in logging module to handle logging.

Key aspects of the logging configuration include:
- `Log Rotation`: Logs are rotated based on time intervals to prevent log files from growing indefinitely. The rotation is configured to occur at midnight, with a new log file created each day.
- `Log Storage`: Logs are stored in the `logger_output` directory. This directory contains all the log files generated by the application.
- `Log Format`: The log format is defined to include timestamps, log levels, filenames, line numbers, module names, function names, and log messages. This detailed format helps in understanding the context of each log entry.
- `Log Levels`: Different log levels (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL) are used to categorize log messages based on their severity. This allows for filtering and prioritizing log entries during analysis.

## Utilities
Utility functions and classes are defined in utilities.py, including JSON file reading and updating, execution time measurement, and custom thread pool executor.
