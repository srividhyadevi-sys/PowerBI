import random
import json
import string
from nltk.tokenize import word_tokenize

# Define a simple chatbot class
class SimpleChatbot:
    def __init__(self):
        self.responses = {}

    # Function to load conversation data from JSON file
    def load_dataset(self, filename):
        with open(filename, "r") as file:
            dataset = json.load(file)
        return dataset

    # Function to train the chatbot using conversation data
    def train(self, dataset):
        for conversation in dataset:
            user_input = conversation.get("user")
            bot_response = conversation.get("bot")
            if user_input and bot_response:
                # Tokenize user input
                user_tokens = self.tokenize_input(user_input)
                for token in user_tokens:
                    if token not in self.responses:
                        self.responses[token] = [bot_response]
                    else:
                        self.responses[token].append(bot_response)

    # Function to tokenize user input
    def tokenize_input(self, input_text):
        return word_tokenize(input_text.lower())

    # Function to get a response from the chatbot
    def get_response(self, user_input):
        # Tokenize user input
        user_tokens = self.tokenize_input(user_input)
        response = []
        for token in user_tokens:
            if token in self.responses:
                response.extend(self.responses[token])
        if response:
            return random.choice(response)
        else:
            return "Sorry, I don't understand that."

# Main function
def main():
    # Initialize the chatbot
    chatbot = SimpleChatbot()

    # Load dataset from JSON file
    dataset = chatbot.load_dataset("chatbot_dataset.json")

    # Train the chatbot
    chatbot.train(dataset)

    # Interact with the chatbot
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

# Start the conversation
if __name__ == "__main__":
    main()
