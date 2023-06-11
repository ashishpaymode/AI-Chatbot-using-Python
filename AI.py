import random

# Define a dictionary of predefined responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how_are_you": ["I'm good, thanks!", "I'm doing well.", "All is well!"],
    "goodbye": ["Goodbye!", "Farewell!", "Have a great day!"],
    "default": ["I'm sorry, I don't understand.", "Can you please rephrase that?", "I'm still learning."]
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()

    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

# Main loop to keep the chatbot running
while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    bot_response = get_response(user_input)
    print("Chatbot:", bot_response)
