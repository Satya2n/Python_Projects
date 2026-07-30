"""Print a random inspirational quote from a built-in collection, by category or overall."""

import random

QUOTES = [
    ("The only way to do great work is to love what you do.", "Steve Jobs", "work"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill", "perseverance"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt", "motivation"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius", "perseverance"),
    ("Life is what happens when you're busy making other plans.", "John Lennon", "life"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt", "motivation"),
    ("Do not watch the clock. Do what it does. Keep going.", "Sam Levenson", "perseverance"),
    ("Whether you think you can or you think you can't, you're right.", "Henry Ford", "motivation"),
    ("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt", "motivation"),
    ("Hardships often prepare ordinary people for an extraordinary destiny.", "C.S. Lewis", "life"),
    ("Opportunities don't happen. You create them.", "Chris Grosser", "work"),
    ("Success usually comes to those who are too busy to be looking for it.", "Henry David Thoreau", "work"),
    ("Don't be afraid to give up the good to go for the great.", "John D. Rockefeller", "motivation"),
    ("What you get by achieving your goals is not as important as what you become by achieving your goals.", "Zig Ziglar", "life"),
    ("The way to get started is to quit talking and begin doing.", "Walt Disney", "work"),
    ("Your time is limited, so don't waste it living someone else's life.", "Steve Jobs", "life"),
    ("It always seems impossible until it's done.", "Nelson Mandela", "perseverance"),
]


def random_quote(quotes):
    return random.choice(quotes)


def quotes_in_category(quotes, category):
    return [q for q in quotes if q[2] == category.lower()]


def format_quote(quote):
    text, author, category = quote
    return f'"{text}" - {author} ({category})'


def main():
    print("Welcome to the Quote Generator!")
    print("Press Enter for a random quote, type a category (work, perseverance, motivation, life), or 'exit' to quit.")
    while True:
        try:
            entry = input("\nCategory (or Enter for random, 'exit' to quit): ").strip()

            if entry.lower() == 'exit':
                print("Exiting the Quote Generator. Goodbye!")
                break

            if not entry:
                print(format_quote(random_quote(QUOTES)))
                continue

            matches = quotes_in_category(QUOTES, entry)
            if matches:
                print(format_quote(random_quote(matches)))
            else:
                print(f"No quotes found for category '{entry}'. Try: work, perseverance, motivation, life.")

        except (KeyboardInterrupt, EOFError):
            print("\nExiting the Quote Generator. Goodbye!")
            break


if __name__ == "__main__":
    main()
