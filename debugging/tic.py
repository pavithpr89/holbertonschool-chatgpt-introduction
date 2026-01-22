def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] != " " and all(cell == row[0] for cell in row):
            return True

    # Check columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    # Check diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def board_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input with validation
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input! Please enter numbers 0, 1, or 2.")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid coordinates! Must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for tie
        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


# Run the game
tic_tac_toe()
