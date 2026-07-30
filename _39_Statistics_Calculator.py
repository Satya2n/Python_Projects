"""Computes mean, median, mode, variance, and standard deviation for a list of numbers."""

import statistics


def compute_statistics(numbers):
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)

    try:
        mode = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode = "no unique mode"

    if len(numbers) > 1:
        variance = statistics.variance(numbers)
        stdev = statistics.stdev(numbers)
    else:
        variance = 0.0
        stdev = 0.0

    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        'stdev': stdev,
    }


def main():
    print("Welcome to the Statistics Calculator!")
    while True:
        try:
            raw = input("Enter numbers separated by spaces (or 'exit' to quit): ").strip()

            if raw.lower() == 'exit':
                print("Exiting the Statistics Calculator. Goodbye!")
                break

            if not raw:
                print("Please enter at least one number.")
                continue

            numbers = [float(token) for token in raw.split()]

            results = compute_statistics(numbers)
            print(f"Mean: {results['mean']}")
            print(f"Median: {results['median']}")
            print(f"Mode: {results['mode']}")
            print(f"Variance: {results['variance']}")
            print(f"Standard Deviation: {results['stdev']}")

        except ValueError:
            print("Invalid input. Please enter numeric values separated by spaces.")


if __name__ == "__main__":
    main()
