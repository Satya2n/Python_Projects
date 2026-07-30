"""Menu-driven toolkit of string operations: case, counts, palindrome, and more."""

VOWELS = "aeiouAEIOU"


def reverse_text(text):
    return text[::-1]


def count_vowels_consonants(text):
    vowels = sum(1 for ch in text if ch in VOWELS)
    consonants = sum(1 for ch in text if ch.isalpha() and ch not in VOWELS)
    return vowels, consonants


def remove_whitespace(text):
    return "".join(text.split())


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


def print_menu():
    print("\nString Toolkit menu:")
    print("  1. Reverse text")
    print("  2. Convert to UPPERCASE")
    print("  3. Convert to lowercase")
    print("  4. Convert to Title Case")
    print("  5. Count vowels and consonants")
    print("  6. Remove whitespace")
    print("  7. Check if palindrome")
    print("  8. Find longest word")
    print("  exit - quit the toolkit")


def main():
    print("Welcome to the String Toolkit!")
    while True:
        try:
            text = input("\nEnter text to work with (or 'exit' to quit): ")

            if text.strip().lower() == 'exit':
                print("Exiting the String Toolkit. Goodbye!")
                break

            print_menu()
            choice = input("Choose an option (1-8): ").strip()

            if choice == '1':
                print(f"Reversed: {reverse_text(text)}")
            elif choice == '2':
                print(f"Uppercase: {text.upper()}")
            elif choice == '3':
                print(f"Lowercase: {text.lower()}")
            elif choice == '4':
                print(f"Title case: {text.title()}")
            elif choice == '5':
                vowels, consonants = count_vowels_consonants(text)
                print(f"Vowels: {vowels}, Consonants: {consonants}")
            elif choice == '6':
                print(f"Without whitespace: {remove_whitespace(text)}")
            elif choice == '7':
                if is_palindrome(text):
                    print("That is a palindrome.")
                else:
                    print("That is not a palindrome.")
            elif choice == '8':
                word = longest_word(text)
                if word:
                    print(f"Longest word: {word}")
                else:
                    print("No words found.")
            else:
                print("Invalid option. Please choose a number from 1 to 8.")

        except (ValueError, KeyboardInterrupt, EOFError) as error:
            print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
