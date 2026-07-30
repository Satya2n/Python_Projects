"""Compute tip amount and total bill, split between a number of people."""


def calculate_tip(bill_amount, tip_percent):
    return bill_amount * tip_percent / 100


def main():
    print("Welcome to the Tip Calculator!")
    while True:
        try:
            bill_input = input("Enter the bill amount (or 'exit' to quit): ").strip()

            if bill_input.lower() == 'exit':
                print("Exiting the Tip Calculator. Goodbye!")
                break

            bill_amount = float(bill_input)
            tip_percent = float(input("Enter tip percentage: "))
            num_people = int(input("Enter number of people to split between: "))

            if bill_amount <= 0 or tip_percent < 0 or num_people <= 0:
                print("Bill and people count must be positive, and tip cannot be negative.")
                continue

            tip_amount = calculate_tip(bill_amount, tip_percent)
            total_bill = bill_amount + tip_amount
            per_person = total_bill / num_people

            print(f"Tip amount: {tip_amount:.2f}")
            print(f"Total bill: {total_bill:.2f}")
            print(f"Amount per person: {per_person:.2f}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
