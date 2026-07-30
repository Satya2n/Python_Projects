"""Simple text-based stopwatch supporting start, stop, reset, and exit."""

import time


def main():
    print("Welcome to the Stopwatch!")
    print("Commands: start, stop, reset, exit")

    start_time = None
    elapsed = 0.0
    running = False

    while True:
        try:
            command = input("Enter command: ").strip().lower()

            if command == 'exit':
                print("Exiting the stopwatch. Goodbye!")
                break

            elif command == 'start':
                if running:
                    print("Stopwatch is already running.")
                else:
                    start_time = time.perf_counter()
                    running = True
                    print("Stopwatch started.")

            elif command == 'stop':
                if not running:
                    print("Stopwatch is not running. Type 'start' first.")
                else:
                    elapsed += time.perf_counter() - start_time
                    running = False
                    print(f"Stopped. Elapsed time: {elapsed:.2f} seconds.")

            elif command == 'reset':
                start_time = None
                elapsed = 0.0
                running = False
                print("Stopwatch reset.")

            else:
                print("Unknown command. Use: start, stop, reset, exit")

        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
