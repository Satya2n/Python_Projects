"""Rates the strength of a user-entered password and gives improvement feedback."""

import string


def analyze(password):
    checks = {
        'length': len(password) >= 8,
        'upper': any(c in string.ascii_uppercase for c in password),
        'lower': any(c in string.ascii_lowercase for c in password),
        'digit': any(c in string.digits for c in password),
        'symbol': any(c not in string.ascii_letters + string.digits for c in password),
    }
    return checks


def rate(checks):
    score = sum(checks.values())

    if len(checks) == score:
        return "Very Strong"
    elif score >= 4:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"


def feedback(checks):
    messages = []

    if not checks['length']:
        messages.append("use at least 8 characters")
    if not checks['upper']:
        messages.append("add an uppercase letter")
    if not checks['lower']:
        messages.append("add a lowercase letter")
    if not checks['digit']:
        messages.append("add a digit")
    if not checks['symbol']:
        messages.append("add a symbol (e.g. !, @, #)")

    return messages


def main():
    print("Welcome to the Password Strength Checker!")
    while True:
        try:
            password = input("Enter a password (or 'exit' to quit): ")

            if password.strip().lower() == 'exit':
                print("Exiting the password checker. Goodbye!")
                break

            if not password:
                print("Password cannot be empty.")
                continue

            checks = analyze(password)
            strength = rate(checks)
            print(f"Password strength: {strength}")

            tips = feedback(checks)
            if tips:
                print("Suggestions: " + "; ".join(tips))
            else:
                print("Great job! Your password covers all the basics.")

        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
