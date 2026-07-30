"""Simple countdown timer that prints the remaining seconds until time's up."""

import time

MAX_SECONDS = 10


def run_countdown(seconds):
    for remaining in range(seconds, 0, -1):
        print(f"{remaining}...")
        time.sleep(1)
    print("Time's up!")


def main():
    print("Welcome to the Countdown Timer!")
    print(f"(Max allowed duration is {MAX_SECONDS} seconds so runs stay quick.)")

    while True:
        try:
            duration_input = input("Enter countdown duration in seconds (or 'exit' to quit): ").strip()

            if duration_input.lower() == 'exit':
                print("Exiting the countdown timer. Goodbye!")
                break

            seconds = int(duration_input)

            if seconds <= 0:
                print("Please enter a positive number of seconds.")
                continue

            if seconds > MAX_SECONDS:
                print(f"Duration too long. Clamping to {MAX_SECONDS} seconds.")
                seconds = MAX_SECONDS

            run_countdown(seconds)

        except ValueError:
            print("Invalid input. Please enter a whole number or 'exit'.")


if __name__ == "__main__":
    main()
