import openai
import sys
import os
import playAsong

if os.path.exists(".env"):
    with open(".env") as env_file:
        for line in env_file:
            key, val = line.strip().split("=")
            os.environ[key] = val

# Load OpenAI API key
messages_input = [
    {"role": "system", "content": "You are a helpful assistant who is also good at recommending great songs when asked."
                                  "Continue your conversation as usual with the user, but if you see that the user wants to play"
                                  " a song, make sure the last line of your response includes the song's name as 'play: '."
                                  "This will ensure that a spotify client reading your responses is able to follow the instructions."
     },
    {"role": "user", "content": "Play Perfect"},
    {"role": "assistant", "content": "play: Perfect"},
    {"role": "user", "content": "Play a romantic song"},
    {"role": "assistant", "content": "play: Thinking out loud"},
    {"role": "user", "content": "play insane"},
    {"role": "assistant", "content": "play: insane"},
    {"role": "user", "content": "can you play something similar to All of me"},
    {"role": "assistant", "content": "play: Say you won't let go"},
    {"role": "user", "content": "how many continents are there in the world?"},
    {"role": "assistant", "content": "7"},
    {"role": "user", "content": "i want to listen to a spanish sad song"},
    {"role": "assistant", "content": "play: corre"},
]


# Define function to generate text with GPT-3
def generate_text():
    global messages_input
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_input
    )
    text = response['choices'][0]['message']['content']
    return text.strip()


def update_messages_input_prompt(prompt):
    global messages_input
    messages_input.append({
        "role": "user", "content": prompt
    })
    # print(messages_input)


def update_messages_input_response(response):
    global messages_input
    messages_input.append({
        "role": "assistant", "content": response
    })
    # print(messages_input)


while True:
    user_input = input("Enter your input:(Type 'out' to exit) ")
    if user_input == "out":
        break
    update_messages_input_prompt(user_input)
    response = generate_text()
    update_messages_input_response(response)
    print("Output:\n", response)
    last_line = response.split("\n")[-1]
    if last_line.startswith("play: "):
        playAsong.playSong(last_line.removeprefix("play: "))
