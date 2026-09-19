
# Rule-Based AI Chatbot

print("Bot: Hello! I am your AI Chatbot.")
print("Bot: Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! Welcome.")

    elif user_input == "how are you":
        print("Bot: I'm fine. Thank you!")

    elif user_input == "what is your name":
        print("Bot: My name is Python Chatbot.")

    elif user_input == "help":
        print("Bot: I can respond to simple messages.")

    elif user_input == "thank you" or user_input == "thanks":
        print("Bot: You're welcome!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.") 