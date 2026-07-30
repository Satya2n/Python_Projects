"""Command-line dice roller that simulates rolling a configurable number of dice and sides."""

import random


def roll_dice(num_dice, num_sides):
    return [random.randint(1, num_sides) for _ in range(num_dice)]


def main():
    print("Welcome to the dice roller!")
    while True:
        try:
            dice_input = input("How many dice would you like to roll? (or 'exit' to quit): ").strip().lower()

            if dice_input == 'exit':
                print("Goodbye!")
                break

            num_dice = int(dice_input)
            if num_dice <= 0:
                print("Please enter a positive number of dice.")
                continue

            num_sides = int(input("How many sides per die? (e.g. 6): "))
            if num_sides <= 1:
                print("Please enter a die with at least 2 sides.")
                continue

            rolls = roll_dice(num_dice, num_sides)
            print(f"Rolls: {rolls}")
            print(f"Total: {sum(rolls)}")

        except ValueError:
            print("Invalid input. Please enter whole numbers.")
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
