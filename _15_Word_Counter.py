"""Count words, characters, and sentences in a block of user-entered text."""


def count_words(text):
    return len(text.split())


def count_characters(text):
    with_spaces = len(text)
    without_spaces = len(text.replace(" ", ""))
    return with_spaces, without_spaces


def count_sentences(text):
    count = 0
    for char in text:
        if char in ".!?":
            count += 1
    return count


def read_multiline_text():
    print("Enter your text. Type 'END' on its own line when finished (or 'exit' to quit).")
    lines = []
    while True:
        line = input()
        if line.strip().lower() == 'exit':
            return None
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    print("Welcome to the Word Counter!")
    while True:
        try:
            text = read_multiline_text()

            if text is None:
                print("Exiting the Word Counter. Goodbye!")
                break

            if not text.strip():
                print("No text entered. Please try again.")
                continue

            words = count_words(text)
            with_spaces, without_spaces = count_characters(text)
            sentences = count_sentences(text)

            print(f"Word count: {words}")
            print(f"Character count (with spaces): {with_spaces}")
            print(f"Character count (without spaces): {without_spaces}")
            print(f"Sentence count (approx.): {sentences}")

        except (ValueError, KeyboardInterrupt, EOFError) as error:
            print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
