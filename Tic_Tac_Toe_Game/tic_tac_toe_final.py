import random

def main_view(board):

    print('\n'*10)
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print(' ', board[7], ' ', '|', ' ', board[8], ' ', '|', ' ', board[9], ' ')
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print('-' * 21)
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print(' ', board[4], ' ', '|', ' ', board[5], ' ', '|', ' ', board[6], ' ')
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print('-' * 21)
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )
    print(' ', board[1], ' ', '|', ' ', board[2], ' ', '|', ' ', board[3], ' ')
    print(' ', ' ', ' ', '|', ' ', ' ', ' ', '|'' ', ' ', ' ', )


def player_marker_choice():
    print('<Hello, and welcome to a Tic Tac Toe Game>')
    # Ask a player 1 to chose X or O
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 please choose your marker X or O: ').upper()

    # Define player1 and player2 choices

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

    return (player1, player2)

def place_marker(board,marker,position):

    board[position] = marker

def win_check(board,marker):

    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))

def choose_first():
    number = random.randint(0,1)

    if number == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def blank_check(board,position):

    return board[position] == ' '

def board_check(board):

    for i in range(1,10):
        if blank_check(board,i):
            return False
    return True

def player_choice(board):

    position = 0

    while position not in range(1,10) or not blank_check(board,position):
        position = int(input('Please, select a posotion :'))

    return position

def play_again():

    choice = input('Do you want to play again? Enter Y or N')

    return choice == 'Y'



# while loop to keep running the game
print('Welcome to a Tic Tac Toe Game')

while True:

    # play the game

    ## set everything up
    test_board = [' ']*10
    player_marker1, place_marker2 = player_marker_choice()

    turn = choose_first()
    print(turn + ' goes first')

    play = input('Are you ready to play Y or N? ').upper()

    if play == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            # show the board
            main_view(test_board)
            # choose a position
            position = player_choice(test_board)

            #insert a position
            place_marker(test_board,player_marker1,position)
            #check a win
            if win_check(test_board,player_marker1):
                main_view(test_board)
                print('Player 1 has won the game')
                game_on = False
            else:
                if board_check(test_board):
                    main_view(test_board)
                    print('TIE')
                    game_on = False
                else:
                    turn = 'Player 2'



            # no TIE?
        else: #player 2 turn

                # show the board
                main_view(test_board)
                # choose a position
                position = player_choice(test_board)

                # insert a position
                place_marker(test_board, place_marker2, position)
                # check a win
                if win_check(test_board, place_marker2):
                    main_view(test_board)
                    print('Player 2 has won the game')
                    game_on = False
                else:
                    if board_check(test_board):
                        main_view(test_board)
                        print('TIE')
                        game_on = False
                    else:
                        turn = 'Player 1'

    if not play_again():
        break
# break out thr while loop


