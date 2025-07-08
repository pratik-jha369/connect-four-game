ROWS = 6
COLS = 7

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")
    print(" " + " ".join(str(i + 1) for i in range(COLS)))

def is_valid_column(board, col):
    return board[0][col] == " "

def get_next_open_row(board, col):
    for r in reversed(range(ROWS)):
        if board[r][col] == " ":
            return r
    return -1

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True
    # Vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True
    # Positive diagonal
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
    # Negative diagonal
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][c] != " " for c in range(COLS))

def play_game():
    board = create_board()
    game_over = False
    turn = 0  # Player 1 starts

    print("🔴 Connect Four Game 🎮")
    print_board(board)

    while not game_over:
        player = turn % 2 + 1
        piece = "X" if player == 1 else "O"

        try:
            col = int(input(f"Player {player} [{piece}], choose column (1-7): ")) - 1
            if col < 0 or col >= COLS:
                print("🚫 Invalid column. Choose between 1 and 7.")
                continue
        except ValueError:
            print("🚫 Invalid input. Enter a number.")
            continue

        if is_valid_column(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, piece)

            print_board(board)

            if winning_move(board, piece):
                print(f"🎉 Player {player} ({piece}) wins!")
                game_over = True
            elif is_draw(board):
                print("🤝 It's a draw!")
                game_over = True
            else:
                turn += 1
        else:
            print("🚫 Column is full. Try another one.")

if __name__== "__main__":
    play_game()
