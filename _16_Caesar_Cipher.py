"""Encode or decode text using a Caesar cipher with a user-supplied shift."""


def shift_char(char, shift):
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    if char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    return char


def caesar_encode(text, shift):
    return "".join(shift_char(char, shift) for char in text)


def caesar_decode(text, shift):
    return "".join(shift_char(char, -shift) for char in text)


def main():
    print("Welcome to the Caesar Cipher!")
    while True:
        try:
            mode = input("Choose mode ('encode', 'decode') or 'exit' to quit: ").strip().lower()

            if mode == 'exit':
                print("Exiting the Caesar Cipher. Goodbye!")
                break

            if mode not in ('encode', 'decode'):
                print("Invalid mode. Please try again.")
                continue

            text = input("Enter the text: ")
            shift = int(input("Enter the shift (integer): "))

            if mode == 'encode':
                result = caesar_encode(text, shift)
            else:
                result = caesar_decode(text, shift)

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Shift must be an integer.")


if __name__ == "__main__":
    main()
