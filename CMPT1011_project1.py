# Tic-Tac-Toe Game
'''
Team Number: 
Team Member 1: Harjoban Singh Jawanda
Team Member 2: Komalpreet Kaur
'''  

# Initialize the board
def initialize_board():
    """
    Initialize the board with empty spaces
    Returns:
        list: A list of 9 spaces representing the board
    """
    return [' '] * 9

# Display the board
def display_board(board):
    """
    Print the current board state to the console
    """
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

# Check if the board is full
def is_board_full(board):
    """
    Determine if there are no empty spaces left
    Returns:
        bool: True if the board has no spaces, False otherwise
    """
    return all(cell != ' ' for cell in board)

# Check for a win condition
def check_win(board, player):
    """
    Check if the given player has a winning combination
    Parameters:
        board (list): Current board state
        player (str): 'X' or 'O'
    Returns:
        bool: True if player has won, False otherwise
    """
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in wins)

# Get and validate player input
def get_player_input(board, player):
    """
    Prompt for a move and validate it
    Returns:
        int: Index 0-8 of valid move
    """
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input: please enter a number between 1 and 9.")
                continue
            idx = move - 1
            if board[idx] != ' ':
                print("That position is already taken. Choose another.")
                continue
            return idx
        except ValueError:
            print("Invalid input: please enter a valid integer.")

# Main game loop
def play_game():
    """
    Run the Tic-Tac-Toe game until the user chooses to quit
    """
    while True:
        board = initialize_board()
        current_player = 'X'
        game_over = False

        while not game_over:
            display_board(board)
            idx = get_player_input(board, current_player)
            board[idx] = current_player

            # Check win
            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!\n")
                game_over = True
                continue

            # Check draw
            if is_board_full(board):
                display_board(board)
                print("It's a draw!\n")
                break

            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'

        # Ask to play again
        again = input("Do you want to play again? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Thanks for playing!")
            break

# Entry point
if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!\n")
    play_game()
