def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_tic_tac_toe():
    print("Welcome to Tic Tac Toe!")

    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'

        while True:
            print_board(board)

            position = input(f"Player {current_player}, enter your move (1-9): ")

            if not position.isdigit() or not (1 <= int(position) <= 9):
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            position = int(position) - 1
            row, col = divmod(position, 3)

            if board[row][col] == ' ':
                board[row][col] = current_player
            else:
                print("Invalid move. The position is already taken. Try again.")
                continue

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if _name_ == "_main_":
    play_tic_tac_toe()