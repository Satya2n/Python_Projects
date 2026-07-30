"""Compute BMI from user-entered height and weight, and report the BMI category."""


def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def main():
    print("Welcome to the BMI Calculator!")
    while True:
        try:
            unit = input("Enter height unit ('cm' or 'm') or 'exit' to quit: ").strip().lower()

            if unit == 'exit':
                print("Exiting the BMI Calculator. Goodbye!")
                break

            if unit not in ('cm', 'm'):
                print("Invalid unit. Please enter 'cm' or 'm'.")
                continue

            height = float(input(f"Enter height in {unit}: "))
            weight = float(input("Enter weight in kg: "))

            if height <= 0 or weight <= 0:
                print("Height and weight must be positive numbers.")
                continue

            height_m = height / 100 if unit == 'cm' else height

            bmi = calculate_bmi(weight, height_m)
            category = bmi_category(bmi)

            print(f"Your BMI is: {bmi:.2f}")
            print(f"Category: {category}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
