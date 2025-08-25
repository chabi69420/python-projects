def chatbot():
    print("🤖 Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("🤖 Chatbot: Hello! How can I help you?")
        elif "your name" in user_input:
            print("🤖 Chatbot: I am PyBot, your assistant!")
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great! Thanks for asking. How about you?")
        elif "time" in user_input:
            from datetime import datetime
            print(f"🤖 Chatbot: The current time is {datetime.now().strftime('%H:%M:%S')}")
        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("🤖 Chatbot: Sorry, I don’t understand that yet.")

# Run chatbot
chatbot()
