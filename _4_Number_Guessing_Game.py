"""Command-line number guessing game where the computer picks a random number to guess."""

import random


def get_hint(guess, target):
    if guess < target:
        return "Higher! Try a bigger number."
    return "Lower! Try a smaller number."


def play_round(lower, upper):
    target = random.randint(lower, upper)
    attempts = 0

    while True:
        try:
            guess_input = input(f"Guess a number between {lower} and {upper} (or 'exit' to quit): ").strip().lower()
        except EOFError:
            return None

        if guess_input == 'exit':
            return None

        try:
            guess = int(guess_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        attempts += 1

        if guess == target:
            print(f"Correct! The number was {target}. You took {attempts} attempt(s).")
            return attempts

        print(get_hint(guess, target))


def main():
    print("Welcome to the number guessing game!")
    lower, upper = 1, 100
    while True:
        result = play_round(lower, upper)

        if result is None:
            print("Exiting the game. Goodbye!")
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
