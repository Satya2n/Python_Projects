"""Compute and display the prime factorization of a user-entered positive integer."""


def prime_factors(number):
    factors = []
    divisor = 2
    remaining = number

    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        divisor += 1

    if remaining > 1:
        factors.append(remaining)

    return factors


def format_factorization(number, factors):
    counts = {}
    for factor in factors:
        counts[factor] = counts.get(factor, 0) + 1

    parts = []
    for factor in sorted(counts):
        count = counts[factor]
        if count == 1:
            parts.append(str(factor))
        else:
            parts.append(f"{factor}^{count}")

    return f"{number} = " + " * ".join(parts)


def main():
    print("Welcome to the Prime Factorization tool!")
    while True:
        try:
            entry = input("Enter a positive integer (or 'exit' to quit): ").strip()

            if entry.lower() == 'exit':
                print("Exiting the Prime Factorization tool. Goodbye!")
                break

            number = int(entry)

            if number < 2:
                print("Please enter an integer greater than 1.")
                continue

            factors = prime_factors(number)

            if len(factors) == 1:
                print(f"{number} is a prime number.")
            else:
                print(format_factorization(number, factors))

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
