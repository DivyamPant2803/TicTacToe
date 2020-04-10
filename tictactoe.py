import random

def display_board(board):
    print('\n'*100)
    print('  |   |')
    print(' ' + board[1] + '| ' + board[2] + ' | ' + board[3])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(' ' + board[4] + '| ' + board[5] + ' | ' + board[6])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(' ' + board[7] + '| ' + board[8] + ' | ' + board[9])
    print('  |   |')


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, Do you want to be X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board,marker,position):
    board[position] = marker


def win_check(board,marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[3] == marker and board[6] == marker and board[9] == marker)
    )


def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'PLayer 1'


def space_check(board,position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board,turn):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input(turn+' Choose position (1-9): '))
    return position


def replay():
    return input('Do you want to play again? (Yes/No) ').lower().startswith('y')

print('Welcome to Tic-Tac-Toe !')

while True:
    board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn+' will play first ')

    play_game = input('Are you ready to play? Enter Yes or No ')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board,turn)
            place_marker(board,player1_marker,position)

            if win_check(board,player1_marker):
                display_board(board)
                print(f'Congratulations! {turn} You won the game ')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw ')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board,turn)
            place_marker(board,player2_marker,position)

            if win_check(board,player2_marker):
                display_board(board)
                print(f'Congratulations! {turn} You won the game ')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a tie ')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break