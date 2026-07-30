"""Encode or decode text using a Vigenere cipher with a user-supplied keyword."""


def shift_char(char, shift):
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    if char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    return char


def vigenere_encode(text, keyword):
    result = []
    key_index = 0
    keyword = keyword.lower()
    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            result.append(shift_char(char, shift))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


def vigenere_decode(text, keyword):
    result = []
    key_index = 0
    keyword = keyword.lower()
    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('a')
            result.append(shift_char(char, -shift))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


def main():
    print("Welcome to the Vigenere Cipher!")
    while True:
        try:
            mode = input("Choose mode ('encode', 'decode') or 'exit' to quit: ").strip().lower()

            if mode == 'exit':
                print("Exiting the Vigenere Cipher. Goodbye!")
                break

            if mode not in ('encode', 'decode'):
                print("Invalid mode. Please try again.")
                continue

            text = input("Enter the text: ")
            keyword = input("Enter the keyword (letters only): ").strip()

            if not keyword.isalpha():
                print("Keyword must contain only letters. Please try again.")
                continue

            if mode == 'encode':
                result = vigenere_encode(text, keyword)
            else:
                result = vigenere_decode(text, keyword)

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
