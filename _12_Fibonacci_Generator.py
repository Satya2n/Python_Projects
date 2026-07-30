"""Menu-driven command-line Fibonacci sequence generator."""


def fibonacci_sequence(count):
    sequence = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    print("Welcome to the Fibonacci generator!")
    print("1. Print the first N Fibonacci numbers")
    print("2. Get the Nth Fibonacci number")
    print("Type 'exit' at any prompt to quit.")

    while True:
        try:
            choice = input("\nChoose an option (1 or 2, or 'exit'): ").strip().lower()
        except EOFError:
            print("\nGoodbye!")
            break

        if choice == 'exit':
            print("Goodbye!")
            break

        if choice not in ('1', '2'):
            print("Invalid option. Please choose 1 or 2.")
            continue

        try:
            n = int(input("Enter N: "))
            if n < 0:
                print("Please enter a non-negative number.")
                continue

            if choice == '1':
                print(f"First {n} Fibonacci numbers: {fibonacci_sequence(n)}")
            else:
                print(f"The {n}th Fibonacci number is: {nth_fibonacci(n)}")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
