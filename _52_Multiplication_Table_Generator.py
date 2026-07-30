"""Print the multiplication table for a user-entered number up to a chosen range."""


def generate_table(number, upper_limit):
    return [(i, number * i) for i in range(1, upper_limit + 1)]


def print_table(number, upper_limit):
    for multiplier, product in generate_table(number, upper_limit):
        print(f"{number} x {multiplier} = {product}")


def main():
    print("Welcome to the Multiplication Table Generator!")
    while True:
        try:
            entry = input("Enter a number (or 'exit' to quit): ").strip()

            if entry.lower() == 'exit':
                print("Exiting the Multiplication Table Generator. Goodbye!")
                break

            number = int(entry)

            limit_entry = input("Enter the range to generate up to (e.g. 10): ").strip()

            if limit_entry.lower() == 'exit':
                print("Exiting the Multiplication Table Generator. Goodbye!")
                break

            upper_limit = int(limit_entry)

            if upper_limit < 1:
                print("Range must be a positive integer.")
                continue

            print_table(number, upper_limit)

        except ValueError:
            print("Invalid input. Please enter valid integers.")


if __name__ == "__main__":
    main()
