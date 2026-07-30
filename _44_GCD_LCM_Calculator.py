"""Compute the GCD and LCM of two or more comma-separated user-entered integers."""

import math


def gcd_of_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = math.gcd(result, number)
    return result


def lcm_of_two(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)


def lcm_of_list(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm_of_two(result, number)
    return result


def parse_numbers(text):
    parts = [p.strip() for p in text.split(",") if p.strip()]
    return [int(p) for p in parts]


def main():
    print("Welcome to the GCD & LCM Calculator!")
    while True:
        try:
            entry = input("Enter two or more integers separated by commas (or 'exit' to quit): ").strip()

            if entry.lower() == 'exit':
                print("Exiting the GCD & LCM Calculator. Goodbye!")
                break

            numbers = parse_numbers(entry)

            if len(numbers) < 2:
                print("Please enter at least two integers.")
                continue

            result_gcd = gcd_of_list(numbers)
            result_lcm = lcm_of_list(numbers)

            numbers_str = ", ".join(str(n) for n in numbers)
            print(f"Numbers: {numbers_str}")
            print(f"GCD: {result_gcd}")
            print(f"LCM: {result_lcm}")

        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")


if __name__ == "__main__":
    main()
