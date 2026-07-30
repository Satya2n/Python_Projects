"""Multiple-choice general-knowledge quiz that tracks and reports the final score."""

QUESTIONS = [
    {
        'question': "What is the capital of France?",
        'options': ["Berlin", "Madrid", "Paris", "Rome"],
        'answer': 3,
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ["Venus", "Mars", "Jupiter", "Saturn"],
        'answer': 2,
    },
    {
        'question': "What is the largest ocean on Earth?",
        'options': ["Atlantic", "Indian", "Arctic", "Pacific"],
        'answer': 4,
    },
    {
        'question': "Who wrote 'Romeo and Juliet'?",
        'options': ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        'answer': 2,
    },
    {
        'question': "What is the chemical symbol for gold?",
        'options': ["Go", "Gd", "Au", "Ag"],
        'answer': 3,
    },
    {
        'question': "How many continents are there on Earth?",
        'options': ["5", "6", "7", "8"],
        'answer': 3,
    },
    {
        'question': "What is the smallest prime number?",
        'options': ["0", "1", "2", "3"],
        'answer': 3,
    },
    {
        'question': "Which language has the most native speakers worldwide?",
        'options': ["English", "Hindi", "Mandarin Chinese", "Spanish"],
        'answer': 3,
    },
]


def ask_question(item):
    print(item['question'])
    for i, option in enumerate(item['options'], start=1):
        print(f"  {i}. {option}")

    choice = input("Your answer (1-4, or 'exit' to quit): ").strip()
    return choice


def run_quiz():
    score = 0
    total = 0
    quit_early = False

    for item in QUESTIONS:
        try:
            choice = ask_question(item)

            if choice.lower() == 'exit':
                print("Exiting the quiz early. Goodbye!")
                quit_early = True
                break

            total += 1
            selected = int(choice)

            if selected == item['answer']:
                print("Correct!\n")
                score += 1
            else:
                correct_text = item['options'][item['answer'] - 1]
                print(f"Wrong! The correct answer was: {correct_text}\n")

        except (ValueError, IndexError):
            print(f"Invalid choice, marking as wrong. The correct answer was: "
                  f"{item['options'][item['answer'] - 1]}\n")

    if total > 0:
        percentage = (score / total) * 100
        print(f"Final score: {score}/{total} ({percentage:.1f}%)")
    else:
        print("No questions were answered.")

    return quit_early


def main():
    print("Welcome to the Quiz Game!")
    print("Answer each question with a number from 1 to 4.")
    print("Type 'exit' at any question prompt to quit immediately.\n")

    while True:
        quit_early = run_quiz()

        if quit_early:
            break

        again = input("\nPlay again? (yes/exit): ").strip().lower()
        if again == 'exit' or again != 'yes':
            print("Thanks for playing. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
