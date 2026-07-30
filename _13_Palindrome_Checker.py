"""Command-line palindrome checker for strings and numbers, ignoring case and spaces."""


def normalize(text):
    return ''.join(text.split()).lower()


def is_palindrome(text):
    normalized = normalize(text)
    return normalized == normalized[::-1]


def main():
    print("Welcome to the palindrome checker!")
    print("Enter a word, phrase, or number to check (or 'exit' to quit).")

    while True:
        try:
            entry = input("\nEnter text: ").strip()
        except EOFError:
            print("\nGoodbye!")
            break

        if entry.lower() == 'exit':
            print("Goodbye!")
            break

        if not entry:
            print("Please enter some text.")
            continue

        if is_palindrome(entry):
            print(f"'{entry}' is a palindrome!")
        else:
            print(f"'{entry}' is not a palindrome.")


if __name__ == "__main__":
    main()
