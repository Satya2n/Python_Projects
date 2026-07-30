"""Simple command-line calculator supporting +, -, *, / with graceful error handling."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def main():
    print("Welcome to the simple calculator!")
    while True:
        try:
            operation = input("Choose operation (+, -, *, /) or 'exit' to quit: ").strip().lower()

            if operation == 'exit':
                print("Exiting the calculator. Goodbye!")
                break

            if operation not in operations:
                print("Invalid operation. Please try again.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = operations[operation](num1, num2)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
