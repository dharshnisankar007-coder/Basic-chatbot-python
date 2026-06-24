def greet():
    print("=" * 60)
    print("        AI ASSISTANT CHATBOT")
    print("=" * 60)
    print("Hello! I am your virtual assistant.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to exit the chatbot.")
    print("=" * 60)


def show_help():
    print("\nAvailable Commands:")
    print("- hello")
    print("- how are you")
    print("- what is your name")
    print("- who created you")
    print("- tell me a joke")
    print("- tell me a fact")
    print("- date")
    print("- time")
    print("- help")
    print("- bye\n")


def chatbot():
    import datetime

    greet()

    while True:
        user = input("\nYou: ").strip().lower()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hello! Nice to meet you. How can I assist you today?")

        elif user == "how are you":
            print("Bot: I'm doing great. Thank you for asking!")

        elif user == "what is your name":
            print("Bot: My name is AI Assistant ChatBot.")

        elif user == "who created you":
            print("Bot: I was created using Python as a rule-based chatbot project.")

        elif user == "tell me a joke":
            print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

        elif user == "tell me a fact":
            print("Bot: Python was created by Guido van Rossum and released in 1991.")

        elif user == "date":
            today = datetime.date.today()
            print(f"Bot: Today's date is {today}")

        elif user == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Current time is {current_time}")

        elif user == "help":
            show_help()

        elif user in ["thank you", "thanks"]:
            print("Bot: You're welcome! Happy to help.")

        elif user == "bye":
            print("Bot: Thank you for using AI Assistant ChatBot.")
            print("Bot: Have a wonderful day!")
            break

        else:
            print("Bot: Sorry, I don't understand that command.")
            print("Bot: Type 'help' to see available commands.")

chatbot()