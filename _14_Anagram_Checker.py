"""Check whether two user-entered words or phrases are anagrams of each other."""


def normalize(text):
    return sorted(text.lower().replace(" ", ""))


def is_anagram(first, second):
    return normalize(first) == normalize(second)


def main():
    print("Welcome to the Anagram Checker!")
    while True:
        try:
            first = input("Enter the first word/phrase (or 'exit' to quit): ").strip()

            if first.lower() == 'exit':
                print("Exiting the Anagram Checker. Goodbye!")
                break

            second = input("Enter the second word/phrase: ").strip()

            if second.lower() == 'exit':
                print("Exiting the Anagram Checker. Goodbye!")
                break

            if not first or not second:
                print("Both entries must be non-empty. Please try again.")
                continue

            if is_anagram(first, second):
                print(f"'{first}' and '{second}' ARE anagrams.")
            else:
                print(f"'{first}' and '{second}' are NOT anagrams.")

        except (ValueError, KeyboardInterrupt, EOFError) as error:
            print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
