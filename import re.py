import re
import random

def respond(user_input):
    for pattern, responses in patterns.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            response = random.choice(responses)
            return response.format(*re.findall(pattern, user_input, re.IGNORECASE))
    return "I'm not sure I understand. Can you elaborate?"

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    else:
        bot_response = respond(user_input)
        print("Bot:", bot_response)
