"""Check whether a year is a leap year and list leap years within a range."""


def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    return True


def leap_years_in_range(start, end):
    return [year for year in range(start, end + 1) if is_leap_year(year)]


def main():
    print("Welcome to the Leap Year Checker!")
    print("Commands: check <year>, range <start> <end>, exit")
    while True:
        try:
            entry = input("Enter a command: ").strip()

            if entry.lower() == 'exit':
                print("Exiting the Leap Year Checker. Goodbye!")
                break

            parts = entry.split()

            if not parts:
                print("Please enter a command.")
                continue

            command = parts[0].lower()

            if command == 'check' and len(parts) == 2:
                year = int(parts[1])
                if is_leap_year(year):
                    print(f"{year} IS a leap year.")
                else:
                    print(f"{year} is NOT a leap year.")

            elif command == 'range' and len(parts) == 3:
                start = int(parts[1])
                end = int(parts[2])
                if start > end:
                    start, end = end, start
                years = leap_years_in_range(start, end)
                if years:
                    print(f"Leap years between {start} and {end}: {', '.join(str(y) for y in years)}")
                else:
                    print(f"No leap years found between {start} and {end}.")

            elif len(parts) == 1 and parts[0].lstrip('-').isdigit():
                year = int(parts[0])
                if is_leap_year(year):
                    print(f"{year} IS a leap year.")
                else:
                    print(f"{year} is NOT a leap year.")

            else:
                print("Usage: check <year>  OR  range <start> <end>  OR just enter a year")

        except ValueError:
            print("Invalid input. Please enter valid whole numbers for years.")


if __name__ == "__main__":
    main()
