"""Translate text to Morse code and Morse code back to text."""


MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.',
}

TEXT_FROM_MORSE = {code: char for char, code in MORSE_CODE.items()}


def text_to_morse(text):
    words = text.upper().split(" ")
    morse_words = []
    for word in words:
        letters = [MORSE_CODE[char] for char in word if char in MORSE_CODE]
        morse_words.append(" ".join(letters))
    return " / ".join(morse_words)


def morse_to_text(morse):
    words = morse.strip().split(" / ")
    text_words = []
    for word in words:
        letters = [TEXT_FROM_MORSE[code] for code in word.split() if code in TEXT_FROM_MORSE]
        text_words.append("".join(letters))
    return " ".join(text_words)


def main():
    print("Welcome to the Morse Code Translator!")
    while True:
        try:
            mode = input("Choose mode ('encode', 'decode') or 'exit' to quit: ").strip().lower()

            if mode == 'exit':
                print("Exiting the Morse Code Translator. Goodbye!")
                break

            if mode not in ('encode', 'decode'):
                print("Invalid mode. Please try again.")
                continue

            if mode == 'encode':
                text = input("Enter text to convert to Morse code: ")
                print(f"Morse code: {text_to_morse(text)}")
            else:
                morse = input("Enter Morse code (letters separated by spaces, words by ' / '): ")
                print(f"Text: {morse_to_text(morse)}")

        except (ValueError, KeyError):
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
