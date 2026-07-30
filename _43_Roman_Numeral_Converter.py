"""Converts integers 1-3999 to Roman numerals and back, menu-driven."""

VALUE_SYMBOLS = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
]

SYMBOL_VALUES = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000,
}


def int_to_roman(number):
    if not 1 <= number <= 3999:
        raise ValueError("Number must be between 1 and 3999")

    result = []
    remaining = number
    for value, symbol in VALUE_SYMBOLS:
        if remaining == 0:
            break
        count, remaining = divmod(remaining, value)
        result.append(symbol * count)

    return "".join(result)


def roman_to_int(roman):
    roman = roman.upper().strip()
    if not roman or any(char not in SYMBOL_VALUES for char in roman):
        raise ValueError("Invalid Roman numeral characters")

    total = 0
    previous_value = 0
    for char in reversed(roman):
        value = SYMBOL_VALUES[char]
        if value < previous_value:
            total -= value
        else:
            total += value
            previous_value = value

    if int_to_roman(total) != roman:
        raise ValueError("Not a valid Roman numeral")

    return total


def main():
    print("Welcome to the Roman Numeral Converter!")
    menu = (
        "\nChoose an option:\n"
        "  1. Integer to Roman numeral\n"
        "  2. Roman numeral to integer\n"
        "  exit. Quit\n"
    )

    while True:
        try:
            print(menu)
            choice = input("Enter your choice: ").strip().lower()

            if choice == 'exit':
                print("Exiting the Roman Numeral Converter. Goodbye!")
                break

            elif choice == '1':
                number = int(input("Enter an integer (1-3999): ").strip())
                roman = int_to_roman(number)
                print(f"{number} in Roman numerals is: {roman}")

            elif choice == '2':
                roman = input("Enter a Roman numeral: ").strip()
                number = roman_to_int(roman)
                print(f"{roman.upper()} as an integer is: {number}")

            else:
                print("Invalid choice. Please try again.")

        except ValueError as error:
            print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
