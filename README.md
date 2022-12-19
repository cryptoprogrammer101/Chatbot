# OpenAI Chatbot

This program uses OpenAI's API to generate and edit text responses. It allows the user to choose between creating a new response or editing an existing one. The program also includes authentication using an API key and has limits on the length of the user's prompt and instructions.

## Features

* Generate text responses using OpenAI's Completion API
* Edit existing text using OpenAI's Edit API
* Authenticate using an API key
* Limit the length of the user's prompt and instructions
* Clear the terminal after each action

## How to use

1. Install the required modules: `openai` and `time`.
2. Replace `api_key.txt` with your own API key and `max_token_limit.txt` with your desired maximum token limit. The API key is used to authenticate with OpenAI's API, and the maximum token limit determines the maximum number of tokens (i.e. length of the response) that the API will generate.
3. Run the program using Python.
4. Choose between creating a new response or editing an existing one by typing `create` or `edit` respectively.
5. Enter your prompt or instructions as prompted by the program. The prompt is the text that you want the API to generate a response for, and the instructions are the edits that you want to make to an existing text.
6. The program will generate or edit a response and display it for you.
7. To quit the program, type `quit`.

## Modifying the program

You can modify the program by changing the values of the following variables:

* `completion_model`: the OpenAI model to use for generating responses. This model should be a trained instance of OpenAI's Completion API.
* `editting_model`: the OpenAI model to use for editing responses. This model should be a trained instance of OpenAI's Edit API.
* `max_prompt_char_count`: the maximum number of characters allowed in the user's prompt or instructions.
* `min_prompt_char_count`: the minimum number of characters allowed in the user's prompt or instructions.
* `horizontal_line_width`: the width of the horizontal line printed between the user's prompt/instructions and the generated/edited response.
* `print_delay_sec`: the delay in seconds before printing the generated/edited response.