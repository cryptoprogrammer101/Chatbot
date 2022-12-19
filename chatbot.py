# import modules
import os
import openai
import time

completion_model = "text-davinci-003"
editting_model = "text-davinci-edit-001"

max_prompt_char_count = 200
min_prompt_char_count = 10

horizontal_line_width = 50

create_option_str = "create"
edit_option_str = "edit"
quit_option_str = "quit"

# number of tokens, length of response
max_token_limit = 4000

print_delay_sec = 3


def retrieveAPIKey():
    # read api key from file
    with open("api_key.txt", "r") as f:
        # return key
        return f.read().strip()


def authenticate(key):
    # authenticate using api key
    openai.api_key = key


def getTextFromResponse(response):

    try:
        # extract text from json
        return response["choices"][0]["text"].strip()

    except KeyError:
        return "Error: Could not extract text from response"


def printHorizontalLine():
    print("\n" + "-" * horizontal_line_width + "\n")


def generateResponse(prompt):

    try:
        # generate response
        return openai.Completion.create(model=completion_model, prompt=prompt, max_tokens=max_token_limit)

    except Exception:
        return "Error: Could not generate completion response"


def editResponse(prompt, instructions):

    try:
        # edit response
        return openai.Edit.create(model=editting_model, input=prompt, instruction=instructions)

    except Exception:
        return "Error: Could not edit text"


def delayPrint(delay):
    time.sleep(delay)


def checkLength(string):

    # check if string is within the desired length range
    if min_prompt_char_count < len(string) < max_prompt_char_count:
        return True

    return False


def create(prompt):

    # if prompt is not correct length
    if not checkLength(prompt):

        print("\nResponse must be at least %s characters and less than %s characters.\n" % (
            min_prompt_char_count, max_prompt_char_count))

        delayPrint(print_delay_sec)

        return False

    # generate response
    response = generateResponse(prompt)

    # retrieve text from response
    text = getTextFromResponse(response)

    # display text
    printHorizontalLine()
    print("\n%s\n" % text)
    printHorizontalLine()
    delayPrint(print_delay_sec)

    return True


def edit(user_prompt, instructions):

    # if prompt or instructions is not correct length
    if not checkLength(user_prompt) or not checkLength(instructions):

        print("\nResponse and instructions must be at least %s characters and less than %s characters.\n" % (
            min_prompt_char_count, max_prompt_char_count))

        delayPrint(print_delay_sec)

        return False

    # edit response
    response = editResponse(user_prompt, instructions)

    # retrieve text from response
    text = getTextFromResponse(response)

    # display text
    printHorizontalLine()
    print("\n%s\n" % text)
    printHorizontalLine()
    delayPrint(print_delay_sec)

    return True


try:

    api_key = retrieveAPIKey()

    authenticate(api_key)

    os.system("clear")

    user_option = ""

    while user_option != quit_option_str:

        # ask user for their choice
        user_option = input("\nDo you want to create, edit or quit: ")

        # convert to lowercase
        user_option = user_option.lower()

        # user said create
        if user_option == create_option_str:

            # ask for prompt
            user_prompt = input("\nEnter prompt: ")

            create(user_prompt)

        # user said edit
        elif user_option == edit_option_str:

            # ask for text to edit
            user_prompt = input("\nEnter text to edit: ")

            # ask for instructions
            instructions = input("\nEditting instructions: ")

            edit(user_prompt, instructions)

        # invalid input
        elif user_option != quit_option_str:
            # display error
            print("Invalid input. Enter \"create\", \"edit\" or \"quit\".")
            delayPrint(print_delay_sec)

except:
    pass

print("\nQuitting program...")
