import random

def hill_climbing(board):
    moves = available_moves(board)
    best_move = None
    best_value = -float("inf")
    for move in moves:
        board[move] = 'X'
        value = evaluate(board)
        board[move] = ' '
        if value > best_value:
            best_value = value
            best_move = move
    return best_move, best_value

def evaluate(board):
    # Sample scoring function
    return random.randint(0, 10)

def available_moves(board):
    return [i for i in range(len(board)) if board[i] == ' ']

# Game board represented as a 1D list
board = [' '] * 9
best_move, best_value = hill_climbing(board)
print("Best state:", best_move)
print("Best value:", best_value)