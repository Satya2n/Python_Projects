"""Command-line unit converter for length, weight, and temperature."""

LENGTH_TO_METERS = {
    'm': 1,
    'km': 1000,
    'cm': 0.01,
    'mile': 1609.34,
    'ft': 0.3048,
}

WEIGHT_TO_GRAMS = {
    'g': 1,
    'kg': 1000,
    'lb': 453.592,
    'oz': 28.3495,
}


def convert_length(value, from_unit, to_unit):
    meters = value * LENGTH_TO_METERS[from_unit]
    return meters / LENGTH_TO_METERS[to_unit]


def convert_weight(value, from_unit, to_unit):
    grams = value * WEIGHT_TO_GRAMS[from_unit]
    return grams / WEIGHT_TO_GRAMS[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'c' and to_unit == 'f':
        return value * 9 / 5 + 32
    if from_unit == 'f' and to_unit == 'c':
        return (value - 32) * 5 / 9
    if from_unit == 'c' and to_unit == 'k':
        return value + 273.15
    if from_unit == 'k' and to_unit == 'c':
        return value - 273.15
    raise ValueError(f"Unsupported temperature conversion: {from_unit} -> {to_unit}")


CATEGORIES = {
    'length': (convert_length, LENGTH_TO_METERS.keys()),
    'weight': (convert_weight, WEIGHT_TO_GRAMS.keys()),
    'temperature': (convert_temperature, ('c', 'f', 'k')),
}


def main():
    print("Welcome to the unit converter!")
    print(f"Categories: {', '.join(CATEGORIES)}")
    while True:
        category = input("Choose a category (or 'exit' to quit): ").strip().lower()

        if category == 'exit':
            print("Goodbye!")
            break

        if category not in CATEGORIES:
            print("Unknown category. Please try again.")
            continue

        convert, units = CATEGORIES[category]
        print(f"Available units: {', '.join(units)}")

        try:
            value = float(input("Value to convert: "))
            from_unit = input("From unit: ").strip().lower()
            to_unit = input("To unit: ").strip().lower()
            result = convert(value, from_unit, to_unit)
            print(f"Result: {result:.4f} {to_unit}")
        except (ValueError, KeyError):
            print("Invalid input. Please check the value and unit names.")


if __name__ == "__main__":
    main()
