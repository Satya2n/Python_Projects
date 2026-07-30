"""Classic command-line hangman game with a built-in word list."""

import random

WORDS = (
    'python', 'hangman', 'keyboard', 'monitor', 'variable',
    'function', 'computer', 'internet', 'developer', 'algorithm',
    'database', 'network',
)

MAX_GUESSES = 6


def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)


def play_round():
    word = random.choice(WORDS)
    guessed_letters = set()
    remaining_guesses = MAX_GUESSES

    while True:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'none'}")
        print(f"Remaining guesses: {remaining_guesses}")

        try:
            guess = input("Guess a letter (or 'exit' to quit): ").strip().lower()
        except EOFError:
            print(f"\nExiting. The word was '{word}'.")
            return None

        if guess == 'exit':
            print(f"Exiting. The word was '{word}'.")
            return None

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            remaining_guesses -= 1

        if all(letter in guessed_letters for letter in word):
            print(f"\nYou win! The word was '{word}'.")
            return True

        if remaining_guesses <= 0:
            print(f"\nOut of guesses! The word was '{word}'.")
            return False


def main():
    print("Welcome to Hangman!")
    while True:
        result = play_round()

        if result is None:
            break

        try:
            again = input("Play again? [Y/n]: ").strip().lower()
        except EOFError:
            print("\nGoodbye!")
            break
        if again not in ('y', 'yes', ''):
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
