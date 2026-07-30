"""Command-line FizzBuzz generator for a user-specified range."""


def fizzbuzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def main():
    print("Welcome to the FizzBuzz generator!")
    while True:
        try:
            start_input = input("Enter the start of the range (or 'exit' to quit): ").strip().lower()
        except EOFError:
            print("\nGoodbye!")
            break

        if start_input == 'exit':
            print("Goodbye!")
            break

        try:
            start = int(start_input)
            end = int(input("Enter the end of the range: "))
        except ValueError:
            print("Invalid input. Please enter whole numbers.")
            continue
        except EOFError:
            print("\nGoodbye!")
            break

        if start > end:
            print("Start must be less than or equal to end.")
            continue

        results = [fizzbuzz(number) for number in range(start, end + 1)]
        print(', '.join(results))


if __name__ == "__main__":
    main()
