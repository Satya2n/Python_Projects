"""Uses an explicit stack to check whether a string of brackets is balanced."""

PAIRS = {
    ')': '(',
    ']': '[',
    '}': '{',
}
OPENERS = set(PAIRS.values())
CLOSERS = set(PAIRS.keys())


def is_balanced(text):
    stack = []

    for char in text:
        if char in OPENERS:
            stack.append(char)
            print(f"  push '{char}' -> stack: {stack}")

        elif char in CLOSERS:
            if not stack:
                print(f"  found '{char}' but stack is empty -> unbalanced")
                return False

            top = stack.pop()
            print(f"  pop '{top}' to match '{char}' -> stack: {stack}")

            if top != PAIRS[char]:
                print(f"  '{top}' does not match '{char}' -> unbalanced")
                return False

    if stack:
        print(f"  stack not empty at end: {stack} -> unbalanced")
        return False

    return True


def main():
    print("Welcome to the Balanced Parentheses Checker!")
    while True:
        try:
            text = input("Enter a string of brackets ( ) [ ] { } (or 'exit' to quit): ").strip()

            if text.lower() == 'exit':
                print("Exiting the Balanced Parentheses Checker. Goodbye!")
                break

            if not text:
                print("Please enter a non-empty string.")
                continue

            print("Processing:")
            if is_balanced(text):
                print(f"'{text}' is balanced.")
            else:
                print(f"'{text}' is NOT balanced.")

        except Exception:
            print("Something went wrong with that input. Please try again.")


if __name__ == "__main__":
    main()
