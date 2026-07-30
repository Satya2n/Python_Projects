"""Simple rule-based chatbot that matches keywords to canned intents and replies."""

import random

INTENT_PATTERNS = [
    ('greeting', ['hello', 'hi', 'hey', 'good morning', 'good evening'],
        ["Hello there!", "Hi! How can I help you today?", "Hey! Good to see you."]),
    ('name', ['your name', 'who are you'],
        ["I'm ChatBot, a simple rule-based assistant.", "You can call me ChatBot."]),
    ('wellbeing', ['how are you'],
        ["I'm just a program, but I'm doing great! How about you?", "Doing well, thanks for asking!"]),
    ('thanks', ['thank', 'thanks'],
        ["You're welcome!", "Happy to help!"]),
    ('help', ['help', 'what can you do'],
        ["I can chat about greetings, my name, how I'm doing, and more. Try saying hello!"]),
    ('weather', ['weather'],
        ["I can't check live weather, but I hope it's nice where you are!"]),
    ('joke', ['joke'],
        ["Why do programmers prefer dark mode? Because light attracts bugs!"]),
    ('bye', ['bye', 'exit', 'quit', 'goodbye'],
        ["Goodbye! Have a great day!", "Bye! Talk to you soon."]),
]

FALLBACK_RESPONSES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Interesting! Tell me more.",
    "I don't have a response for that yet.",
]


def match_intent(message):
    lowered = message.lower()
    for intent, keywords, responses in INTENT_PATTERNS:
        for keyword in keywords:
            if keyword in lowered:
                return intent, responses
    return None, None


def get_response(message):
    intent, responses = match_intent(message)
    if responses:
        return intent, random.choice(responses)
    return None, random.choice(FALLBACK_RESPONSES)


def main():
    print("Welcome to the Rule-Based Chatbot!")
    print("Say hello, ask my name, or say 'bye'/'exit' to quit.")
    while True:
        try:
            message = input("You: ").strip()

            if not message:
                print("Bot: Say something!")
                continue

            intent, response = get_response(message)
            print(f"Bot: {response}")

            if intent == 'bye':
                break

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break


if __name__ == "__main__":
    main()
