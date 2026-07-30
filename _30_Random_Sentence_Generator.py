"""Generates random silly sentences from built-in word banks."""

import random

SUBJECTS = ["The cat", "A wizard", "My neighbor", "The robot", "A pirate", "The teacher"]
VERBS = ["chased", "discovered", "painted", "devoured", "questioned", "juggled"]
ADJECTIVES = ["mysterious", "gigantic", "tiny", "sparkling", "ancient", "invisible"]
OBJECTS = ["a spaceship", "the treasure map", "a bowl of soup", "the old bicycle", "a rubber duck", "the moon"]
ADVERBS = ["quickly", "quietly", "cheerfully", "suddenly", "carelessly", "gracefully"]


def generate_sentence():
    subject = random.choice(SUBJECTS)
    verb = random.choice(VERBS)
    adjective = random.choice(ADJECTIVES)
    obj = random.choice(OBJECTS)
    adverb = random.choice(ADVERBS)
    return f"{subject} {verb} {adjective} {obj} {adverb}."


def main():
    print("Welcome to the Random Sentence Generator!")
    while True:
        try:
            count_input = input("How many sentences to generate? (or 'exit' to quit): ").strip()

            if count_input.lower() == 'exit':
                print("Exiting the sentence generator. Goodbye!")
                break

            count = int(count_input)

            if count <= 0:
                print("Please enter a positive number.")
                continue

            if count > 50:
                print("That's a lot! Generating only the first 50 sentences.")
                count = 50

            for _ in range(count):
                print(generate_sentence())
            print()

        except ValueError:
            print("Invalid input. Please enter a whole number or 'exit'.")


if __name__ == "__main__":
    main()
