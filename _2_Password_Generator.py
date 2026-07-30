"""Command-line random password generator with configurable length and character sets."""

import secrets
import string


def generate_password(length=12, use_digits=True, use_symbols=True):
    alphabet = string.ascii_letters
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def ask_yes_no(prompt):
    return input(prompt).strip().lower() in ('y', 'yes', '')


def main():
    print("Welcome to the password generator!")
    while True:
        try:
            length = int(input("Password length (default 12): ") or 12)
        except ValueError:
            print("Please enter a valid number.")
            continue

        use_digits = ask_yes_no("Include digits? [Y/n]: ")
        use_symbols = ask_yes_no("Include symbols? [Y/n]: ")

        print(f"Generated password: {generate_password(length, use_digits, use_symbols)}")

        if input("Generate another? [Y/n]: ").strip().lower() not in ('y', 'yes', ''):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
