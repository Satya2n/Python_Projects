"""Command-line coin flip simulator that reports the sequence, counts, and percentages."""

import random


def flip_coins(num_flips):
    return [random.choice(('Heads', 'Tails')) for _ in range(num_flips)]


def main():
    print("Welcome to the coin flip simulator!")
    while True:
        try:
            flips_input = input("How many times would you like to flip? (or 'exit' to quit): ").strip().lower()
        except EOFError:
            print("\nGoodbye!")
            break

        if flips_input == 'exit':
            print("Goodbye!")
            break

        try:
            num_flips = int(flips_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if num_flips <= 0:
            print("Please enter a positive number of flips.")
            continue

        results = flip_coins(num_flips)
        heads = results.count('Heads')
        tails = results.count('Tails')

        print(f"Sequence: {', '.join(results)}")
        print(f"Heads: {heads} ({heads / num_flips:.1%})")
        print(f"Tails: {tails} ({tails / num_flips:.1%})")


if __name__ == "__main__":
    main()
