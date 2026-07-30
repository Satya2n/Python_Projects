"""Demonstrates binary search by printing the low/high/mid comparisons for each step."""


def binary_search_demo(sorted_numbers, target):
    low = 0
    high = len(sorted_numbers) - 1
    step = 0

    while low <= high:
        step += 1
        mid = (low + high) // 2
        mid_value = sorted_numbers[mid]
        print(f"Step {step}: low={low}, high={high}, mid={mid} (value={mid_value})")

        if mid_value == target:
            print(f"  {mid_value} == {target} -> target found!")
            return mid
        elif mid_value < target:
            print(f"  {mid_value} < {target} -> searching right half")
            low = mid + 1
        else:
            print(f"  {mid_value} > {target} -> searching left half")
            high = mid - 1

    return -1


def main():
    print("Welcome to the Binary Search Demo!")
    while True:
        try:
            raw = input("Enter a sorted list of numbers separated by spaces (or 'exit' to quit): ").strip()

            if raw.lower() == 'exit':
                print("Exiting the Binary Search Demo. Goodbye!")
                break

            if not raw:
                print("Please enter at least one number.")
                continue

            numbers = [float(token) for token in raw.split()]
            numbers = [int(n) if n.is_integer() else n for n in numbers]

            if numbers != sorted(numbers):
                print("The list must be sorted in ascending order. Please try again.")
                continue

            target_raw = input("Enter the target value to search for: ").strip()
            target = float(target_raw)
            target = int(target) if target.is_integer() else target

            index = binary_search_demo(numbers, target)
            if index == -1:
                print(f"{target} was not found in the list.")
            else:
                print(f"{target} was found at index {index}.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
