"""Two-player command-line tic-tac-toe with win and draw detection."""

WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def new_board():
    return [str(i + 1) for i in range(9)]


def print_board(board):
    rows = [board[i:i + 3] for i in range(0, 9, 3)]
    print()
    for i, row in enumerate(rows):
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print()


def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    return all(cell in ('X', 'O') for cell in board)


def play_game():
    board = new_board()
    current_player = 'X'

    while True:
        print_board(board)
        try:
            move_input = input(f"Player {current_player}, choose a position (1-9) or 'exit' to quit: ").strip().lower()
        except EOFError:
            return False

        if move_input == 'exit':
            return False

        try:
            position = int(move_input)
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        if position < 1 or position > 9:
            print("Please choose a number between 1 and 9.")
            continue

        index = position - 1
        if board[index] in ('X', 'O'):
            print("That spot is already taken. Choose another.")
            continue

        board[index] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return True

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            return True

        current_player = 'O' if current_player == 'X' else 'X'


def main():
    print("Welcome to Tic-Tac-Toe! Positions are numbered 1-9, left to right, top to bottom.")
    while True:
        exited = not play_game()
        if exited:
            print("Exiting the game. Goodbye!")
            break

        try:
            again = input("Play again? [Y/n]: ").strip().lower()
        except EOFError:
            print("\nGoodbye!")
            break
        if again not in ('y', 'yes', ''):
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
