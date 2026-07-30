"""Convert a number between binary, octal, decimal, and hexadecimal."""


BASES = {
    'binary': 2,
    'octal': 8,
    'decimal': 10,
    'hexadecimal': 16,
}


def to_decimal(value, base):
    return int(value, base)


def from_decimal(value, base):
    if base == 2:
        return bin(value)[2:]
    if base == 8:
        return oct(value)[2:]
    if base == 16:
        return hex(value)[2:]
    return str(value)


def convert(value, from_base_name, to_base_name):
    from_base = BASES[from_base_name]
    to_base = BASES[to_base_name]
    decimal_value = to_decimal(value, from_base)
    return from_decimal(decimal_value, to_base)


def main():
    print("Welcome to the Number Base Converter!")
    print(f"Supported bases: {', '.join(BASES)}")
    while True:
        try:
            from_base_name = input("Convert from base (or 'exit' to quit): ").strip().lower()

            if from_base_name == 'exit':
                print("Exiting the Number Base Converter. Goodbye!")
                break

            if from_base_name not in BASES:
                print("Invalid base. Please try again.")
                continue

            to_base_name = input("Convert to base: ").strip().lower()

            if to_base_name not in BASES:
                print("Invalid base. Please try again.")
                continue

            value = input(f"Enter the {from_base_name} number: ").strip()

            result = convert(value, from_base_name, to_base_name)
            print(f"Result ({to_base_name}): {result}")

        except ValueError:
            print("Invalid number for the given base. Please try again.")


if __name__ == "__main__":
    main()
