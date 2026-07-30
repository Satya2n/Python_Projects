"""Menu-driven command-line prime number checker and lister."""

import math


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(math.isqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def primes_up_to(limit):
    return [number for number in range(2, limit + 1) if is_prime(number)]


def main():
    print("Welcome to the prime checker!")
    print("1. Check if a number is prime")
    print("2. List all primes up to N")
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
            if choice == '1':
                number = int(input("Enter a number: "))
                if is_prime(number):
                    print(f"{number} is prime.")
                else:
                    print(f"{number} is not prime.")
            else:
                limit = int(input("List primes up to: "))
                if limit < 2:
                    print("No primes below 2.")
                else:
                    print(f"Primes up to {limit}: {primes_up_to(limit)}")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
