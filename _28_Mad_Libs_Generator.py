"""Mad Libs story generator that fills user-supplied words into silly templates."""

import random

TEMPLATES = [
    (
        "The Adventure",
        "Today, a {adjective} {noun} decided to {verb} all the way to {place}. "
        "It moved so {adverb} that a nearby {animal} named {name} started to laugh "
        "uncontrollably. Everyone agreed it was the most {adjective} day ever."
    ),
    (
        "The Mishap",
        "{name} woke up and found a {adjective} {noun} sitting on the kitchen table. "
        "Without thinking, {name} decided to {verb} it {adverb}, which startled the "
        "family {animal}. They all ran off toward {place}, screaming with laughter."
    ),
]


def get_words():
    prompts = [
        ('name', "Enter a name: "),
        ('noun', "Enter a noun: "),
        ('verb', "Enter a verb: "),
        ('adjective', "Enter an adjective: "),
        ('adverb', "Enter an adverb: "),
        ('place', "Enter a place: "),
        ('animal', "Enter an animal: "),
    ]
    words = {}
    for key, prompt in prompts:
        value = input(prompt).strip()
        words[key] = value if value else key
    return words


def choose_template():
    print("Choose a story template:")
    for i, (title, _) in enumerate(TEMPLATES, start=1):
        print(f"{i}. {title}")
    print("Or press Enter for a random template.")

    choice = input("Your choice: ").strip()

    if not choice:
        return random.choice(TEMPLATES)

    try:
        index = int(choice)
        if 1 <= index <= len(TEMPLATES):
            return TEMPLATES[index - 1]
    except ValueError:
        pass

    print("Invalid choice, picking a random template instead.")
    return random.choice(TEMPLATES)


def main():
    print("Welcome to the Mad Libs Generator!")
    while True:
        try:
            start = input("Type 'go' to create a story, or 'exit' to quit: ").strip().lower()

            if start == 'exit':
                print("Exiting Mad Libs. Goodbye!")
                break

            if start != 'go':
                print("Please type 'go' or 'exit'.")
                continue

            words = get_words()
            title, template = choose_template()
            story = template.format(**words)

            print(f"\n--- {title} ---")
            print(story)
            print()

        except (ValueError, KeyError):
            print("Something went wrong building the story. Please try again.")


if __name__ == "__main__":
    main()
