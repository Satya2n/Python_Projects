"""Compute compound interest given principal, annual rate, compounding frequency, and years."""


def compound_amount(principal, annual_rate, times_per_year, years):
    rate_decimal = annual_rate / 100
    return principal * (1 + rate_decimal / times_per_year) ** (times_per_year * years)


def main():
    print("Welcome to the Compound Interest Calculator!")
    while True:
        try:
            principal_input = input("Enter principal amount (or 'exit' to quit): ").strip()

            if principal_input.lower() == 'exit':
                print("Exiting the Compound Interest Calculator. Goodbye!")
                break

            principal = float(principal_input)
            annual_rate = float(input("Enter annual interest rate (%): "))
            times_per_year = int(input("Enter number of times compounded per year: "))
            years = float(input("Enter number of years: "))

            if principal <= 0 or times_per_year <= 0 or years <= 0:
                print("Principal, compounding frequency, and years must be positive.")
                continue

            final_amount = compound_amount(principal, annual_rate, times_per_year, years)
            interest_earned = final_amount - principal

            print(f"Final amount: {final_amount:.2f}")
            print(f"Interest earned: {interest_earned:.2f}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Compounding frequency cannot be zero.")


if __name__ == "__main__":
    main()
