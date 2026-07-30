"""Collect subject scores, compute the average, and assign a letter grade."""


def score_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def average_score(subjects):
    if not subjects:
        return 0.0
    return sum(score for _, score in subjects) / len(subjects)


def print_breakdown(subjects):
    for name, score in subjects:
        print(f"  {name}: {score:.1f} ({score_to_grade(score)})")


def main():
    print("Welcome to the Grade Calculator!")
    print("Enter a subject name and score, one at a time. Type 'done' as the subject name to finish, or 'exit' to quit.")

    while True:
        subjects = []
        try:
            while True:
                name = input("Subject name (or 'done' to finish, 'exit' to quit): ").strip()

                if name.lower() == 'exit':
                    print("Exiting the Grade Calculator. Goodbye!")
                    return

                if name.lower() == 'done':
                    break

                if not name:
                    print("Subject name cannot be empty.")
                    continue

                score = float(input(f"Score for {name} (0-100): ").strip())

                if score < 0 or score > 100:
                    print("Score must be between 0 and 100.")
                    continue

                subjects.append((name, score))

            if not subjects:
                print("No subjects entered.")
                continue

            average = average_score(subjects)
            overall_grade = score_to_grade(average)

            print("\nPer-subject breakdown:")
            print_breakdown(subjects)
            print(f"\nAverage score: {average:.2f}")
            print(f"Overall grade: {overall_grade}")
            print()

        except ValueError:
            print("Invalid input. Please enter a numeric score.")


if __name__ == "__main__":
    main()
