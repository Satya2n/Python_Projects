"""Command-line rock-paper-scissors game against the computer with score tracking."""

import random

CHOICES = ('rock', 'paper', 'scissors')

BEATS = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}


def decide_winner(user, computer):
    if user == computer:
        return 'tie'
    if BEATS[user] == computer:
        return 'user'
    return 'computer'


def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play, or 'exit' to quit.")

    user_score = 0
    computer_score = 0
    ties = 0

    while True:
        try:
            choice = input("Your choice: ").strip().lower()
        except EOFError:
            print(f"\nFinal score - You: {user_score}, Computer: {computer_score}, Ties: {ties}")
            print("Goodbye!")
            break

        if choice == 'exit':
            print(f"Final score - You: {user_score}, Computer: {computer_score}, Ties: {ties}")
            print("Goodbye!")
            break

        if choice not in CHOICES:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(CHOICES)
        print(f"Computer chose: {computer_choice}")

        outcome = decide_winner(choice, computer_choice)

        if outcome == 'tie':
            ties += 1
            print("It's a tie!")
        elif outcome == 'user':
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!")

        print(f"Score - You: {user_score}, Computer: {computer_score}, Ties: {ties}")


if __name__ == "__main__":
    main()
