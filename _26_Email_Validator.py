"""Validates whether user-entered strings look like proper email addresses."""

import re

EMAIL_PATTERN = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')


def diagnose(email):
    if '@' not in email:
        return "missing '@' symbol"

    local, _, domain = email.partition('@')

    if not local:
        return "missing local part before '@'"

    if not domain:
        return "missing domain part after '@'"

    if '.' not in domain:
        return "missing domain extension (e.g. '.com')"

    if domain.startswith('.') or domain.endswith('.'):
        return "domain has misplaced dot"

    if ' ' in email:
        return "email contains spaces"

    return "contains invalid characters"


def main():
    print("Welcome to the Email Validator!")
    while True:
        try:
            email = input("Enter an email address (or 'exit' to quit): ").strip()

            if email.lower() == 'exit':
                print("Exiting the email validator. Goodbye!")
                break

            if not email:
                print("Input cannot be empty.")
                continue

            if EMAIL_PATTERN.match(email):
                print(f"'{email}' looks like a valid email address.")
            else:
                reason = diagnose(email)
                print(f"'{email}' is not a valid email address: {reason}.")

        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
