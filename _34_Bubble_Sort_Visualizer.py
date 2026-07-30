"""Visualizes the bubble sort algorithm by printing the array after every swap."""


def bubble_sort_visualized(numbers):
    arr = list(numbers)
    n = len(arr)
    step = 0

    print(f"Starting array: {arr}")

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                step += 1
                print(f"Step {step}: swapped positions {j} and {j + 1} -> {arr}")

        if not swapped:
            break

    return arr


def main():
    print("Welcome to the Bubble Sort Visualizer!")
    while True:
        try:
            raw = input("Enter numbers separated by spaces (or 'exit' to quit): ").strip()

            if raw.lower() == 'exit':
                print("Exiting the Bubble Sort Visualizer. Goodbye!")
                break

            if not raw:
                print("Please enter at least one number.")
                continue

            numbers = [float(token) for token in raw.split()]
            numbers = [int(n) if n.is_integer() else n for n in numbers]

            sorted_numbers = bubble_sort_visualized(numbers)
            print(f"Final sorted array: {sorted_numbers}")

        except ValueError:
            print("Invalid input. Please enter numeric values separated by spaces.")


if __name__ == "__main__":
    main()
