import random

board = [' ' for _ in range(9)]

def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def user_move():
    while True:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1
            if move >= 0 and move < 9:
                if board[move] == ' ':
                    board[move] = 'X'
                    break
                else:
                    print("That space is already occupied.")
            else:
                print("Enter a number between 1 and 9.")
        except ValueError:
            print("Enter a number between 1 and 9.")

def ai_move():
    # AI uses simple logic: it checks if it can win, block player from winning, or just choose random available spot
    possible_moves = [i for i, x in enumerate(board) if x == ' ']
    for letter in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = letter
            if check_winner(board_copy, letter):
                board[i] = 'O'
                return
    corners_open = []
    for i in possible_moves:
        if i in [0,2,6,8]:
            corners_open.append(i)
    if len(corners_open) > 0:
        board[random.choice(corners_open)] = 'O'
        return
    if 4 in possible_moves:
        board[4] = 'O'
        return
    edges_open = []
    for i in possible_moves:
        if i in [1,3,5,7]:
            edges_open.append(i)
    if len(edges_open) > 0:
        board[random.choice(edges_open)] = 'O'
        return

def check_winner(board, letter):
    return (board[0] == letter and board[1] == letter and board[2] == letter) or \
           (board[3] == letter and board[4] == letter and board[5] == letter) or \
           (board[6] == letter and board[7] == letter and board[8] == letter) or \
           (board[0] == letter and board[3] == letter and board[6] == letter) or \
           (board[1] == letter and board[4] == letter and board[7] == letter) or \
           (board[2] == letter and board[5] == letter and board[8] == letter) or \
           (board[0] == letter and board[4] == letter and board[8] == letter) or \
           (board[2] == letter and board[4] == letter and board[6] == letter)

def is_board_full(board):
    return ' ' not in board

print_board()

while not is_board_full(board):
    if not check_winner(board, 'O'):
        user_move()
        print_board()
    else:
        print("Sorry, the computer won this time.")
        break

    if not check_winner(board, 'X'):
        ai_move()
        print_board()
    else:
        print("Congratulations, you won!")
        break

    if is_board_full(board):
        print("Tie game.")
