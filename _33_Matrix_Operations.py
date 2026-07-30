"""Menu-driven matrix calculator supporting addition, subtraction, and multiplication."""


def read_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: ").strip())
    cols = int(input(f"Enter number of columns for Matrix {name}: ").strip())

    if rows <= 0 or cols <= 0:
        raise ValueError("Matrix dimensions must be positive.")

    matrix = []
    for r in range(rows):
        row_input = input(f"Enter row {r + 1} of Matrix {name} "
                           f"({cols} space-separated numbers): ").strip()
        row = [float(value) for value in row_input.split()]

        if len(row) != cols:
            raise ValueError(f"Expected {cols} numbers, got {len(row)}.")

        matrix.append(row)

    return matrix


def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def subtract_matrices(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiply_matrices(a, b):
    rows_a, cols_a = len(a), len(a[0])
    cols_b = len(b[0])
    result = [[0.0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(cols_a))

    return result


def print_matrix(matrix):
    for row in matrix:
        formatted = " ".join(
            str(int(v)) if float(v).is_integer() else f"{v:.2f}" for v in row
        )
        print(formatted)


def main():
    print("Welcome to the Matrix Operations Calculator!")
    print("Commands: add, subtract, multiply, exit")

    while True:
        try:
            command = input("Choose operation (add, subtract, multiply) or 'exit' to quit: ").strip().lower()

            if command == 'exit':
                print("Exiting the matrix calculator. Goodbye!")
                break

            if command not in ('add', 'subtract', 'multiply'):
                print("Invalid operation. Please try again.")
                continue

            matrix_a = read_matrix('A')
            matrix_b = read_matrix('B')

            if command in ('add', 'subtract'):
                if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
                    print("Matrices must have the same dimensions for this operation.")
                    continue

                result = add_matrices(matrix_a, matrix_b) if command == 'add' \
                    else subtract_matrices(matrix_a, matrix_b)

            else:
                if len(matrix_a[0]) != len(matrix_b):
                    print("Number of columns in Matrix A must match number of rows in Matrix B.")
                    continue

                result = multiply_matrices(matrix_a, matrix_b)

            print("Result:")
            print_matrix(result)

        except ValueError as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
