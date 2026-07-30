"""Compute monthly EMI for a loan given principal, annual interest rate, and tenure in months."""


def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / 12 / 100

    if monthly_rate == 0:
        return principal / tenure_months

    numerator = principal * monthly_rate * (1 + monthly_rate) ** tenure_months
    denominator = (1 + monthly_rate) ** tenure_months - 1
    return numerator / denominator


def main():
    print("Welcome to the Loan EMI Calculator!")
    while True:
        try:
            principal_input = input("Enter loan principal (or 'exit' to quit): ").strip()

            if principal_input.lower() == 'exit':
                print("Exiting the Loan EMI Calculator. Goodbye!")
                break

            principal = float(principal_input)
            annual_rate = float(input("Enter annual interest rate (%): "))
            tenure_months = int(input("Enter tenure in months: "))

            if principal <= 0 or tenure_months <= 0 or annual_rate < 0:
                print("Principal and tenure must be positive, and rate cannot be negative.")
                continue

            emi = calculate_emi(principal, annual_rate, tenure_months)
            total_payment = emi * tenure_months
            total_interest = total_payment - principal

            print(f"Monthly EMI: {emi:.2f}")
            print(f"Total payment: {total_payment:.2f}")
            print(f"Total interest: {total_interest:.2f}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
